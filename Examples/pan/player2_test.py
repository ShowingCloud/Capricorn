'''
Created on 2013-1-29

@author: Pyroshow
'''
import sys, wave, struct
from PySide import QtCore, QtGui
from PySide.phonon import Phonon

class Player(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setGeometry(300, 100, 350, 200)
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
        self.media.setTickInterval(1000)
        self.media.finished.connect(app.quit)
        self.output = Phonon.AudioOutput(Phonon.MusicCategory, self)
        Phonon.createPath(self.media, self.output)

        self.buttonPlay = QtGui.QPushButton('Play', self)
        self.buttonPlay.setIcon(QtGui.QIcon('play.ico'))
        self.color = QtGui.QColor(255, 255, 0)
        self.buttonPlay.setStyleSheet('QWidget {background-color: %s}' % self.color.name())
        
        self.buttonStop = QtGui.QPushButton('Stop', self)
        self.buttonStop.setIcon(QtGui.QIcon('stop.ico'))
        self.color = QtGui.QColor(100, 180, 0)
        self.buttonStop.setStyleSheet('QWidget {background-color: %s}' % self.color.name())
        
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
        lowerLayout.addWidget(self.buttonPlay)
        lowerLayout.addWidget(self.buttonStop)
        lowerLayout.addWidget(self.slider)
        
        layout=QtGui.QVBoxLayout()
        layout.addLayout(upperLayout)
        layout.addLayout(midLayout)
        layout.addLayout(lowerLayout)
        self.setLayout(layout)
        
        self.media.stateChanged.connect(self.stateChanged)
        self.media.tick.connect(self.tick)
        self.buttonPlay.clicked.connect(self.changePlayPause)
        self.buttonStop.clicked.connect(self.changeStop)
        self.buttonOpen.clicked.connect(self.handleButtonChoose)
        self.buttonPlay.clicked.connect(self.analyzewave)
        
    def handleButtonChoose(self):
        dialog = QtGui.QFileDialog(self)
        dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.path = dialog.selectedFiles()[0]
            self.media.setCurrentSource(Phonon.MediaSource(self.path))
            self.media.play()
            self.fileEdit.setText(self.path)
        dialog.deleteLater()
        
    def tick(self, time):
        displayTime = QtCore.QTime(0, (time / 60000) % 60, (time / 1000) % 60)
        self.lcdTimer.display(displayTime.toString('mm:ss'))

    def analyzewave(self):
        form = waveform(self.path)
        form.waveform()

    def changePlayPause(self):
        if self.media.state() == Phonon.PlayingState:
            self.media.pause()
        else:
            self.media.play()

    def changeStop(self):
        self.media.stop()

    def stateChanged(self, newstate, oldstate):
        if newstate == Phonon.PlayingState:
            self.buttonPlay.setText('Pause')
            self.buttonPlay.setIcon(QtGui.QIcon('pause.ico'))
        elif (newstate != Phonon.LoadingState and newstate != Phonon.BufferingState):
            self.buttonPlay.setText('Play')
            self.buttonPlay.setIcon(QtGui.QIcon('play.ico'))
        if newstate == Phonon.ErrorState:
            print('ERROR: play is wrong: %s' % self.media.errorString())
global waveData
class waveform():
    def __init__(self, path):
        self.audio = wave.open(path, 'r')
        self.nchannels, self.sampwidth, self.framerate, self.nframes, self.comptype, self.compname = self.audio.getparams()
                
    def cell(self, start, size, channel):
        self.audio.setpos(start)
        data = self.audio.readframes(size)

        if channel != -1:
            data = data[:, channel]

        if self.sampwidth == 1:
            sample = struct.unpack('%sb' % size, data)
        elif self.sampwidth == 2:
            sample = struct.unpack('%sh' % size, data)
        elif self.sampwidth == 4:
            sample = struct.unpack('%si' % size, data)
        elif self.sampwidth == 8:
            sample = struct.unpack('%sq' % size, data)

        return(min(sample), max(sample))

    def read(self, starttime, endtime, number):
        start = starttime * self.framerate / 1000
        end = endtime * self.framerate / 1000
        interval =(end - start) / number
        global waveData
        waveData = []
        for i in xrange(number):
            if self.nchannels > 1:
                print self.cell(start + i * interval, interval, 0)
                print 3
#                repr(self.cell(start + i * interval, interval, 0))
#                waveData.append(self.cell(start + i * interval, interval, 0))
            
                print self.cell(start + i * interval, interval, 1)
                
            else:
                a = self.cell(start + i * interval, interval, -1)
                print a
                waveData.append(a)

    def waveform(self):
        self.read (0, 1000, 100)

app = QtGui.QApplication(sys.argv)
myapp = Player()
myapp.show()

app.exec_()

import matplotlib.pyplot as plt
import numpy as np

ax = plt.subplot(111)

global waveData

dataOne = []
dataTwo = []
t =[]
dataNumber = len(waveData)
for i in range(dataNumber):
    t.append(i)
    dataOne.append(waveData[i][0])
    dataTwo.append(waveData[i][1])
ax.plot(t,dataOne,t,dataTwo,t,[0]*dataNumber)
plt.show()
   
