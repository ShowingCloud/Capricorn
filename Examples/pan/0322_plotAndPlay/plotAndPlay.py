# coding=utf-8
import numpy as np
from PySide import QtGui,QtCore
import sys
import lowerPlotWidget,upperPlotWidget,player,waveForm
import progressWidget

import datetime


class playAndPlotWidget(QtGui.QWidget):
    def __init__(self):
        super(playAndPlotWidget,self).__init__()
        self.setGeometry(100,100,1000,400)
        self.upperPlotWidget = upperPlotWidget.plotControlWidget(self)
        self.lowerPlotWidget = lowerPlotWidget.plotWidget(self)
#        self.lowerPlotWidget.resize(1000,200)

        self.playWidget = player.Player(self)
        self.path = None
        self.playWidget.buttonPlay.clicked.connect(self.analyzewave)
        self.playWidget.timeSignal.TimeNowChanged.connect(self.upperPlotWidget.plotWidget.figure.mediaTimeChanged)
#        self.playWidget.timeSignal.TimeNowChanged.connect(self.lowerPlotWidget.figure.fresh333)
        layout=QtGui.QVBoxLayout()
        layout.addWidget(self.playWidget)
        layout.addWidget(self.upperPlotWidget)
        layout.addWidget(self.lowerPlotWidget)
        
        self.setLayout(layout)
        
        self.upperPlotWidget.plotWidget.figure.signal.freshLowerPlotPanLeftAndWidth.connect\
        (self.lowerPlotWidget.figure.freshLeftAndWidthFromUpperPlot)
        self.upperPlotWidget.plotWidget.figure.signal.freshLowerPlotCurrentTime.connect\
        (self.lowerPlotWidget.figure.freshCurrentTimeFromUpperPlot)
        
        self.lowerPlotWidget.figure.signal.freshFunction.connect\
        (self.upperPlotWidget.plotWidget.figure.freshFromLowerPlot)
         
    def analyzewave(self):
        self.oldFilePath = ''
        from PySide.phonon import Phonon
        if self.playWidget.media.state() == Phonon.StoppedState and not self.oldFilePath == self.playWidget.media.currentSource():
            self.oldFilePath = self.playWidget.media.currentSource()

            form = waveForm.waveform(self.playWidget.fileEdit.text())
            waveData = form.getWaveData()
            dataDict = dict(data=waveData, framerate=form.framerate,media=self.playWidget.media)
            self.lowerPlotWidget.figure.drawInit(waveData)
            self.upperPlotWidget.plotWidget.figure.drawInit(dataDict)
            

def main():
    Curtime1 = datetime.datetime.now()
    print 'Curtime1：',Curtime1
    
    app = QtGui.QApplication(sys.argv)
    playAndPlot = playAndPlotWidget()
    playAndPlot.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
#    import cProfile
#    cProfile.run ('main()')
    