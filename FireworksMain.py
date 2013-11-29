#coding=utf-8
'''
Created on 2013-10-17

@author: YuJin
'''
from PySide import QtGui, QtCore
from UI.ui_main import Ui_Form
from Frontend.fireNow import UiShow as FireNowWin
from Frontend.connectTest import UiShow as ConnectTestWin
import sys
from Translations.tr_rc import *
from Frontend.firework import Firework
from config import basedir
from Device.Communication import HardwareCommunicate
import Queue
import time
try:
    from Device import ftdi2 as ft
except:
    print "Unable to load ftdi2 driver"


class Main(QtGui.QWidget):
    showSignal = QtCore.Signal()
    signalDev = QtCore.Signal(bool)
    def __init__(self, parent = None):
        super(Main, self).__init__()
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.pushButtonProject.clicked.connect(self.editProject)
        self.ui.pushButtonConnect.clicked.connect(self.connectTest)
        self.ui.pushButtonFire.clicked.connect(self.handFire)
        self.ui.pushButtonExit.clicked.connect(self.cancel)
        self.showSignal.connect(self.showAgain)
        self.queuePut = Queue.Queue()
        self.queueGet = Queue.Queue()
        self.threadIsRun = False
        try:
            dev = ft.list_devices()
        except:
            dev = []
        
        if len(dev) == 0:
#            QtGui.QMessageBox.question(None,self.tr('message'),self.tr('No device connect'),QtGui.QMessageBox.Ok)
            self.deviceConnected = False
            self.checkDevice()
        else:
            self.deviceConnected = True
            self.threadStart()
            
    def checkDevice(self):
        self.timerCheckDev = QtCore.QTimer()
        self.timerCheckDev.timeout.connect(self.timeTick)
        self.timerCheckDev.setInterval(1000)
        self.timerCheckDev.start()
        
    def timeTick(self):
        try:
            dev = ft.list_devices()
        except:
            dev = []
        print 'checking device'
        if len(dev) > 0:
#             self.isconnected = True
#         else:
#             self.isconnected = False
            print 'device connected'
            self.signalDev.emit(True)
            self.deviceConnected = True
            self.timerCheckDev.stop()
            self.threadStart()

#     def getConnected(self):
#         return self.isconnected
        
    def threadStart(self):
        self.comminute = HardwareCommunicate(self.queueGet,self.queuePut)
        self.threadCommunicate = QtCore.QThread()
        self.comminute.moveToThread(self.threadCommunicate)
        self.threadCommunicate.start()
        time.sleep(0.1)
        self.comminute.signalCommunicate.emit()
    
    def connectTest(self):
        if not self.deviceConnected:
            QtGui.QMessageBox.question(None,self.tr('message'),self.tr('No fireworks device connected'),QtGui.QMessageBox.Ok)
            return
        self.connectTestForm = ConnectTestWin(self.showSignal,self.queueGet ,self.queuePut)
        self.connectTestForm.show()
        self.hide()
    
    def handFire(self):
        if not self.deviceConnected:
            QtGui.QMessageBox.question(None,self.tr('message'),self.tr('No fireworks device connected'),QtGui.QMessageBox.Ok)
            return
        self.fireNowWin = FireNowWin(self.showSignal,self.queueGet)
        self.fireNowWin.show()
        self.hide()
    
    def editProject(self):
        self.fireworks = Firework(self.showSignal,self.queueGet,self.deviceConnected,self.signalDev)
        self.fireworks.show()
        self.hide()
        
    
    def cancel(self):
        self.close()
        
    def showAgain(self):
        self.show()
        
def main():
    app = QtGui.QApplication(sys.argv)
    locale = QtCore.QLocale.system().name()
    appTranslator = QtCore.QTranslator()
    if appTranslator.load (":/Fireworks_" + locale):
        app.installTranslator (appTranslator)
    app.addLibraryPath (basedir)
    window = Main()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()

