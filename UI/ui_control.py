# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'control.ui'
#
# Created: Fri Oct 18 14:45:19 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class ControlDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(215, 70)
        Dialog.setMinimumSize(QtCore.QSize(215, 70))
        Dialog.setMaximumSize(QtCore.QSize(215, 70))
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowSystemMenuHint)
        self.pushButtonStopFire = QtGui.QPushButton(Dialog)
        self.pushButtonStopFire.setGeometry(QtCore.QRect(130, 20, 30, 30))
        self.pushButtonStopFire.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButtonStopFire.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonStopFire.setIcon(icon)
        self.pushButtonStopFire.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonStopFire.setObjectName("pushButtonStopFire")
        self.pushButtonStartOrPause = QtGui.QPushButton(Dialog)
        self.pushButtonStartOrPause.setGeometry(QtCore.QRect(60, 20, 30, 30))
        self.pushButtonStartOrPause.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButtonStartOrPause.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Images/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonStartOrPause.setIcon(icon1)
        self.pushButtonStartOrPause.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonStartOrPause.setObjectName("pushButtonStartOrPause")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

from Resource import images_rc
