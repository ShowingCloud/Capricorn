# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Mon Oct 14 08:13:21 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(260, 110)
        Dialog.setMinimumSize(QtCore.QSize(260, 110))
        Dialog.setMaximumSize(QtCore.QSize(260, 110))
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.labelDelayTime = QtGui.QLabel(Dialog)
        self.labelDelayTime.setGeometry(QtCore.QRect(10, 20, 80, 25))
        self.labelDelayTime.setMinimumSize(QtCore.QSize(80, 25))
        self.labelDelayTime.setMaximumSize(QtCore.QSize(16777215, 25))
        self.labelDelayTime.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.labelDelayTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDelayTime.setObjectName("labelDelayTime")
        self.lineEditDelayTime = QtGui.QLineEdit(Dialog)
        self.lineEditDelayTime.setGeometry(QtCore.QRect(100, 20, 121, 25))
        self.lineEditDelayTime.setMinimumSize(QtCore.QSize(25, 25))
        self.lineEditDelayTime.setObjectName("lineEditDelayTime")
        self.label_s = QtGui.QLabel(Dialog)
        self.label_s.setGeometry(QtCore.QRect(230, 20, 10, 25))
        self.label_s.setMinimumSize(QtCore.QSize(10, 25))
        self.label_s.setMaximumSize(QtCore.QSize(10, 25))
        self.label_s.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_s.setObjectName("label_s")
        self.pushButtonCancel = QtGui.QPushButton(Dialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(170, 70, 50, 25))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.pushButtonStart = QtGui.QPushButton(Dialog)
        self.pushButtonStart.setGeometry(QtCore.QRect(110, 70, 50, 25))
        self.pushButtonStart.setObjectName("pushButtonStart")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "延时燃放", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDelayTime.setText(QtGui.QApplication.translate("Dialog", "输入延时时间:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_s.setText(QtGui.QApplication.translate("Dialog", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancel.setText(QtGui.QApplication.translate("Dialog", "取消", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonStart.setText(QtGui.QApplication.translate("Dialog", "开始", None, QtGui.QApplication.UnicodeUTF8))

