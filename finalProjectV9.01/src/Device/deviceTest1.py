# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'fireTest.ui'
#
# Created: Fri Mar 01 10:46:59 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!
import ftdi2 as ft
import Queue
from PySide import QtCore, QtGui
import protocol


try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
    
class getMessage(QtCore.QObject):
    signalRead = QtCore.Signal()
    def __init__(self, q, parent = None):
        QtCore.QObject.__init__(self, parent)
        self.signalRead.connect(self.readFun)
        self.q = q
    
    def readFun(self):
        dev = ft.list_devices()
        print dev[0]
        self.f = ft.open_ex(dev[0])
        
        while True:
            item = self.q.get()
            self.f.write(item)
            while not self.f.get_queue_status():
                pass
                print 'No data to read'
            dataRead = self.f.read(self.f.get_queue_status())
            print repr(item),'\n',repr(dataRead)
##            if dataRead != item:
##                for i in range(3):
##                    print i
##                    self.f.write(item)
##                    while not self.f.get_queue_status():
##                        pass
##                    dataRead = self.f.read(self.f.get_queue_status())
##                    if dataRead != item:
##                        continue
##                    else:
##                        break
##                if dataRead!=item:
##                    print 'connect error'
                    
            


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.q = Queue.Queue()
        self.c = getMessage(self.q)
        thread = QtCore.QThread()
        self.c.moveToThread(thread)
        thread.start()
        self.c.signalRead.emit()
        
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(761, 392)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox1 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox1.setGeometry(QtCore.QRect(40, 30, 331, 251))
        self.groupBox1.setObjectName(_fromUtf8("groupBox1"))
        self.boxA1Button = QtGui.QPushButton(self.groupBox1)
        self.boxA1Button.setGeometry(QtCore.QRect(10, 40, 31, 31))
        self.boxA1Button.setCheckable(True)
        
        self.boxA1Button.setObjectName(_fromUtf8("boxA1Button"))
        self.boxA2Button = QtGui.QPushButton(self.groupBox1)
        self.boxA2Button.setGeometry(QtCore.QRect(90, 40, 31, 31))
        self.boxA2Button.setCheckable(True)
        
        self.boxA2Button.setObjectName(_fromUtf8("boxA2Button"))
        self.boxA3Button = QtGui.QPushButton(self.groupBox1)
        self.boxA3Button.setGeometry(QtCore.QRect(170, 40, 31, 31))
        self.boxA3Button.setCheckable(True)
        
        self.boxA3Button.setObjectName(_fromUtf8("boxA3Button"))
        self.boxA4Button = QtGui.QPushButton(self.groupBox1)
        self.boxA4Button.setGeometry(QtCore.QRect(250, 40, 31, 31))
        self.boxA4Button.setCheckable(True)
        
        self.boxA4Button.setObjectName(_fromUtf8("boxA4Button"))
        self.boxA8Button = QtGui.QPushButton(self.groupBox1)
        self.boxA8Button.setGeometry(QtCore.QRect(250, 90, 31, 31))
        self.boxA8Button.setCheckable(True)
        self.boxA8Button.setChecked(False)
        self.boxA8Button.setObjectName(_fromUtf8("boxA8Button"))
        self.boxA7Button = QtGui.QPushButton(self.groupBox1)
        self.boxA7Button.setGeometry(QtCore.QRect(170, 90, 31, 31))
        self.boxA7Button.setCheckable(True)
        self.boxA7Button.setObjectName(_fromUtf8("boxA7Button"))
        self.boxA6Button = QtGui.QPushButton(self.groupBox1)
        self.boxA6Button.setGeometry(QtCore.QRect(90, 90, 31, 31))
        self.boxA6Button.setCheckable(True)
        self.boxA6Button.setObjectName(_fromUtf8("BoxA6Button"))
        self.boxA5Button = QtGui.QPushButton(self.groupBox1)
        self.boxA5Button.setGeometry(QtCore.QRect(10, 90, 31, 31))
        self.boxA5Button.setCheckable(True)
        self.boxA5Button.setObjectName(_fromUtf8("boxA5Button"))
        self.boxA9Button = QtGui.QPushButton(self.groupBox1)
        self.boxA9Button.setGeometry(QtCore.QRect(10, 140, 31, 31))
        self.boxA9Button.setCheckable(True)
        self.boxA9Button.setObjectName(_fromUtf8("boxA9Button"))
        self.boxA10Button = QtGui.QPushButton(self.groupBox1)
        self.boxA10Button.setGeometry(QtCore.QRect(90, 140, 31, 31))
        self.boxA10Button.setCheckable(True)
        self.boxA10Button.setObjectName(_fromUtf8("boxA10Button"))
        self.boxA11Button = QtGui.QPushButton(self.groupBox1)
        self.boxA11Button.setGeometry(QtCore.QRect(170, 140, 31, 31))
        self.boxA11Button.setCheckable(True)
        self.boxA11Button.setObjectName(_fromUtf8("boxA11Button"))
        self.boxA12Button = QtGui.QPushButton(self.groupBox1)
        self.boxA12Button.setGeometry(QtCore.QRect(250, 140, 31, 31))
        self.boxA12Button.setCheckable(True)
        self.boxA12Button.setObjectName(_fromUtf8("boxA12Button"))
        self.boxA13Button = QtGui.QPushButton(self.groupBox1)
        self.boxA13Button.setGeometry(QtCore.QRect(10, 190, 31, 31))
        self.boxA13Button.setCheckable(True)
        self.boxA13Button.setObjectName(_fromUtf8("boxA13Button"))
        self.boxA14Button = QtGui.QPushButton(self.groupBox1)
        self.boxA14Button.setGeometry(QtCore.QRect(90, 190, 31, 31))
        self.boxA14Button.setCheckable(True)
        self.boxA14Button.setObjectName(_fromUtf8("boxA14Button"))
        self.boxA15Button = QtGui.QPushButton(self.groupBox1)
        self.boxA15Button.setGeometry(QtCore.QRect(170, 190, 31, 31))
        self.boxA15Button.setCheckable(True)
        self.boxA15Button.setObjectName(_fromUtf8("boxA15Button"))
        self.boxA16Button = QtGui.QPushButton(self.groupBox1)
        self.boxA16Button.setGeometry(QtCore.QRect(250, 190, 31, 31))
        self.boxA16Button.setCheckable(True)
        self.boxA16Button.setObjectName(_fromUtf8("boxA16Button"))
        self.spinBoxA1 = QtGui.QSpinBox(self.groupBox1)
        
        self.spinBoxA1.setGeometry(QtCore.QRect(40, 40, 41, 31))
        self.spinBoxA1.setMaximum(60)
        self.spinBoxA1.setObjectName(_fromUtf8("spinBoxA1"))
        self.spinBoxA5 = QtGui.QSpinBox(self.groupBox1)
        self.spinBoxA5.setGeometry(QtCore.QRect(40, 90, 41, 31))
        self.spinBoxA5.setMaximum(60)
        self.spinBoxA5.setObjectName(_fromUtf8("spinBoxA5"))
        self.spinBoxA9 = QtGui.QSpinBox(self.groupBox1)
        self.spinBoxA9.setGeometry(QtCore.QRect(40, 140, 41, 31))
        self.spinBoxA9.setMaximum(60)
        self.spinBoxA9.setObjectName(_fromUtf8("spinBoxA9"))
        self.spinBoxA13 = QtGui.QSpinBox(self.groupBox1)
        self.spinBoxA13.setGeometry(QtCore.QRect(40, 190, 41, 31))
        self.spinBoxA13.setMaximum(60)
        self.spinBoxA13.setObjectName(_fromUtf8("spinBoxA13"))
        self.spinBoxA14 = QtGui.QSpinBox(self.groupBox1)
        self.spinBoxA14.setGeometry(QtCore.QRect(120, 190, 41, 31))
        self.spinBoxA14.setMaximum(60)
        self.spinBoxA14.setObjectName(_fromUtf8("spinBoxA14"))
        self.spinBoxA10 = QtGui.QSpinBox(self.groupBox1)
        self.spinBoxA10.setGeometry(QtCore.QRect(120, 140, 41, 31))
        self.spinBoxA10.setMaximum(60)
        self.spinBoxA10.setObjectName(_fromUtf8("spinBoxA10"))
        self.spinBoxA6 = QtGui.QSpinBox(self.groupBox1)
        self.spinBoxA6.setGeometry(QtCore.QRect(120, 90, 41, 31))
        self.spinBoxA6.setMaximum(60)
        self.spinBoxA6.setObjectName(_fromUtf8("spinBoxA6"))
        self.spinBoxA2 = QtGui.QSpinBox(self.groupBox1)
        self.spinBoxA2.setGeometry(QtCore.QRect(120, 40, 41, 31))
        self.spinBoxA2.setMaximum(60)
        self.spinBoxA2.setObjectName(_fromUtf8("spinBoxA2"))
        self.spinBoxA3 = QtGui.QSpinBox(self.groupBox1)
        self.spinBoxA3.setGeometry(QtCore.QRect(200, 40, 41, 31))
        self.spinBoxA3.setMaximum(60)
        self.spinBoxA3.setObjectName(_fromUtf8("spinBoxA3"))
        self.spinBoxA7 = QtGui.QSpinBox(self.groupBox1)
        self.spinBoxA7.setGeometry(QtCore.QRect(200, 90, 41, 31))
        self.spinBoxA7.setMaximum(60)
        self.spinBoxA7.setObjectName(_fromUtf8("spinBoxA7"))
        self.spinBoxA11 = QtGui.QSpinBox(self.groupBox1)
        self.spinBoxA11.setGeometry(QtCore.QRect(200, 140, 41, 31))
        self.spinBoxA11.setMaximum(60)
        self.spinBoxA11.setObjectName(_fromUtf8("spinBoxA11"))
        self.spinBoxA15 = QtGui.QSpinBox(self.groupBox1)
        self.spinBoxA15.setGeometry(QtCore.QRect(200, 190, 41, 31))
        self.spinBoxA15.setMaximum(60)
        self.spinBoxA15.setObjectName(_fromUtf8("spinBoxA15"))
        self.spinBoxA16 = QtGui.QSpinBox(self.groupBox1)
        self.spinBoxA16.setGeometry(QtCore.QRect(280, 190, 41, 31))
        self.spinBoxA16.setMaximum(60)
        self.spinBoxA16.setObjectName(_fromUtf8("spinBoxA16"))
        self.spinBoxA12 = QtGui.QSpinBox(self.groupBox1)
        self.spinBoxA12.setGeometry(QtCore.QRect(280, 140, 41, 31))
        self.spinBoxA12.setMaximum(60)
        self.spinBoxA12.setObjectName(_fromUtf8("spinBoxA12"))
        self.spinBoxA8 = QtGui.QSpinBox(self.groupBox1)
        self.spinBoxA8.setGeometry(QtCore.QRect(280, 90, 41, 31))
        self.spinBoxA8.setMaximum(60)
        self.spinBoxA8.setObjectName(_fromUtf8("spinBoxA8"))
        self.spinBoxA4 = QtGui.QSpinBox(self.groupBox1)
        self.spinBoxA4.setGeometry(QtCore.QRect(280, 40, 41, 31))
        self.spinBoxA4.setMaximum(60)
        self.spinBoxA4.setObjectName(_fromUtf8("spinBoxA4"))
        self.groupBox2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox2.setGeometry(QtCore.QRect(390, 30, 341, 251))
        self.groupBox2.setObjectName(_fromUtf8("groupBox2"))
        self.boxB1Button = QtGui.QPushButton(self.groupBox2)
        self.boxB1Button.setGeometry(QtCore.QRect(20, 40, 31, 31))
        self.boxB1Button.setCheckable(True)
        self.boxB1Button.setObjectName(_fromUtf8("boxB1Button"))
        self.boxB2Button = QtGui.QPushButton(self.groupBox2)
        self.boxB2Button.setGeometry(QtCore.QRect(100, 40, 31, 31))
        self.boxB2Button.setCheckable(True)
        self.boxB2Button.setObjectName(_fromUtf8("boxB2Button"))
        self.boxB3Button = QtGui.QPushButton(self.groupBox2)
        self.boxB3Button.setGeometry(QtCore.QRect(180, 40, 31, 31))
        self.boxB3Button.setCheckable(True)
        self.boxB3Button.setObjectName(_fromUtf8("boxB3Button"))
        self.boxB4Button = QtGui.QPushButton(self.groupBox2)
        self.boxB4Button.setGeometry(QtCore.QRect(260, 40, 31, 31))
        self.boxB4Button.setCheckable(True)
        self.boxB4Button.setObjectName(_fromUtf8("boxB4Button"))
        self.boxB5Button = QtGui.QPushButton(self.groupBox2)
        self.boxB5Button.setGeometry(QtCore.QRect(20, 90, 31, 31))
        self.boxB5Button.setCheckable(True)
        self.boxB5Button.setObjectName(_fromUtf8("boxB5Button"))
        self.boxB6Button = QtGui.QPushButton(self.groupBox2)
        self.boxB6Button.setGeometry(QtCore.QRect(100, 90, 31, 31))
        self.boxB6Button.setCheckable(True)
        self.boxB6Button.setObjectName(_fromUtf8("boxB6Button"))
        self.boxB7Button = QtGui.QPushButton(self.groupBox2)
        self.boxB7Button.setGeometry(QtCore.QRect(180, 90, 31, 31))
        self.boxB7Button.setCheckable(True)
        self.boxB7Button.setObjectName(_fromUtf8("boxB7Button"))
        self.boxB8Button = QtGui.QPushButton(self.groupBox2)
        self.boxB8Button.setGeometry(QtCore.QRect(260, 90, 31, 31))
        self.boxB8Button.setCheckable(True)
        self.boxB8Button.setObjectName(_fromUtf8("boxB8Button"))
        self.boxB9Button = QtGui.QPushButton(self.groupBox2)
        self.boxB9Button.setGeometry(QtCore.QRect(20, 140, 31, 31))
        self.boxB9Button.setCheckable(True)
        self.boxB9Button.setObjectName(_fromUtf8("boxB9Button"))
        self.boxB10Button = QtGui.QPushButton(self.groupBox2)
        self.boxB10Button.setGeometry(QtCore.QRect(100, 140, 31, 31))
        self.boxB10Button.setCheckable(True)
        self.boxB10Button.setObjectName(_fromUtf8("boxB10Button"))
        self.boxB11Button = QtGui.QPushButton(self.groupBox2)
        self.boxB11Button.setGeometry(QtCore.QRect(180, 140, 31, 31))
        self.boxB11Button.setCheckable(True)
        self.boxB11Button.setObjectName(_fromUtf8("boxB11Button"))
        self.boxB12Button = QtGui.QPushButton(self.groupBox2)
        self.boxB12Button.setGeometry(QtCore.QRect(260, 140, 31, 31))
        self.boxB12Button.setCheckable(True)
        self.boxB12Button.setObjectName(_fromUtf8("boxB12Button"))
        self.boxB13Button = QtGui.QPushButton(self.groupBox2)
        self.boxB13Button.setGeometry(QtCore.QRect(20, 190, 31, 31))
        self.boxB13Button.setCheckable(True)
        self.boxB13Button.setObjectName(_fromUtf8("boxB13Button"))
        self.boxB14Button = QtGui.QPushButton(self.groupBox2)
        self.boxB14Button.setGeometry(QtCore.QRect(100, 190, 31, 31))
        self.boxB14Button.setCheckable(True)
        self.boxB14Button.setObjectName(_fromUtf8("boxB14Button"))
        self.boxB15Button = QtGui.QPushButton(self.groupBox2)
        self.boxB15Button.setGeometry(QtCore.QRect(180, 190, 31, 31))
        self.boxB15Button.setCheckable(True)
        self.boxB15Button.setObjectName(_fromUtf8("boxB15Button"))
        self.boxB16Button = QtGui.QPushButton(self.groupBox2)
        self.boxB16Button.setGeometry(QtCore.QRect(260, 190, 31, 31))
        self.boxB16Button.setCheckable(True)
        self.boxB16Button.setObjectName(_fromUtf8("boxB16Button"))
        self.spinBoxB1 = QtGui.QSpinBox(self.groupBox2)
        self.spinBoxB1.setGeometry(QtCore.QRect(50, 40, 41, 31))
        self.spinBoxB1.setMaximum(60)
        self.spinBoxB1.setObjectName(_fromUtf8("spinBoxB1"))
        self.spinBoxB5 = QtGui.QSpinBox(self.groupBox2)
        self.spinBoxB5.setGeometry(QtCore.QRect(50, 90, 41, 31))
        self.spinBoxB5.setMaximum(60)
        self.spinBoxB5.setObjectName(_fromUtf8("spinBoxB5"))
        self.spinBoxB9 = QtGui.QSpinBox(self.groupBox2)
        self.spinBoxB9.setGeometry(QtCore.QRect(50, 140, 41, 31))
        self.spinBoxB9.setMaximum(60)
        self.spinBoxB9.setObjectName(_fromUtf8("spinBoxB9"))
        self.spinBoxB13 = QtGui.QSpinBox(self.groupBox2)
        self.spinBoxB13.setGeometry(QtCore.QRect(50, 190, 41, 31))
        self.spinBoxB13.setMaximum(60)
        self.spinBoxB13.setObjectName(_fromUtf8("spinBoxB13"))
        self.spinBoxB2 = QtGui.QSpinBox(self.groupBox2)
        self.spinBoxB2.setGeometry(QtCore.QRect(130, 40, 41, 31))
        self.spinBoxB2.setMaximum(60)
        self.spinBoxB2.setObjectName(_fromUtf8("spinBoxB2"))
        self.spinBoxB6 = QtGui.QSpinBox(self.groupBox2)
        self.spinBoxB6.setGeometry(QtCore.QRect(130, 90, 41, 31))
        self.spinBoxB6.setMaximum(60)
        self.spinBoxB6.setObjectName(_fromUtf8("spinBoxB6"))
        self.spinBoxB10 = QtGui.QSpinBox(self.groupBox2)
        self.spinBoxB10.setGeometry(QtCore.QRect(130, 140, 41, 31))
        self.spinBoxB10.setMaximum(60)
        self.spinBoxB10.setObjectName(_fromUtf8("spinBoxB10"))
        self.spinBoxB14 = QtGui.QSpinBox(self.groupBox2)
        self.spinBoxB14.setGeometry(QtCore.QRect(130, 190, 41, 31))
        self.spinBoxB14.setMaximum(60)
        self.spinBoxB14.setObjectName(_fromUtf8("spinBoxB14"))
        self.spinBoxB3 = QtGui.QSpinBox(self.groupBox2)
        self.spinBoxB3.setGeometry(QtCore.QRect(210, 40, 41, 31))
        self.spinBoxB3.setMaximum(60)
        self.spinBoxB3.setObjectName(_fromUtf8("spinBoxB3"))
        self.spinBoxB7 = QtGui.QSpinBox(self.groupBox2)
        self.spinBoxB7.setGeometry(QtCore.QRect(210, 90, 41, 31))
        self.spinBoxB7.setMaximum(60)
        self.spinBoxB7.setObjectName(_fromUtf8("spinBoxB7"))
        self.spinBoxB11 = QtGui.QSpinBox(self.groupBox2)
        self.spinBoxB11.setGeometry(QtCore.QRect(210, 140, 41, 31))
        self.spinBoxB11.setMaximum(60)
        self.spinBoxB11.setObjectName(_fromUtf8("spinBoxB11"))
        self.spinBoxB15 = QtGui.QSpinBox(self.groupBox2)
        self.spinBoxB15.setGeometry(QtCore.QRect(210, 190, 41, 31))
        self.spinBoxB15.setMaximum(60)
        self.spinBoxB15.setObjectName(_fromUtf8("spinBoxB15"))
        self.spinBoxB4 = QtGui.QSpinBox(self.groupBox2)
        self.spinBoxB4.setGeometry(QtCore.QRect(290, 40, 41, 31))
        self.spinBoxB4.setMaximum(60)
        self.spinBoxB4.setObjectName(_fromUtf8("spinBoxB4"))
        self.spinBoxB8 = QtGui.QSpinBox(self.groupBox2)
        self.spinBoxB8.setGeometry(QtCore.QRect(290, 90, 41, 31))
        self.spinBoxB8.setMaximum(60)
        self.spinBoxB8.setObjectName(_fromUtf8("spinBoxB8"))
        self.spinBoxB12 = QtGui.QSpinBox(self.groupBox2)
        self.spinBoxB12.setGeometry(QtCore.QRect(290, 140, 41, 31))
        self.spinBoxB12.setMaximum(60)
        self.spinBoxB12.setObjectName(_fromUtf8("spinBoxB12"))
        self.spinBoxB16 = QtGui.QSpinBox(self.groupBox2)
        self.spinBoxB16.setGeometry(QtCore.QRect(290, 190, 41, 31))
        self.spinBoxB16.setMaximum(60)
        self.spinBoxB16.setObjectName(_fromUtf8("spinBoxB16"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(250, 310, 71, 31))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.pauseButton = QtGui.QPushButton(self.centralwidget)
        self.pauseButton.setGeometry(QtCore.QRect(370, 310, 71, 31))
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.continueButton = QtGui.QPushButton(self.centralwidget)
        self.continueButton.setGeometry(QtCore.QRect(500, 310, 71, 31))
        self.continueButton.setObjectName(_fromUtf8("continueButton"))
        self.radioButtonNow = QtGui.QRadioButton(self.centralwidget)
        self.radioButtonNow.setGeometry(QtCore.QRect(150, 310, 81, 31))
        self.radioButtonNow.setObjectName(_fromUtf8("radioButtonNow"))
        self.radioButtonDelay = QtGui.QRadioButton(self.centralwidget)
        self.radioButtonDelay.setGeometry(QtCore.QRect(40, 310, 91, 31))
        self.radioButtonDelay.setChecked(True)
        self.radioButtonDelay.setObjectName(_fromUtf8("radioButtonDelay"))
        self.stopButton = QtGui.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(630, 310, 71, 31))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 761, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        self.radioButtonNow.clicked.connect(self.fireNowMode)
        self.radioButtonDelay.clicked.connect(self.fireDelayMode)
        self.startButton.clicked.connect(self.start_fun)
        self.pauseButton.clicked.connect(self.pause_fun)
        self.continueButton.clicked.connect(self.continue_fun)
        self.stopButton.clicked.connect(self.stop_fun)
        

        
    def checkButton(self):
        self.buttonList = [None]*2
        self.buttonList[0] = [None]*16
        self.buttonList[1] = [None]*16
        if self.radioButtonDelay.isChecked():
            self.timeList = [None]*2
            self.timeList[0] = [None]*16
            self.timeList[1] = [None]*16
            if self.boxA1Button.isChecked():
                self.buttonList[0][0] = 1
                self.timeList[0][0] = int(self.spinBoxA1.text())
            if self.boxA2Button.isChecked():
                self.buttonList[0][1] = 1
                self.timeList[0][1] = int(self.spinBoxA2.text())
            if self.boxA3Button.isChecked():
                self.buttonList[0][2] = 1
                self.timeList[0][2] = int(self.spinBoxA3.text())
            if self.boxA4Button.isChecked():
                self.buttonList[0][3] = 1
                self.timeList[0][3] = int(self.spinBoxA4.text())
            if self.boxA5Button.isChecked():
                self.buttonList[0][4] = 1
                self.timeList[0][4] = int(self.spinBoxA5.text())
            if self.boxA6Button.isChecked():
                self.buttonList[0][5] = 1
                self.timeList[0][5] = int(self.spinBoxA6.text())
            if self.boxA7Button.isChecked():
                self.buttonList[0][6] = 1
                self.timeList[0][6] = int(self.spinBoxA7.text())
            if self.boxA8Button.isChecked():
                self.buttonList[0][7] = 1
                self.timeList[0][7] = int(self.spinBoxA8.text())
            if self.boxA9Button.isChecked():
                self.buttonList[0][8] = 1
                self.timeList[0][8] = int(self.spinBoxA9.text())
            if self.boxA10Button.isChecked():
                self.buttonList[0][9] = 1
                self.timeList[0][9] = int(self.spinBoxA10.text())
            if self.boxA11Button.isChecked():
                self.buttonList[0][10] = 1
                self.timeList[0][10] = int(self.spinBoxA11.text())
            if self.boxA12Button.isChecked():
                self.buttonList[0][11] = 1
                self.timeList[0][11] = int(self.spinBoxA12.text())
            if self.boxA13Button.isChecked():
                self.buttonList[0][12] = 1
                self.timeList[0][12] = int(self.spinBoxA13.text())
            if self.boxA14Button.isChecked():
                self.buttonList[0][13] = 1
                self.timeList[0][13] = int(self.spinBoxA14.text())
            if self.boxA15Button.isChecked():
                self.buttonList[0][14] = 1
                self.timeList[0][14] = int(self.spinBoxA15.text())
            if self.boxA16Button.isChecked():
                self.buttonList[0][15] = 1
                self.timeList[0][15] = int(self.spinBoxA16.text())
            if self.boxB1Button.isChecked():
                self.buttonList[1][0] = 1
                self.timeList[1][0] = int(self.spinBoxB1.text())
            if self.boxB2Button.isChecked():
                self.buttonList[1][1] = 1
                self.timeList[1][1] = int(self.spinBoxB2.text())
            if self.boxB3Button.isChecked():
                self.buttonList[1][2] = 1
                self.timeList[1][2] = int(self.spinBoxB3.text())
            if self.boxB4Button.isChecked():
                self.buttonList[1][3] = 1
                self.timeList[1][3] = int(self.spinBoxB4.text())
            if self.boxB5Button.isChecked():
                self.buttonList[1][4] = 1
                self.timeList[1][4] = int(self.spinBoxB5.text())
            if self.boxB6Button.isChecked():
                self.buttonList[1][5] = 1
                self.timeList[1][5] = int(self.spinBoxB6.text())
            if self.boxB7Button.isChecked():
                self.buttonList[1][6] = 1
                self.timeList[1][6] = int(self.spinBoxB7.text())
            if self.boxB8Button.isChecked():
                self.buttonList[1][7] = 1
                self.timeList[1][7] = int(self.spinBoxB8.text())
            if self.boxB9Button.isChecked():
                self.buttonList[1][8] = 1
                self.timeList[1][8] = int(self.spinBoxB9.text())
            if self.boxB10Button.isChecked():
                self.buttonList[1][9] = 1
                self.timeList[1][9] = int(self.spinBoxB10.text())
            if self.boxB11Button.isChecked():
                self.buttonList[1][10] = 1
                self.timeList[1][10] = int(self.spinBoxB11.text())
            if self.boxB12Button.isChecked():
                self.buttonList[1][11] = 1
                self.timeList[1][11] = int(self.spinBoxB12.text())
            if self.boxB13Button.isChecked():
                self.buttonList[1][12] = 1
                self.timeList[1][12] = int(self.spinBoxB13.text())
            if self.boxB14Button.isChecked():
                self.buttonList[1][13] = 1
                self.timeList[1][13] = int(self.spinBoxB14.text())
            if self.boxB15Button.isChecked():
                self.buttonList[1][14] = 1
                self.timeList[1][14] = int(self.spinBoxB15.text())
            if self.boxB16Button.isChecked():
                self.buttonList[1][15] = 1
                self.timeList[1][15] = int(self.spinBoxB16.text())
        elif self.radioButtonNow.isChecked():
                
            if self.boxA1Button.isChecked():
                self.buttonList[0][0] = 1
            if self.boxA2Button.isChecked():
                self.buttonList[0][1] = 1
            if self.boxA3Button.isChecked():
                self.buttonList[0][2] = 1
            if self.boxA4Button.isChecked():
                self.buttonList[0][3] = 1
            if self.boxA5Button.isChecked():
                self.buttonList[0][4] = 1
            if self.boxA6Button.isChecked():
                self.buttonList[0][5] = 1
            if self.boxA7Button.isChecked():
                self.buttonList[0][6] = 1
            if self.boxA8Button.isChecked():
                self.buttonList[0][7] = 1
            if self.boxA9Button.isChecked():
                self.buttonList[0][8] = 1
            if self.boxA10Button.isChecked():
                self.buttonList[0][9] = 1
            if self.boxA11Button.isChecked():
                self.buttonList[0][10] = 1
            if self.boxA12Button.isChecked():
                self.buttonList[0][11] = 1
            if self.boxA13Button.isChecked():
                self.buttonList[0][12] = 1
            if self.boxA14Button.isChecked():
                self.buttonList[0][13] = 1
            if self.boxA15Button.isChecked():
                self.buttonList[0][14] = 1
            if self.boxA16Button.isChecked():
                self.buttonList[0][15] = 1
                
            if self.boxB1Button.isChecked():
                self.buttonList[1][0] = 1
            if self.boxB2Button.isChecked():
                self.buttonList[1][1] = 1
            if self.boxB3Button.isChecked():
                self.buttonList[1][2] = 1
            if self.boxB4Button.isChecked():
                self.buttonList[1][3] = 1
            if self.boxB5Button.isChecked():
                self.buttonList[1][4] = 1
            if self.boxB6Button.isChecked():
                self.buttonList[1][5] = 1
            if self.boxB7Button.isChecked():
                self.buttonList[1][6] = 1
            if self.boxB8Button.isChecked():
                self.buttonList[1][7] = 1
            if self.boxB9Button.isChecked():
                self.buttonList[1][8] = 1
            if self.boxB10Button.isChecked():
                self.buttonList[1][9] = 1
            if self.boxB11Button.isChecked():
                self.buttonList[1][10] = 1
            if self.boxB12Button.isChecked():
                self.buttonList[1][11] = 1
            if self.boxB13Button.isChecked():
                self.buttonList[1][12] = 1
            if self.boxB14Button.isChecked():
                self.buttonList[1][13] = 1
            if self.boxB15Button.isChecked():
                self.buttonList[1][14] = 1
            if self.boxB16Button.isChecked():
                self.buttonList[1][15] = 1

    
    def start_fun(self):
        reply = QtGui.QMessageBox.question(None,'message','Are you sure to fire?',
                                           QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            self.checkButton()

            if self.radioButtonDelay.isChecked():

                data = {'head':0xAAF0,'length':0x14,'function':0xF1,
                        'ID':0xAABBCCDD,'fireBox':None,'firePoint':None,
                        'seconds':None,'offsetSec':0,'crc':0,'tail':0xDD}
                for j in range(2):
                    for i in range(16):
                        if self.buttonList[j][i]:
                            print "Box%d firePoint %d ,time=%d s"%((j+1),(i+1),self.timeList[j][i])                       
                            data['fireBox'] = j+1
                            data['firePoint'] = i+1
                            data['seconds'] = self.timeList[j][i]
                            package = protocol.dataPack(data)
                            package.pack()
                            self.q.put (package.package)
                        
                    

                    
            elif self.radioButtonNow.isChecked():
                data = {'head':0xAAF0,'length':0x0E,'function':0x02,
                        'ID':0xAABBCCDD,'fireBox':None,'firePoint':None,
                        'seconds':None,'offsetSec':None,'crc':0,'tail':0xDD}
                for j in range(2):
                    for i in range(16):
                        if self.buttonList[j][i]:
                            print "Box%d firePoint %d"%((j+1),(i+1))
                        
                            data['fireBox'] = j+1
                            data['firePoint'] = i+1

                            package = protocol.dataPack(data)
                            package.pack()
                       
                            self.q.put(package.package)
                        
                  
                       
    def pause_fun(self):
        pass

    def continue_fun(self):
        pass

    def stop_fun(self):
        self.boxA1Button.setChecked(False)
        self.boxA2Button.setChecked(False)
        self.boxA3Button.setChecked(False)
        self.boxA4Button.setChecked(False)
        self.boxA5Button.setChecked(False)
        self.boxA6Button.setChecked(False)
        self.boxA7Button.setChecked(False)
        self.boxA8Button.setChecked(False)
        self.boxA9Button.setChecked(False)
        self.boxA10Button.setChecked(False)
        self.boxA11Button.setChecked(False)
        self.boxA12Button.setChecked(False)
        self.boxA13Button.setChecked(False)
        self.boxA14Button.setChecked(False)
        self.boxA15Button.setChecked(False)
        self.boxA16Button.setChecked(False)
        self.boxB1Button.setChecked(False)
        self.boxB2Button.setChecked(False)
        self.boxB3Button.setChecked(False)
        self.boxB4Button.setChecked(False)
        self.boxB5Button.setChecked(False)
        self.boxB6Button.setChecked(False)
        self.boxB7Button.setChecked(False)
        self.boxB8Button.setChecked(False)
        self.boxB9Button.setChecked(False)
        self.boxB10Button.setChecked(False)
        self.boxB11Button.setChecked(False)
        self.boxB12Button.setChecked(False)
        self.boxB13Button.setChecked(False)
        self.boxB14Button.setChecked(False)
        self.boxB15Button.setChecked(False)
        self.boxB16Button.setChecked(False)
        if self.radioButtonDelay.isChecked():
            self.spinBoxA1.setProperty("value", 0)
            self.spinBoxA2.setProperty("value", 0)
            self.spinBoxA3.setProperty("value", 0)
            self.spinBoxA4.setProperty("value", 0)
            self.spinBoxA5.setProperty("value", 0)
            self.spinBoxA6.setProperty("value", 0)
            self.spinBoxA7.setProperty("value", 0)
            self.spinBoxA8.setProperty("value", 0)
            self.spinBoxA9.setProperty("value", 0)
            self.spinBoxA10.setProperty("value", 0)
            self.spinBoxA11.setProperty("value", 0)
            self.spinBoxA12.setProperty("value", 0)
            self.spinBoxA13.setProperty("value", 0)
            self.spinBoxA14.setProperty("value", 0)
            self.spinBoxA15.setProperty("value", 0)
            self.spinBoxA16.setProperty("value", 0)
            self.spinBoxB1.setProperty("value", 0)
            self.spinBoxB2.setProperty("value", 0)
            self.spinBoxB3.setProperty("value", 0)
            self.spinBoxB4.setProperty("value", 0)
            self.spinBoxB5.setProperty("value", 0)
            self.spinBoxB6.setProperty("value", 0) 
            self.spinBoxB7.setProperty("value", 0)
            self.spinBoxB8.setProperty("value", 0)
            self.spinBoxB9.setProperty("value", 0)
            self.spinBoxB10.setProperty("value", 0)
            self.spinBoxB11.setProperty("value", 0)
            self.spinBoxB12.setProperty("value", 0)
            self.spinBoxB13.setProperty("value", 0)
            self.spinBoxB14.setProperty("value", 0)
            self.spinBoxB15.setProperty("value", 0)
            self.spinBoxB16.setProperty("value", 0)
    
    def fireNowMode(self):
        self.boxA1Button.setChecked(False)
        self.boxA2Button.setChecked(False)
        self.boxA3Button.setChecked(False)
        self.boxA4Button.setChecked(False)
        self.boxA5Button.setChecked(False)
        self.boxA6Button.setChecked(False)
        self.boxA7Button.setChecked(False)
        self.boxA8Button.setChecked(False)
        self.boxA9Button.setChecked(False)
        self.boxA10Button.setChecked(False)
        self.boxA11Button.setChecked(False)
        self.boxA12Button.setChecked(False)
        self.boxA13Button.setChecked(False)
        self.boxA14Button.setChecked(False)
        self.boxA15Button.setChecked(False)
        self.boxA16Button.setChecked(False)
        self.boxB1Button.setChecked(False)
        self.boxB2Button.setChecked(False)
        self.boxB3Button.setChecked(False)
        self.boxB4Button.setChecked(False)
        self.boxB5Button.setChecked(False)
        self.boxB6Button.setChecked(False)
        self.boxB7Button.setChecked(False)
        self.boxB8Button.setChecked(False)
        self.boxB9Button.setChecked(False)
        self.boxB10Button.setChecked(False)
        self.boxB11Button.setChecked(False)
        self.boxB12Button.setChecked(False)
        self.boxB13Button.setChecked(False)
        self.boxB14Button.setChecked(False)
        self.boxB15Button.setChecked(False)
        self.boxB16Button.setChecked(False)
        
        self.spinBoxA1.setProperty("value", 0)
        self.spinBoxA1.setEnabled(False)
        self.spinBoxA2.setProperty("value", 0)
        self.spinBoxA2.setEnabled(False)
        self.spinBoxA3.setProperty("value", 0)
        self.spinBoxA3.setEnabled(False)
        self.spinBoxA4.setProperty("value", 0)
        self.spinBoxA4.setEnabled(False)
        self.spinBoxA5.setProperty("value", 0)
        self.spinBoxA5.setEnabled(False)
        self.spinBoxA6.setProperty("value", 0)
        self.spinBoxA6.setEnabled(False)
        self.spinBoxA7.setProperty("value", 0)
        self.spinBoxA7.setEnabled(False)
        self.spinBoxA8.setProperty("value", 0)
        self.spinBoxA8.setEnabled(False)
        self.spinBoxA9.setProperty("value", 0)
        self.spinBoxA9.setEnabled(False)
        self.spinBoxA10.setProperty("value", 0)
        self.spinBoxA10.setEnabled(False)
        self.spinBoxA11.setProperty("value", 0)
        self.spinBoxA11.setEnabled(False)
        self.spinBoxA12.setProperty("value", 0)
        self.spinBoxA12.setEnabled(False)
        self.spinBoxA13.setProperty("value", 0)
        self.spinBoxA13.setEnabled(False)
        self.spinBoxA14.setProperty("value", 0)
        self.spinBoxA14.setEnabled(False)
        self.spinBoxA15.setProperty("value", 0)
        self.spinBoxA15.setEnabled(False)
        self.spinBoxA16.setProperty("value", 0)
        self.spinBoxA16.setEnabled(False)
        self.spinBoxB1.setProperty("value", 0)
        self.spinBoxB1.setEnabled(False)
        self.spinBoxB2.setProperty("value", 0)
        self.spinBoxB2.setEnabled(False)
        self.spinBoxB3.setProperty("value", 0)
        self.spinBoxB3.setEnabled(False)
        self.spinBoxB4.setProperty("value", 0)
        self.spinBoxB4.setEnabled(False)
        self.spinBoxB5.setProperty("value", 0)
        self.spinBoxB5.setEnabled(False)
        self.spinBoxB6.setProperty("value", 0) 
        self.spinBoxB6.setEnabled(False)
        self.spinBoxB7.setProperty("value", 0)
        self.spinBoxB7.setEnabled(False)
        self.spinBoxB8.setProperty("value", 0)
        self.spinBoxB8.setEnabled(False)
        self.spinBoxB9.setProperty("value", 0)
        self.spinBoxB9.setEnabled(False)
        self.spinBoxB10.setProperty("value", 0)
        self.spinBoxB10.setEnabled(False)
        self.spinBoxB11.setProperty("value", 0)
        self.spinBoxB11.setEnabled(False)
        self.spinBoxB12.setProperty("value", 0)
        self.spinBoxB12.setEnabled(False)
        self.spinBoxB13.setProperty("value", 0)
        self.spinBoxB13.setEnabled(False)
        self.spinBoxB14.setProperty("value", 0)
        self.spinBoxB14.setEnabled(False)
        self.spinBoxB15.setProperty("value", 0)
        self.spinBoxB15.setEnabled(False)
        self.spinBoxB16.setProperty("value", 0)
        self.spinBoxB16.setEnabled(False)

    def fireDelayMode(self):
        self.boxA1Button.setChecked(False)
        self.boxA2Button.setChecked(False)
        self.boxA3Button.setChecked(False)
        self.boxA4Button.setChecked(False)
        self.boxA5Button.setChecked(False)
        self.boxA6Button.setChecked(False)
        self.boxA7Button.setChecked(False)
        self.boxA8Button.setChecked(False)
        self.boxA9Button.setChecked(False)
        self.boxA10Button.setChecked(False)
        self.boxA11Button.setChecked(False)
        self.boxA12Button.setChecked(False)
        self.boxA13Button.setChecked(False)
        self.boxA14Button.setChecked(False)
        self.boxA15Button.setChecked(False)
        self.boxA16Button.setChecked(False)
        self.boxB1Button.setChecked(False)
        self.boxB2Button.setChecked(False)
        self.boxB3Button.setChecked(False)
        self.boxB4Button.setChecked(False)
        self.boxB5Button.setChecked(False)
        self.boxB6Button.setChecked(False)
        self.boxB7Button.setChecked(False)
        self.boxB8Button.setChecked(False)
        self.boxB9Button.setChecked(False)
        self.boxB10Button.setChecked(False)
        self.boxB11Button.setChecked(False)
        self.boxB12Button.setChecked(False)
        self.boxB13Button.setChecked(False)
        self.boxB14Button.setChecked(False)
        self.boxB15Button.setChecked(False)
        self.boxB16Button.setChecked(False)
        
        self.spinBoxA1.setEnabled(True)
        self.spinBoxA2.setEnabled(True)        
        self.spinBoxA3.setEnabled(True)
        self.spinBoxA4.setEnabled(True)
        self.spinBoxA5.setEnabled(True)
        self.spinBoxA6.setEnabled(True)
        self.spinBoxA7.setEnabled(True)
        self.spinBoxA8.setEnabled(True)
        self.spinBoxA9.setEnabled(True)
        self.spinBoxA10.setEnabled(True)
        self.spinBoxA11.setEnabled(True)
        self.spinBoxA12.setEnabled(True)
        self.spinBoxA13.setEnabled(True)
        self.spinBoxA14.setEnabled(True)
        self.spinBoxA15.setEnabled(True)
        self.spinBoxA16.setEnabled(True)
        self.spinBoxB1.setEnabled(True)
        self.spinBoxB2.setEnabled(True)
        self.spinBoxB3.setEnabled(True)
        self.spinBoxB4.setEnabled(True)
        self.spinBoxB5.setEnabled(True)
        self.spinBoxB6.setEnabled(True)
        self.spinBoxB7.setEnabled(True)
        self.spinBoxB8.setEnabled(True)
        self.spinBoxB9.setEnabled(True)
        self.spinBoxB10.setEnabled(True)
        self.spinBoxB11.setEnabled(True)
        self.spinBoxB12.setEnabled(True)
        self.spinBoxB13.setEnabled(True)
        self.spinBoxB14.setEnabled(True)
        self.spinBoxB15.setEnabled(True)
        self.spinBoxB16.setEnabled(True)
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox1.setTitle(_translate("MainWindow", "Box1", None))
        self.boxA1Button.setText(_translate("MainWindow", "1", None))
        self.boxA2Button.setText(_translate("MainWindow", "2", None))
        self.boxA3Button.setText(_translate("MainWindow", "3", None))
        self.boxA4Button.setText(_translate("MainWindow", "4", None))
        self.boxA8Button.setText(_translate("MainWindow", "8", None))
        self.boxA7Button.setText(_translate("MainWindow", "7", None))
        self.boxA6Button.setText(_translate("MainWindow", "6", None))
        self.boxA5Button.setText(_translate("MainWindow", "5", None))
        self.boxA9Button.setText(_translate("MainWindow", "9", None))
        self.boxA10Button.setText(_translate("MainWindow", "10", None))
        self.boxA11Button.setText(_translate("MainWindow", "11", None))
        self.boxA12Button.setText(_translate("MainWindow", "12", None))
        self.boxA13Button.setText(_translate("MainWindow", "13", None))
        self.boxA14Button.setText(_translate("MainWindow", "14", None))
        self.boxA15Button.setText(_translate("MainWindow", "15", None))
        self.boxA16Button.setText(_translate("MainWindow", "16", None))
        self.groupBox2.setTitle(_translate("MainWindow", "Box2", None))
        self.boxB1Button.setText(_translate("MainWindow", "1", None))
        self.boxB2Button.setText(_translate("MainWindow", "2", None))
        self.boxB3Button.setText(_translate("MainWindow", "3", None))
        self.boxB4Button.setText(_translate("MainWindow", "4", None))
        self.boxB5Button.setText(_translate("MainWindow", "5", None))
        self.boxB6Button.setText(_translate("MainWindow", "6", None))
        self.boxB7Button.setText(_translate("MainWindow", "7", None))
        self.boxB8Button.setText(_translate("MainWindow", "8", None))
        self.boxB9Button.setText(_translate("MainWindow", "9", None))
        self.boxB10Button.setText(_translate("MainWindow", "10", None))
        self.boxB11Button.setText(_translate("MainWindow", "11", None))
        self.boxB12Button.setText(_translate("MainWindow", "12", None))
        self.boxB13Button.setText(_translate("MainWindow", "13", None))
        self.boxB14Button.setText(_translate("MainWindow", "14", None))
        self.boxB15Button.setText(_translate("MainWindow", "15", None))
        self.boxB16Button.setText(_translate("MainWindow", "16", None))
        self.startButton.setText(_translate("MainWindow", "Start", None))
        self.pauseButton.setText(_translate("MainWindow", "Pause", None))
        self.continueButton.setText(_translate("MainWindow", "Continue", None))
        self.radioButtonNow.setText(_translate("MainWindow", "Fire directly", None))
        self.radioButtonDelay.setText(_translate("MainWindow", "Fire delayed", None))
        self.stopButton.setText(_translate("MainWindow", "Reset", None))

