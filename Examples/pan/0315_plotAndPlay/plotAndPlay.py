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
         
    def analyzewave(self):
        self.oldFilePath = ''
        from PySide.phonon import Phonon
        if self.playWidget.media.state() == Phonon.StoppedState and not self.oldFilePath == self.playWidget.media.currentSource():
            self.oldFilePath = self.playWidget.media.currentSource()
            Curtime2 = datetime.datetime.now()
            print 'Curtime2：',Curtime2
            form = waveForm.waveform(self.playWidget.fileEdit.text())
            waveData = form.getWaveData()
            Curtime3 = datetime.datetime.now()
            print 'Curtime3：',Curtime3
            dataDict = dict(data=waveData, framerate=form.framerate,media=self.playWidget.media)
            self.upperPlotWidget.plotWidget.figure.drawImage(dataDict)
            Curtime4 = datetime.datetime.now()
            print 'Curtime4：',Curtime4
            self.lowerPlotWidget.figure.drawImage(waveData)
            Curtime5 = datetime.datetime.now()
            print 'Curtime5：',Curtime5
            
def main():
    Curtime1 = datetime.datetime.now()
    print 'Curtime1：',Curtime1
    
    app = QtGui.QApplication(sys.argv)
    playAndPlot = playAndPlotWidget()
    playAndPlot.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
    