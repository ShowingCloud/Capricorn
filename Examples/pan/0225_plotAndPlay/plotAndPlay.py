# coding=utf-8
import numpy as np
from PySide import QtGui,QtCore

import sys

import lowerPlotWidget,upperPlotWidget,player,waveForm

class playAndPlotWidget(QtGui.QWidget):
    def __init__(self):
        super(playAndPlotWidget,self).__init__()
        self.setGeometry(100,100,1000,400)
        self.plotControlWidget = upperPlotWidget.plotControlWidget(self)
        self.lowerPlotWidget = lowerPlotWidget.plotWidget(self)
#        self.lowerPlotWidget.resize(1000,200)

        self.playWidget = player.Player(self)
        
        self.playWidget.buttondisplay.clicked.connect(self.analyzewave)
#        self.playWidget.buttondisplay.clicked.connect(self.plotControlWidget.plotWidget.figure.drawImage)
        
        layout=QtGui.QVBoxLayout()
        layout.addWidget(self.playWidget)
        layout.addWidget(self.plotControlWidget)
        layout.addWidget(self.lowerPlotWidget)
        
        self.setLayout(layout)
        
        self.plotControlWidget.plotWidget.figure.signal.freshFunction.connect\
        (self.lowerPlotWidget.figure.freshFromUpperPlot)
        
        self.lowerPlotWidget.figure.signal.freshFunction.connect\
        (self.plotControlWidget.plotWidget.figure.freshFromLowerPlot)
        
    def analyzewave(self):
        form = waveForm.waveform(self.playWidget.fileEdit.text())
        self.plotControlWidget.plotWidget.figure.drawImage(form.getWaveData())
        self.lowerPlotWidget.figure.drawImage(form.getWaveData())
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    playAndPlot = playAndPlotWidget()
    playAndPlot.show()
    sys.exit(app.exec_())