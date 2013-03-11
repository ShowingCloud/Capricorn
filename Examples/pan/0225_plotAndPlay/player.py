# coding=utf-8
from PySide import QtGui,QtCore
import sys
from PySide.phonon import Phonon
class Player(QtGui.QWidget):
    playerData = []
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setWindowTitle('Player')
        self.color = QtGui.QColor(0, 255, 0)
#        self.setStyleSheet('QWidget {background-color: %s}' % self.color.name())
#        self.setAutoFillBackground(True)
#        back = QtGui.QPalette()
#        back.setBrush(self.backgroundRole(), QtGui.QBrush('back.png'))
#        self.setPalette(back)
        self.setWindowIcon(QtGui.QIcon('myplayer.png'))

        self.media = Phonon.MediaObject(self)
        
        self.media.setCurrentSource(Phonon.MediaSource())
        self.media.setTickInterval(10)
#        self.media.finished.connect(app.quit)
        self.output = Phonon.AudioOutput(Phonon.MusicCategory, self)
        Phonon.createPath(self.media, self.output)

        self.buttonPlay = QtGui.QPushButton('Play', self)
        self.buttonPlay.setIcon(QtGui.QIcon('play.ico'))
        self.color = QtGui.QColor(255, 255, 0)
        self.buttonPlay.setStyleSheet('QWidget {background-color: %s}' % self.color.name())
        
#        self.buttondisplay = QtGui.QPushButton('display Figure', self)
#        self.color = QtGui.QColor(55, 155, 0)
#        self.buttondisplay.setStyleSheet('QWidget {background-color: %s}' % self.color.name())
        
#        self.comboboxShowImage = QtGui.QComboBox(self)
#        years = ["show two images","show only upper one","show only lower one"]
#        self.comboboxShowImage.addItems(years)
                
        self.buttonStop = QtGui.QPushButton('Stop', self)
        self.buttonStop.setIcon(QtGui.QIcon('stop.ico'))
        self.color = QtGui.QColor(100, 180, 0)
        self.buttonStop.setStyleSheet('QWidget {background-color: %s}' % self.color.name())
        
#        self.buttonPause = QtGui.QPushButton('Pause', self)
#        self.color = QtGui.QColor(10, 180, 22)
#        self.buttonPause.setStyleSheet('QWidget {background-color: %s}' % self.color.name())
#        
        self.slider = Phonon.VolumeSlider(self)
        self.slider.setAudioOutput(self.output)
        
        self.buttonOpen = QtGui.QPushButton('Choose File', self)
        self.buttonOpen.setIcon(QtGui.QIcon('open.ico'))
        self.color = QtGui.QColor(90, 220, 150)
        self.buttonOpen.setStyleSheet('QWidget {background-color: %s}' % self.color.name())
        
        self.progressbar = Phonon.SeekSlider()
        self.progressbar.setMediaObject(self.media)
        self.color = QtGui.QColor(0, 0, 150)
        self.progressbar.setStyleSheet('QWidget {background-color: %s}' % self.color.name())
        
        self.fileLabel = QtGui.QLabel("File")
        self.fileEdit = QtGui.QLineEdit()
        self.fileLabel.setBuddy(self.fileEdit)
        self.color = QtGui.QColor(255, 255, 255)
        self.fileEdit.setStyleSheet('QWidget {background-color: %s}' % self.color.name())
        
        self.lcdTimer=QtGui.QLCDNumber()
        self.lcdTimer.display("00:00")
        self.color = QtGui.QColor(0, 255, 0)
        self.lcdTimer.setStyleSheet('QWidget {background-color: %s}' % self.color.name())

        upperLayout=QtGui.QHBoxLayout()
        upperLayout.addWidget(self.fileLabel)
        upperLayout.addWidget(self.fileEdit)
        upperLayout.addWidget(self.buttonOpen)
        
        midLayout=QtGui.QHBoxLayout()
        midLayout.addWidget(self.progressbar)
        midLayout.addWidget(self.lcdTimer)
        
        lowerLayout=QtGui.QHBoxLayout()
#        lowerLayout.addWidget(self.buttondisplay)
#        lowerLayout.addWidget(self.comboboxShowImage)
        lowerLayout.addWidget(self.buttonPlay)
        lowerLayout.addWidget(self.buttonStop)
#        lowerLayout.addWidget(self.buttonPause)
        lowerLayout.addWidget(self.slider)
        
        layout=QtGui.QVBoxLayout()
        layout.addLayout(upperLayout)
        layout.addLayout(midLayout)
        layout.addLayout(lowerLayout)
        self.setLayout(layout)
        self.setGeometry(300, 50, 350, 150)
        
        self.media.stateChanged.connect(self.stateChanged)
        self.media.tick.connect(self.tick)
        self.buttonPlay.clicked.connect(self.changePlayPause)
        self.buttonStop.clicked.connect(self.changeStop)
        self.buttonOpen.clicked.connect(self.handleButtonChoose)
        
    def handleButtonChoose(self):
        dialog = QtGui.QFileDialog(self)
        dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.path = dialog.selectedFiles()[0]
            self.media.setCurrentSource(Phonon.MediaSource(self.path))
#            self.media.play()
            self.fileEdit.setText(self.path)
        dialog.deleteLater()
#        self.path = 'C:\Users\pyroshow\Desktop\\test.wav'
#        self.path = 'C:\Users\pyroshow\Desktop\Rossini.wav'
#        self.media.setCurrentSource(Phonon.MediaSource(self.path))
##        self.media.play()
#        self.fileEdit.setText(self.path)
        
    def tick(self, time):
##        print 'player'
#        print 'time',time
#        print 'currentTime',self.media.currentTime()
        displayTime = QtCore.QTime(0, (time / 60000) % 60, (time / 1000) % 60)
        self.lcdTimer.display(displayTime.toString('mm:ss'))

    
    def changePlayPause(self):
        
#        print 'total time',self.media.totalTime()
#        print 'currentTime',self.media.currentTime()
        if self.media.state() == Phonon.PlayingState:
            print '1'
            self.media.pause()
            print '2'
        else:
#            self.media.pause()
            self.media.play()

    def changeStop(self):
        self.media.stop()

    def stateChanged(self, newstate, oldstate):
#        print '------'
#        print 'newstate=',repr(newstate)
#        print 'oldstate=',repr(oldstate)
        if newstate == Phonon.PlayingState:
            self.buttonPlay.setText('Pause')
            self.buttonPlay.setIcon(QtGui.QIcon('pause.ico'))
        elif (newstate != Phonon.LoadingState and newstate != Phonon.BufferingState):
            self.buttonPlay.setText('Play')
            self.buttonPlay.setIcon(QtGui.QIcon('play.ico'))
        if newstate == Phonon.ErrorState:
            print('ERROR: play is wrong: %s' % self.media.errorString())
            
            
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    player = Player()
    player.show()
    sys.exit(app.exec_())
            