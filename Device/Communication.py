# -*- coding: utf-8 -*-
from PySide import QtCore
import time
import struct
try:
    import ftdi2 as ft
except:
    print "Unable to load ftdi2 driver"
    pass

CONNECT_TEST = 0x01
FIRE = 0x02

class HardwareCommunicate(QtCore.QObject):
    signalCommunicate = QtCore.Signal() 

    def __init__ (self, queueGet,queuePut, parent = None):
        QtCore.QObject.__init__ (self, parent)

        self.signalCommunicate.connect(self.communicateFun)
        self.queueGet = queueGet
        self.queuePut = queuePut

    def communicateFun (self):
        try:
            dev = ft.list_devices()
        except:
            dev = []

        while len (dev) == 0:
            time.sleep (5) 
            print "Rechecking hardware connection..."
            try:
                dev = ft.list_devices()
            except:
                dev = []

        self.f = ft.open_ex(dev[0])
        print self.f

        while True:
            item = self.queueGet.get()
            if item[0]== CONNECT_TEST:
                self.f.write(item[1])
#                 print repr(item[1]),'connect test....'
                time.sleep(0.1)
                readData = self.f.read (self.f.get_queue_status())
                print repr(readData),'read device data.....'
                
                listHead = self.getConnectedList(readData)
                self.queuePut.put(listHead)
                
            elif item[0] == FIRE:
                self.f.write(item[1])
#                 print repr(item[1]),'Fire........'
                time.sleep(0.1)
                readData = self.f.read (self.f.get_queue_status())
                
    def getConnectedList(self,readData):
        fmtR = '@14B'
        datalistR = [None]*14
        (datalistR[0],datalistR[1],datalistR[2],datalistR[3],datalistR[4],datalistR[5],
        datalistR[6],datalistR[7],datalistR[8],datalistR[9],datalistR[10],datalistR[11],
        datalistR[12],datalistR[13]) = struct.unpack(fmtR,readData)

        listHead = [1] * 16
        allHead = datalistR[10] * 256 + datalistR[11]
        a = 1
            
        for i in range(16):
            if a & allHead:
                listHead[i] = 0
            a  = a * 2
        return listHead
    