from PySide import QtCore, QtGui
from UI.ui_fireNow import Ui_Dialog
from Device.protocol import dataPack
import sys
import struct
import Queue
import time

try:
    from Device import ftdi2 as ft
except:
    print "Unable to load ftdi2 driver"
    pass


class getMessage (QtCore.QObject):
    signalRead = QtCore.Signal()

    def __init__(self, q, parent = None):
        QtCore.QObject.__init__ (self, parent)

        self.signalRead.connect(self.readFun)

        self.q = q

    def readFun(self):
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
            item = self.q.get()
            if item == False:
                return
            self.f.write(item)
            print repr(item)


class UiShow(QtGui.QDialog):

    def __init__(self,signalClose,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.signalClose = signalClose
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.buttonConnect()
        self.confirmFlag = None

        self.data = {'head':0xAAF0,'length':0x0E,'function':0x02,
                     'ID':0xAABBCCDD,'fireBox':None,'firePoint':None,
                     'crc':0,'tail':0xDD}
        intVal = QtGui.QIntValidator()
        self.ui.lineEditBoxID.setValidator(intVal)
        self.q = Queue.Queue()
        self.c = getMessage(self.q)
        thread = QtCore.QThread()
        self.c.moveToThread(thread)
        thread.start()
        time.sleep(1)
        self.c.signalRead.emit()
        self.boxChanged()
        
    def closeEvent(self, event):
        self.signalClose.emit()
        self.q.put(False)
        event.accept()
    
    def buttonConnect(self):
        self.ui.lineEditBoxID.textChanged.connect(self.boxChanged)
        self.ui.ButtonConfirm.clicked.connect(self.confirm)
        self.ui.boxA1Button.clicked.connect(self.buttonPushed1)
        self.ui.boxA2Button.clicked.connect(self.buttonPushed2)
        self.ui.boxA3Button.clicked.connect(self.buttonPushed3)
        self.ui.boxA4Button.clicked.connect(self.buttonPushed4)
        self.ui.boxA5Button.clicked.connect(self.buttonPushed5)
        self.ui.boxA6Button.clicked.connect(self.buttonPushed6)
        self.ui.boxA7Button.clicked.connect(self.buttonPushed7)
        self.ui.boxA8Button.clicked.connect(self.buttonPushed8)
        self.ui.boxA9Button.clicked.connect(self.buttonPushed9)
        self.ui.boxA10Button.clicked.connect(self.buttonPushed10)
        self.ui.boxA11Button.clicked.connect(self.buttonPushed11)
        self.ui.boxA12Button.clicked.connect(self.buttonPushed12)
        self.ui.boxA13Button.clicked.connect(self.buttonPushed13)
        self.ui.boxA14Button.clicked.connect(self.buttonPushed14)
        self.ui.boxA15Button.clicked.connect(self.buttonPushed15)
        self.ui.boxA16Button.clicked.connect(self.buttonPushed16)

    def confirm(self):
        if self.ui.lineEditBoxID.text() == '':
            return
        self.data['fireBox'] = int(self.ui.lineEditBoxID.text())
        self.confirmFlag = 'confirm'
        self.ui.boxA1Button.setEnabled(True)
        self.ui.boxA2Button.setEnabled(True)
        self.ui.boxA3Button.setEnabled(True)
        self.ui.boxA4Button.setEnabled(True)
        self.ui.boxA5Button.setEnabled(True)
        self.ui.boxA6Button.setEnabled(True)
        self.ui.boxA7Button.setEnabled(True)
        self.ui.boxA8Button.setEnabled(True)
        self.ui.boxA9Button.setEnabled(True)
        self.ui.boxA10Button.setEnabled(True)
        self.ui.boxA11Button.setEnabled(True)
        self.ui.boxA12Button.setEnabled(True)
        self.ui.boxA13Button.setEnabled(True)
        self.ui.boxA14Button.setEnabled(True)
        self.ui.boxA15Button.setEnabled(True)
        self.ui.boxA16Button.setEnabled(True)
    def buttonPushed1(self):
        if self.confirmFlag == 'confirm':
            print 'Box is ',self.data['fireBox'],', Head is ',1
            self.data['firePoint'] = 1
            self.downloadData()

    def buttonPushed2(self):
        if self.confirmFlag == 'confirm':
            print 'Box is ',self.data['fireBox'],', Head is ',2
            self.data['firePoint'] = 2
            self.downloadData()

    def buttonPushed3(self):
        if self.confirmFlag == 'confirm':
            print 'Box is ',self.data['fireBox'],', Head is ',3
            self.data['firePoint'] = 3
            self.downloadData()

    def buttonPushed4(self):
        if self.confirmFlag == 'confirm':
            print 'Box is ',self.data['fireBox'],', Head is ',4
            self.data['firePoint'] = 4
            self.downloadData()

    def buttonPushed5(self):
        if self.confirmFlag == 'confirm':
            print 'Box is ',self.data['fireBox'],', Head is ',5
            self.data['firePoint'] = 5
            self.downloadData()

    def buttonPushed6(self):
        if self.confirmFlag == 'confirm':
            print 'Box is ',self.data['fireBox'],', Head is ',6
            self.data['firePoint'] = 6
            self.downloadData()

    def buttonPushed7(self):
        if self.confirmFlag == 'confirm':
            print 'Box is ',self.data['fireBox'],', Head is ',7
            self.data['firePoint'] = 7
            self.downloadData()

    def buttonPushed8(self):
        if self.confirmFlag == 'confirm':
            print 'Box is ',self.data['fireBox'],', Head is ',8
            self.data['firePoint'] = 8
            self.downloadData()

    def buttonPushed9(self):
        if self.confirmFlag == 'confirm':
            print 'Box is ',self.data['fireBox'],', Head is ',9
            self.data['firePoint'] = 9
            self.downloadData()

    def buttonPushed10(self):
        if self.confirmFlag == 'confirm':
            print 'Box is ',self.data['fireBox'],', Head is ',10
            self.data['firePoint'] = 10
            self.downloadData()

    def buttonPushed11(self):
        if self.confirmFlag == 'confirm':
            print 'Box is ',self.data['fireBox'],', Head is ',11
            self.data['firePoint'] = 11
            self.downloadData()

    def buttonPushed12(self):
        if self.confirmFlag == 'confirm':
            print 'Box is ',self.data['fireBox'],', Head is ',12
            self.data['firePoint'] = 12
            self.downloadData()

    def buttonPushed13(self):
        if self.confirmFlag == 'confirm':
            print 'Box is ',self.data['fireBox'],', Head is ',13
            self.data['firePoint'] = 13
            self.downloadData()

    def buttonPushed14(self):
        if self.confirmFlag == 'confirm':
            print 'Box is ',self.data['fireBox'],', Head is ',14
            self.data['firePoint'] = 14
            self.downloadData()

    def buttonPushed15(self):
        if self.confirmFlag == 'confirm':
            print 'Box is ',self.data['fireBox'],', Head is ',15
            self.data['firePoint'] = 15
            self.downloadData()

    def buttonPushed16(self):
        if self.confirmFlag == 'confirm':
            print 'Box is ',self.data['fireBox'],', Head is ',16
            self.data['firePoint'] = 16
            self.downloadData()

    def downloadData(self):
        dataPackage = dataPack(self.data)
        print repr(dataPackage.package)
        self.q.put (dataPackage.package)

    def boxChanged(self):
        self.confirmFlag = None
        self.ui.boxA1Button.setEnabled(False)
        self.ui.boxA2Button.setEnabled(False)
        self.ui.boxA3Button.setEnabled(False)
        self.ui.boxA4Button.setEnabled(False)
        self.ui.boxA5Button.setEnabled(False)
        self.ui.boxA6Button.setEnabled(False)
        self.ui.boxA7Button.setEnabled(False)
        self.ui.boxA8Button.setEnabled(False)
        self.ui.boxA9Button.setEnabled(False)
        self.ui.boxA10Button.setEnabled(False)
        self.ui.boxA11Button.setEnabled(False)
        self.ui.boxA12Button.setEnabled(False)
        self.ui.boxA13Button.setEnabled(False)
        self.ui.boxA14Button.setEnabled(False)
        self.ui.boxA15Button.setEnabled(False)
        self.ui.boxA16Button.setEnabled(False)

def main():
    app = QtGui.QApplication(sys.argv)
    window = UiShow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
