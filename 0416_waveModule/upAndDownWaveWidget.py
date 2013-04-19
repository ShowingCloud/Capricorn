# coding=utf-8
import numpy as np
from PySide import QtGui,QtCore
import sys
import lowerPlotWidget,waveForm
from plotWidget import plotWidget
import datetime


class UpAndDownWaveWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(UpAndDownWaveWidget,self).__init__(parent)
        self.setGeometry(100,100,1000,400)
        self.plotWidget = plotWidget(self)
        self.lowerPlotWidget = lowerPlotWidget.plotWidget(self)
        self.path = None
        self.media = None
        layout=QtGui.QVBoxLayout()
        layout.addWidget(self.plotWidget)
#        layout.addSpacing(30)
        layout.addWidget(self.lowerPlotWidget)
        self.lowerPlotWidget.setFixedHeight(53)
        self.setLayout(layout)
        
        self.plotWidget.figure.signal.freshLowerPlotPanLeftAndWidth.connect\
        (self.lowerPlotWidget.figure.freshLeftAndWidthFromUpperPlot)
        self.plotWidget.figure.signal.freshLowerPlotCurrentTime.connect\
        (self.lowerPlotWidget.figure.freshCurrentTimeFromUpperPlot)
        
#        self.lowerPlotWidget.figure.signal.freshFunction.connect\
#        (self.upperPlotWidget.plotWidget.figure.freshFromLowerPlot)
         
        
    def setMedia(self, media):
        self.media = media
        
    def analyzeWaveAndDrawInit(self):
        path = str(self.media.currentSource().url().path())
        path = path[1:]
        form = waveForm.waveform(path)
        waveData = form.getWaveData()
        dataDict = dict(data=waveData, framerate=form.framerate,media=self.media)
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
    
