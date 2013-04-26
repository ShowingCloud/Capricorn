# coding=utf-8
import numpy as np
from PySide import QtGui,QtCore
import sys
import lowerPlotWidget,waveForm
from plotWidget import plotWidget
import datetime

#整合上、下两个波形图类
class UpAndDownWaveWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(UpAndDownWaveWidget,self).__init__(parent)
        #设置位置与大小
        self.setGeometry(100,100,1000,400)
        self.plotWidget = plotWidget(self)
        self.lowerPlotWidget = lowerPlotWidget.plotWidget(self)
        self.path = None
        self.media = None
        #布局
        layout=QtGui.QVBoxLayout()
        #在此布局中添加上、下两个画图类
        layout.addWidget(self.plotWidget)
#        layout.addSpacing(30)
        layout.addWidget(self.lowerPlotWidget)
        self.lowerPlotWidget.setFixedHeight(53)
        self.setLayout(layout)

        #singal 、slot 连接
        #刷新矩形条的位置和宽度
        self.plotWidget.figure.signal.freshLowerPlotPanLeftAndWidth.connect\
        (self.lowerPlotWidget.figure.freshLeftAndWidthFromUpperPlot)
        #刷新当前时间
        self.plotWidget.figure.signal.freshLowerPlotCurrentTime.connect\
        (self.lowerPlotWidget.figure.freshCurrentTimeFromUpperPlot)
        
        
#        self.lowerPlotWidget.figure.signal.freshFunction.connect\
#        (self.upperPlotWidget.plotWidget.figure.freshFromLowerPlot)
         
    #设置音乐媒体类
    def setMedia(self, media):
        self.media = media

    #解析波形并将解析后的数据传给上、下两个波形图类
    def analyzeWaveAndDrawInit(self):
        path = str(self.media.currentSource().url().path())
        path = path[1:]
        form = waveForm.waveform(path)
        waveData = form.getWaveData()
        dataDict = dict(data=waveData, framerate=form.framerate,media=self.media)
        #上下两个波形图画图初始化
        self.lowerPlotWidget.figure.drawInit(waveData)
        self.plotWidget.figure.drawInit(dataDict)  
        
def main():
    Curtime1 = datetime.datetime.now()
    print 'Curtime1：',Curtime1
    
    app = QtGui.QApplication(sys.argv)
    playAndPlot = UpAndDownWaveWidget()
    playAndPlot.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
#    main()
#    import cProfile
#    cProfile.run ('main()')

    from waveModule import main
    main()
