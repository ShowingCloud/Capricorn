from PySide import QtCore,QtGui
from Ui_toolBox import Ui_toolBoxWidget
import sys
from PySide.phonon import Phonon

class Player(QtGui.QWidget):

    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_toolBoxWidget()
        self.ui.setupUi(self)
        
        self.media = Phonon.MediaObject(self)
        self.media.setCurrentSource(Phonon.MediaSource())
        self.media.setTickInterval(10)
        self.output = Phonon.AudioOutput(Phonon.MusicCategory, self)
        Phonon.createPath(self.media, self.output)
        
        self.ui.volumeSlider_music.setAudioOutput(self.output)
        
        self.ui.seekSlider_musicProgress.setMediaObject(self.media)
        
        self.ui.lcdNumber.display("00:00")
        
        
        self.media.stateChanged.connect(self.stateChanged)
        self.media.tick.connect(self.tick)
        
        self.ui.pushButton_musicPlay.clicked.connect(self.changePlayPause)
        self.ui.pushButton_musicStop.clicked.connect(self.changeStop)
#        self.ui.pushButton_chooseMusicFile.clicked.connect(self.handleButtonChoose)
        self.ui.timeEdit_music.timeChanged.connect(self.timeEditTimeChanged)
        
        self.path = None
        self.signal = FileChoosedSignal()
        
    def timeEditTimeChanged(self, time):
        miliSec = (((time.hour()*60+time.minute())*60)+time.second())*1000
        print 'miliSec',miliSec
        self.media.seek(miliSec)
#        self.ui.lcdNumber.display(time.toString('mm:ss'))
#        self.signal.TimeNowChanged.emit(time)
        
    def setMusicFilePath(self, filePath):
        self.path = filePath
        self.media.setCurrentSource(Phonon.MediaSource(self.path))
        print filePath
        
    def getPlayerMedia(self):
        return self.media
        
  
        
    def handleButtonChoose(self):
         dialog = QtGui.QFileDialog(self)
         dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
         if dialog.exec_() == QtGui.QDialog.Accepted:
             self.path = dialog.selectedFiles()[0]
             self.media.setCurrentSource(Phonon.MediaSource(self.path))
 #            totalTime = self.media.totalTime()
 #            time = QtCore.QTime(0, (totalTime / 60000) % 60, (totalTime / 1000) % 60)
 #            self.ui.timeEdit_music.setMaximumTime (time)
             self.ui.lineEdit_musicFilePath.setText(self.path)
         dialog.deleteLater()
        
#        self.path = 'C:\Users\pyroshow\Desktop\\test.wav'
#        self.path = 'C:\Users\pyroshow\Desktop\Rossini.wav'
#        self.media.setCurrentSource(Phonon.MediaSource(self.path))
#        self.media.play()
#        self.fileEdit.setText(self.path)
        
    def tick(self, time):
        displayTime = QtCore.QTime(0, (time / 60000) % 60, (time / 1000) % 60)
        self.ui.lcdNumber.display(displayTime.toString('mm:ss'))
        self.signal.TimeNowChanged.emit(time)
        
    def changePlayPause(self):
        if self.path == None:
            
            msgBox = QtGui.QMessageBox(self)
            msgBox.setText("please choose a music file first.")
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.exec_()
            return
        if self.media.state() == Phonon.PlayingState:
            self.media.pause()
        elif self.media.state() == Phonon.StoppedState:
            self.media.play()
            self.signal.fileChoosedSignal.emit()
        else:
            self.media.play()
            
    def changeStop(self):
        self.media.stop()

    def stateChanged(self, newstate, oldstate):
        if newstate == Phonon.PlayingState:
#            self.buttonPlay.setText('Pause')
            self.ui.pushButton_musicPlay.setIcon(QtGui.QIcon(":/Image/Image/pause.png"))
        elif (newstate != Phonon.LoadingState and newstate != Phonon.BufferingState):
#            self.buttonPlay.setText('Play')
            self.ui.pushButton_musicPlay.setIcon(QtGui.QIcon(":/Image/Image/play.png"))
        if newstate == Phonon.ErrorState:
            print('ERROR: play is wrong: %s' % self.media.errorString())
            
class FileChoosedSignal(QtCore.QObject):
    fileChoosedSignal = QtCore.Signal()
    TimeNowChanged = QtCore.Signal(int)
    
def main():
    app = QtGui.QApplication(sys.argv)
#    locale = QtCore.QLocale.system().name()
#    print locale
    musicPlayer = Player()
    musicPlayer.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
#    main()
    from waveModule import main
    main()
