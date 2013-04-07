# coding=utf-8
import numpy as np
from PySide import QtGui,QtCore
import sys
import lowerPlotWidget,upperPlotWidget,waveForm

import datetime


class UpAndDownWaveWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(UpAndDownWaveWidget,self).__init__(parent)
        self.setGeometry(100,100,1000,400)
        self.upperPlotWidget = upperPlotWidget.plotControlWidget(self)
        self.lowerPlotWidget = lowerPlotWidget.plotWidget(self)
        self.path = None
        self.media = None
        layout=QtGui.QVBoxLayout()
        layout.addWidget(self.upperPlotWidget)
        layout.addWidget(self.lowerPlotWidget)
        
        self.setLayout(layout)
        
        self.upperPlotWidget.plotWidget.figure.signal.freshLowerPlotPanLeftAndWidth.connect\
        (self.lowerPlotWidget.figure.freshLeftAndWidthFromUpperPlot)
        self.upperPlotWidget.plotWidget.figure.signal.freshLowerPlotCurrentTime.connect\
        (self.lowerPlotWidget.figure.freshCurrentTimeFromUpperPlot)
        
#        self.lowerPlotWidget.figure.signal.freshFunction.connect\
#        (self.upperPlotWidget.plotWidget.figure.freshFromLowerPlot)
         
#    def setMusicFilePath(self,  path):
#        self.path = path
#        
#    def setPlayerMedia(self,  media):
#        self.media = media
        
    def setMedia(self, media):
        self.media = media
        
    def analyzeWaveAndDrawInit(self):
        path = str(self.media.currentSource().url().path())
        path = path[1:]
#        self.oldFilePath = ''
#        from PySide.phonon import Phonon
#        if self.playWidget.media.state() == Phonon.StoppedState and not self.oldFilePath == self.playWidget.media.currentSource():
#            self.oldFilePath = self.playWidget.media.currentSource()
#        print 'self.path=',self.path
        form = waveForm.waveform(path)
        waveData = form.getWaveData()
        dataDict = dict(data=waveData, framerate=form.framerate,media=self.media)
        self.lowerPlotWidget.figure.drawInit(waveData)
        self.upperPlotWidget.plotWidget.figure.drawInit(dataDict)
        
        
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
    
