# -*- coding: utf-8 -*-
from PySide import QtCore
import time
try:
    import ftdi2 as ft
except:
    print "Unable to load ftdi2 driver"
    pass

class HardwareCommunicate(QtCore.QObject):
    signalCommunicate = QtCore.Signal()

    def __init__ (self, queue, parent = None):
        QtCore.QObject.__init__ (self, parent)

        self.signalCommunicate.connect(self.communicateFun)

        self.myQueue = queue

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
            item = self.myQueue.get()
            self.f.write(item[0])
            print repr(item)
            time.sleep(0.1)
            