from PySide import QtCore,QtGui
from UI.ui_control import ControlDialog
import sys


class ControlWinShow(QtGui.QDialog):

    def __init__(self,signalPlayOrPause,signalStop,signalMusicFinished,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.signalPlayOrPause = signalPlayOrPause
        self.musicStatus = 'play'
        self.signalStop = signalStop
        self.signalMusicFinished = signalMusicFinished
        self.ui=ControlDialog()
        self.ui.setupUi(self)
        self.ui.pushButtonStopFire.setEnabled(False)
        self.signalMusicFinished.connect(self.musicFinished)
        self.ui.pushButtonStartOrPause.clicked.connect(self.playOrPause)
        self.ui.pushButtonStopFire.clicked.connect(self.stopFire)
        
    def playOrPause(self):
        self.signalPlayOrPause.emit()
        if self.musicStatus == 'play':
            self.musicStatus = 'pause'
            self.ui.pushButtonStartOrPause.setIcon(QtGui.QIcon(':/Images/play.png'))
            self.ui.pushButtonStopFire.setEnabled(True)
        else:
            self.musicStatus = 'play'
            self.ui.pushButtonStartOrPause.setIcon(QtGui.QIcon(':/Images/pause.png'))
            self.ui.pushButtonStopFire.setEnabled(False)
            
    def stopFire(self):
        self.signalStop.emit()
        self.reject()
    
    def musicFinished(self):
        self.accept()