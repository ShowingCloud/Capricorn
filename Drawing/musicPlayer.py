# coding=utf-8
from PySide import QtCore,QtGui
from Ui_toolBox import Ui_toolBoxWidget
import sys
from PySide.phonon import Phonon

#音乐播放器类
class Player(QtGui.QWidget):
    
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        #建立UI界面，UI文件用Qt自动生成
        self.ui=Ui_toolBoxWidget()
        self.ui.setupUi(self)

        #音乐媒体类
        self.media = Phonon.MediaObject(self)
        self.media.setCurrentSource(Phonon.MediaSource())
        #10ms Tick 一次
        self.media.setTickInterval(10)
        self.output = Phonon.AudioOutput(Phonon.MusicCategory, self)
        Phonon.createPath(self.media, self.output)

        self.ui.volumeSlider_music.setAudioOutput(self.output)
        
        #音乐播放器的进度条
        self.ui.seekSlider_musicProgress.setMediaObject(self.media)

        #LCD显示当前播放到的时刻
        self.ui.lcdNumber.display("00:00")
        
        #media状态改变时触发函数stateChanged
        self.media.stateChanged.connect(self.stateChanged)
        
        #每tick一次调self.tick
        self.media.tick.connect(self.tick)

        #信号连接
        #点play按钮后改变play、pause 图标
        self.ui.pushButton_musicPlay.clicked.connect(self.changePlayPause)
        #停止
        self.ui.pushButton_musicStop.clicked.connect(self.changeStop)
        #timeEdit控件控制跳转到指定的时刻
        self.ui.timeEdit_music.timeChanged.connect(self.timeEditTimeChanged)
        
        self.path = None
        self.signal = FileChoosedSignal()
        
    def timeEditTimeChanged(self, time):
        #时间转换成以ms为单位
        miliSec = (((time.hour()*60+time.minute())*60)+time.second())*1000
        self.media.seek(miliSec)
#        self.ui.lcdNumber.display(time.toString('mm:ss'))
#        self.signal.TimeNowChanged.emit(time)

    #设置音乐的路径
    def setMusicFilePath(self, filePath):
        self.signal.fileChoosedSignal.emit()
        self.path = filePath
        self.media.setCurrentSource(Phonon.MediaSource(self.path))
        print filePath

    #供外部获取media 对象
    def getPlayerMedia(self):
        return self.media
        
  
    #点open file 按钮时，触发打开并选中音乐文件操作
    def handleButtonChoose(self):
         #文件选择对话框
         dialog = QtGui.QFileDialog(self)
         dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
         if dialog.exec_() == QtGui.QDialog.Accepted:
             self.path = dialog.selectedFiles()[0]
             self.media.setCurrentSource(Phonon.MediaSource(self.path))
 #            totalTime = self.media.totalTime()
 #            time = QtCore.QTime(0, (totalTime / 60000) % 60, (totalTime / 1000) % 60)
 #            self.ui.timeEdit_music.setMaximumTime (time)
             self.ui.lineEdit_musicFilePath.setText(self.path)
         #删除对话框
         dialog.deleteLater()
        
#        self.path = 'C:\Users\pyroshow\Desktop\\test.wav'
#        self.path = 'C:\Users\pyroshow\Desktop\Rossini.wav'
#        self.media.setCurrentSource(Phonon.MediaSource(self.path))
#        self.media.play()
#        self.fileEdit.setText(self.path)

    #当前播放时间显示
    def tick(self, time):
        displayTime = QtCore.QTime(0, (time / 60000) % 60, (time / 1000) % 60)
        self.ui.lcdNumber.display(displayTime.toString('mm:ss'))
        self.signal.TimeNowChanged.emit(time)

    #播放暂停切换
    def changePlayPause(self):
        if self.path == None:
            msgBox = QtGui.QMessageBox(self)
            msgBox.setText("please choose a music file first.")
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.exec_()
            return
        if self.media.state() == Phonon.PlayingState:
            self.media.pause()
#        elif self.media.state() == Phonon.StoppedState:
#            self.media.play()
        else:
            self.media.play()

    #停止意味着音乐播放至0时刻并暂停
    def changeStop(self):
        self.media.seek(0)
        self.media.pause()

    #改变播放、暂停的按钮图标
    def stateChanged(self, newstate, oldstate):
        if newstate == Phonon.PlayingState:
#            self.buttonPlay.setText('Pause')
            self.ui.pushButton_musicPlay.setIcon(QtGui.QIcon(":/Image/Image/pause.png"))
        elif (newstate != Phonon.LoadingState and newstate != Phonon.BufferingState):
#            self.buttonPlay.setText('Play')
            self.ui.pushButton_musicPlay.setIcon(QtGui.QIcon(":/Image/Image/play.png"))
        if newstate == Phonon.ErrorState:
            print('ERROR: play is wrong: %s' % self.media.errorString())

#信号类
class FileChoosedSignal(QtCore.QObject):
    fileChoosedSignal = QtCore.Signal()
    TimeNowChanged = QtCore.Signal(int)

#主函数
def main():
    app = QtGui.QApplication(sys.argv)
#    locale = QtCore.QLocale.system().name()
#    print locale
    musicPlayer = Player()
    musicPlayer.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
#    from waveModule import main
#    main()
