# coding=utf-8
import numpy as np
from PySide import QtGui,QtCore
import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.collections import PatchCollection
import matplotlib.patches as mpatches
from matplotlib import mpl
import waveForm
import sys
from PySide.phonon import Phonon

#画板类，用以将figure 对象封装成一个控制对象
class plotWidget(FigureCanvas):
    def __init__(self, parent=None):
        self.figure = fig()
        super(plotWidget,self).__init__(self.figure)
        self.setParent(parent)
        self.setWindowTitle("pyside test_plot fig FigureCanvas")
    

#figure 类，用于画图   
class fig(Figure):
    def __init__(self):
        super(fig,self).__init__()
        self.ax = None
        #每屏显示1000个数据点
        self.dotsInScreen = 1000
        #刷新信号
        self.signal = freshSignal()

    #upper plot figure 图像放大缩小时，调用此函数
    def freshLeftAndWidthFromUpperPlot(self,leftFrame, rightFrame):
        if self.ax == None:
            return
        else:
            self.leftDot = leftFrame/self.zipRate
            self.rightDot = rightFrame/self.zipRate
            xy = np.array([[self.leftDot,0.],[self.leftDot,1.],[self.rightDot,1.],[self.rightDot,0.],[self.leftDot,0.]])
            self.span.set_xy(xy)
        self.canvas.draw()

    # 当时播放时刻 (current time) 改变时调用此函数
    def freshCurrentTimeFromUpperPlot(self,frameNow):
        if hasattr(self, 'vline'):
            self.vline.set_xdata(frameNow/self.zipRate)
            self.canvas.draw()
        

#    
#
#    def freshCurrentTime(self):
#        dotNow = int(self.currentTime_ms*self.framerate/1000/self.zipRate)
#        self.vline.set_xdata(dotNow)
#        self.canvas.draw()

    #画图初始化函数
    def drawInit(self,waveData):
        #清空图像
        self.clf()
        #将解析出来的数据进行处理
        self.plotDataDict = self.plotDataProcess(waveData)
        self.ax = self.add_axes([0,0,1,1])
        #竖直线，表示当前时间
        self.vline = self.ax.axvline(x=10,color='red',zorder=3)
        #与x轴重合的水平钱
        self.ax.axhline(y=0,color='0.8',zorder=2)
        #矩形块
        self.span = self.ax.axvspan(0, 0, facecolor='g', alpha=0.5,zorder=2)
        #画图
        self.plotFunc(self.plotDataDict)
        #设置x轴的边界
        self.ax.set_xlim(0,self.dotsInScreen)
        #轴线隐藏
        self.ax.set_axis_off()
        #图像背景颜色
        self.set_facecolor("#ffffff")
#        print dir(self)
        #刷新
        self.canvas.draw()

    def plotFunc(self,plotDataDict):
        xarray = np.arange(self.dotsInScreen)
        #双声道
        if plotDataDict.has_key('y_mean_2'):
            #最大值，最小值，2个平均值
            ymax = plotDataDict['y_max']
            ymin = plotDataDict['y_min']
            #平均值放大20倍，方便看清楚
            ymean = plotDataDict['y_mean']*20
            ymean2 = plotDataDict['y_mean_2']*20
            self.fillPlot = self.ax.fill_between(xarray, ymax, y2=ymin ,color='#DDA0DD', zorder=0)
            self.linePlot = self.ax.plot(xarray,ymean,'pink',xarray,ymean2,'y',zorder=1)
        #单声道
        else:
            ymax = plotDataDict['y_max']
            ymin = plotDataDict['y_min']
            ymean = plotDataDict['y_mean']*20
            self.fillPlot = self.ax.fill_between(xarray, ymax, y2=ymin ,color='#DDA0DD', zorder=0)
            self.linePlot = self.ax.plot(xarray,ymean,'b',zorder=1)
            
        
    def plotDataProcess(self, waveData):
        if isinstance(waveData, list):
            dataOne = waveData[0]
            dataTwo = waveData[1]
            dataLength = len(dataOne)
            numchunks = self.dotsInScreen
            chunksize = dataLength // numchunks
            self.zipRate = chunksize
            
            team_1 = dataOne[:chunksize*numchunks].reshape((-1, chunksize))
            team_2 = dataTwo[:chunksize*numchunks].reshape((-1, chunksize))
            max_1 = team_1.max(axis=1)
            max_2 = team_2.max(axis=1)
            max_1_2 = np.maximum(max_1,max_2)
            
            min_1 = team_1.min(axis=1)
            min_2 = team_2.min(axis=1)
            min_1_2 = np.minimum(min_1,min_2)
            
            mean_1 = team_1.mean(axis=1)
            mean_2 = team_2.mean(axis=1)
            plotDataDict = dict(y_max=max_1_2, y_min=min_1_2, y_mean=mean_1, y_mean_2=mean_2)
            
        else:
            dataOne = waveData
            dataLength = len(dataOne)
            numchunks = self.dotsInScreen
            chunksize = dataLength // numchunks
            self.zipRate = chunksize        
            team_1 = dataOne[:chunksize*numchunks].reshape((-1, chunksize))
            max_1 = team_1.max(axis=1)
            min_1 = team_1.min(axis=1)
            mean_1 = team_1.mean(axis=1)
            plotDataDict = dict(y_max=max_1, y_min=min_1, y_mean=mean_1)
        return plotDataDict
        
    
    

class freshSignal(QtCore.QObject):
    freshFunction = QtCore.Signal(int)
    
if __name__ == '__main__':
#    import time
    app = QtGui.QApplication(sys.argv)
    dialog = QtGui.QFileDialog()
    dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
    path = 0
    if dialog.exec_() == QtGui.QDialog.Accepted:
        path = dialog.selectedFiles()[0]
#        print path
    dialog.deleteLater()
    print path
    form = waveForm.waveform(path)
    plot_Widget = plotWidget()
#    time.sleep(2)
    plot_Widget.figure.drawInit(form.getWaveData())
#    plot_Widget.figure.drawImage((1,8,3))
    plot_Widget.show()
 
    sys.exit(app.exec_())
    
