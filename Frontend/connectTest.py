from PySide import QtCore, QtGui
from UI.ui_connectTest import Ui_Dialog
import sys
from Device.protocol import dataPack

CONNECT_TEST = 0x01
FIRE = 0x02


class UiShow(QtGui.QDialog):

    def __init__(self ,signalClose ,queueGet,queuePut,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.signalClose = signalClose
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.buttonConnect()

        self.data = {'head':0xAAF0,'length':0x0E,'function':0x03,
                     'ID':0xAABBCCDD,'fireBox':None,'firePoint':None,
                     'crc':0,'tail':0xDD}

        self.q = queueGet
        self.p = queuePut

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timerEvent)
        self.timer.setInterval(1000)

        intVal = QtGui.QIntValidator()
        self.ui.pushButtonTest.setEnabled(False)
        self.ui.lineEditBoxID.setValidator(intVal)
        self.ui.lineEditBoxID.textChanged.connect(self.setStartEnable)

    def setStartEnable(self):
        if self.ui.lineEditBoxID.text()!='' and self.ui.lineEditBoxID.text()!='0':
            self.ui.pushButtonTest.setEnabled(True)
        else:
            self.ui.pushButtonTest.setEnabled(False)
            
    def closeEvent(self, event):
        self.signalClose.emit()
        self.timer.stop()
        event.accept()
        
    def timerEvent(self):
        print "get message...."
        if self.p.empty():
            return
        headList = self.p.get()

        for i in range(16):
            if headList[i]:
                self.setButton(i+1)

    def setButton(self,head):
        print "head = ", head

        if head == 1:
            self.ui.radioButton_1.setChecked(True)
        elif head == 2:
            self.ui.radioButton_2.setChecked(True)
        elif head == 3:
            self.ui.radioButton_3.setChecked(True)
        elif head == 4:
            self.ui.radioButton_4.setChecked(True)
        elif head == 5:
            self.ui.radioButton_5.setChecked(True)
        elif head == 6:
            self.ui.radioButton_6.setChecked(True)
        elif head == 7:
            self.ui.radioButton_7.setChecked(True)
        elif head == 8:
            self.ui.radioButton_8.setChecked(True)
        elif head == 9:
            self.ui.radioButton_9.setChecked(True)
        elif head == 10:
            self.ui.radioButton_10.setChecked(True)
        elif head == 11:
            self.ui.radioButton_11.setChecked(True)
        elif head == 12:
            self.ui.radioButton_12.setChecked(True)
        elif head == 13:
            self.ui.radioButton_13.setChecked(True)
        elif head == 14:
            self.ui.radioButton_14.setChecked(True)
        elif head == 15:
            self.ui.radioButton_15.setChecked(True)
        elif head == 16:
            self.ui.radioButton_16.setChecked(True)

    def buttonConnect(self):
        self.ui.pushButtonTest.clicked.connect(self.buttonTest)
        self.ui.pushButtonReset.clicked.connect(self.buttonReset)

    def buttonTest(self):
        if self.ui.lineEditBoxID.text() == '':
            return
        self.buttonReset()
        self.timer.start()
        self.data['fireBox'] = int(self.ui.lineEditBoxID.text())
        self.data['firePoint'] = 0
        dataPackage = dataPack(self.data)
        print repr(dataPackage.package)
        self.q.put((CONNECT_TEST,dataPackage.package))

    def buttonReset(self):
        self.ui.radioButton_1.setChecked(False)
        self.ui.radioButton_2.setChecked(False)
        self.ui.radioButton_3.setChecked(False)
        self.ui.radioButton_4.setChecked(False)
        self.ui.radioButton_5.setChecked(False)
        self.ui.radioButton_6.setChecked(False)
        self.ui.radioButton_7.setChecked(False)
        self.ui.radioButton_8.setChecked(False)
        self.ui.radioButton_9.setChecked(False)
        self.ui.radioButton_10.setChecked(False)
        self.ui.radioButton_11.setChecked(False)
        self.ui.radioButton_12.setChecked(False)
        self.ui.radioButton_13.setChecked(False)
        self.ui.radioButton_14.setChecked(False)
        self.ui.radioButton_15.setChecked(False)
        self.ui.radioButton_16.setChecked(False)
        self.timer.stop()

def main():
    app = QtGui.QApplication(sys.argv)
    window = UiShow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
