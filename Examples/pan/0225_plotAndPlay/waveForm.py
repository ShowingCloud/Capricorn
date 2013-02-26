# coding=utf-8
import numpy as np
from PySide import QtGui,QtCore

import sys, wave, struct

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
        data = struct.unpack ('<%d%s' % (len (data) / sw,
            wave._array_fmts[sw]), data)

        nc = self.audio.getnchannels()
        if nc > 1:
            left = [data[si] for si in xrange (0, len (data), nc)]
            right = [data[si] for si in xrange (1, len (data), nc)]
            sample = []
            sample.append (left)
            sample.append (right)
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
    print 'waveData.__class__ =', waveData.__class__
#    
#    if isinstance(wave, list):
#        dataOne = wave[0]
#        dataTwo = wave[1]
#        print 'dataOne[0:30]=',dataOne[0:30]
#        print 'dataTwo[0:30]=',dataTwo[0:30]
#    else:
#        dataOne = wave
#        print 'dataOne[30]= ',dataOne[0:30]
    len = len(waveData)     
    print 'len=',len
    print 'analysis succeed!'
    sys.exit(app.exec_())
     
    