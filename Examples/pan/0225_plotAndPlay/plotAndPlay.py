# coding=utf-8
import numpy as np
from PySide import QtGui,QtCore

import sys

import lowerPlotWidget,upperPlotWidget,player,waveForm
import progressWidget

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

        layout=QtGui.QVBoxLayout()
        layout.addWidget(self.playWidget)
        layout.addWidget(self.upperPlotWidget)
        layout.addWidget(self.lowerPlotWidget)
        
        self.setLayout(layout)
        
#        self.playWidget.media.tick.connect(self.lowerPlotWidget.figure.freshFromUpperPlot)
        
        self.upperPlotWidget.plotWidget.figure.signal.freshFunction.connect\
        (self.lowerPlotWidget.figure.freshFromUpperPlot)
#        
#        self.lowerPlotWidget.figure.signal.freshFunction.connect\
#        (self.upperPlotWidget.plotWidget.figure.freshFromLowerPlot)
#        
    def slotAdd(self):
        pass
        
    def analyzewave(self):
#        pass
#        newThread_progressWindow = progressWidget.newThread(self)
#        newThread_progressWindow.start()
#        self.connect(self.newThread_progressWindow,SIGNAL('output(QString)'),self.slotAdd)
        form = waveForm.waveform(self.playWidget.fileEdit.text())
        waveData = form.getWaveData()
##        
#        import sys
#        print 'sizeof waveData', sys.getsizeof (waveData)
#        del waveData
        dataDict = dict(data=waveData, framerate=form.framerate,media=self.playWidget.media)
#        print 'sizeof waveData',waveData[0].__sizeof__()
        self.upperPlotWidget.plotWidget.figure.drawImage(dataDict)
        self.lowerPlotWidget.figure.drawImage(waveData)
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    playAndPlot = playAndPlotWidget()
    playAndPlot.show()
    sys.exit(app.exec_())