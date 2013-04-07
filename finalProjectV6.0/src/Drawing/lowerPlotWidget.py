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

class plotWidget(FigureCanvas):
    def __init__(self, parent=None):
        self.figure = fig()
        super(plotWidget,self).__init__(self.figure)
        self.setParent(parent)
        self.setWindowTitle("pyside test_plot fig FigureCanvas")
    
        
class fig(Figure):
    def __init__(self):
        super(fig,self).__init__()
        self.ax = None
        self.dotsInScreen = 1000
        self.signal = freshSignal()
        
    def freshLeftAndWidthFromUpperPlot(self,leftFrame, rightFrame):
        if self.ax == None:
            return
        else:
            self.leftDot = leftFrame/self.zipRate
            self.rightDot = rightFrame/self.zipRate
            xy = np.array([[self.leftDot,0.],[self.leftDot,1.],[self.rightDot,1.],[self.rightDot,0.],[self.leftDot,0.]])
            self.span.set_xy(xy)
        self.canvas.draw()
    
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
        
    def drawInit(self,waveData):
        self.clf()
        self.plotDataDict = self.plotDataProcess(waveData)
        self.ax = self.add_axes([0.1,0.1,0.8,0.8])
        self.vline = self.ax.axvline(x=10,color='red',zorder=3)
        self.span = self.ax.axvspan(0, 0, facecolor='g', alpha=0.5,zorder=2)
        self.plotFunc(self.plotDataDict)
        self.ax.set_xlim(0,self.dotsInScreen)
        self.canvas.draw()

    def plotFunc(self,plotDataDict):
        xarray = np.arange(self.dotsInScreen)
        if plotDataDict.has_key('y_mean_2'):
            ymax = plotDataDict['y_max']
            ymin = plotDataDict['y_min']
            ymean = plotDataDict['y_mean']
            ymean2 = plotDataDict['y_mean_2']
            self.fillPlot = self.ax.fill_between(xarray, ymax, y2=ymin ,color='#108070', zorder=0)
            self.linePlot = self.ax.plot(xarray,ymean,'pink',xarray,ymean2,'y',zorder=1)
        else:
            ymax = plotDataDict['y_max']
            ymin = plotDataDict['y_min']
            ymean = plotDataDict['y_mean']
            self.fillPlot = self.ax.fill_between(xarray, ymax, y2=ymin , zorder=0)
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
    