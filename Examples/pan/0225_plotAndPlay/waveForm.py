# coding=utf-8
import numpy
from PySide import QtGui,QtCore

import sys, wave
import time
from PySide.phonon import Phonon

class waveform():
    def __init__(self, path):
        self.waveData = []
        self.audio = wave.open(path, 'r')
        self.nchannels, self.sampwidth, self.framerate, self.nframes, self.comptype, self.compname \
                 = self.audio.getparams()
        self.waveform()
        
    def read (self, size):
        data = self.audio.readframes (size)

        sw = self.audio.getsampwidth()
        data = numpy.frombuffer (data, dtype = numpy.dtype ("i%d" % sw))

        nc = self.audio.getnchannels()
        if nc > 1:
            left = data[0::nc]
            right = data[1::nc]
            sample = [left, right]
        else:
            sample = data

        return sample


    def waveform (self):
        self.waveData = self.read (self.audio.getnframes())
        
    def getWaveData(self):
        return self.waveData
    def getTotalDataNumber(self):
        return self.nframes

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dialog = QtGui.QFileDialog()
    dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
    path = 0
    if dialog.exec_() == QtGui.QDialog.Accepted:
        path = dialog.selectedFiles()[0]
    dialog.deleteLater()
    
    form = waveform(path)
    waveData = form.getWaveData()
#    print 'waveData.__class__ =', waveData.__class__
#    
#    if isinstance(wave, list):
#        dataOne = wave[0]
#        dataTwo = wave[1]
#        print 'dataOne[0:30]=',dataOne[0:30]
#        print 'dataTwo[0:30]=',dataTwo[0:30]
#    else:
#        dataOne = wave
#        print 'dataOne[30]= ',dataOne[0:30]
    len = sys.getsizeof(waveData)
    print 'len=',len
    print 'analysis succeed!'
    print form.audio.getparams()
    
    time.sleep(30)
    sys.exit(app.exec_())
     
    