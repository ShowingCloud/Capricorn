# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fireNow.ui'
#
# Created: Mon Apr 22 15:27:31 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(329, 323)
        Dialog.setMinimumSize(QtCore.QSize(329, 323))
        Dialog.setMaximumSize(QtCore.QSize(329, 323))
        self.ButtonConfirm = QtGui.QPushButton(Dialog)
        self.ButtonConfirm.setGeometry(QtCore.QRect(250, 10, 60, 30))
        self.ButtonConfirm.setObjectName("ButtonConfirm")
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 40, 291, 271))
        self.groupBox.setObjectName("groupBox")
        self.boxA1Button = QtGui.QPushButton(self.groupBox)
        self.boxA1Button.setEnabled(True)
        self.boxA1Button.setGeometry(QtCore.QRect(20, 30, 41, 41))
        self.boxA1Button.setCheckable(False)
        self.boxA1Button.setChecked(False)
        self.boxA1Button.setObjectName("boxA1Button")
        self.boxA2Button = QtGui.QPushButton(self.groupBox)
        self.boxA2Button.setGeometry(QtCore.QRect(90, 30, 41, 41))
        self.boxA2Button.setCheckable(False)
        self.boxA2Button.setChecked(False)
        self.boxA2Button.setObjectName("boxA2Button")
        self.boxA3Button = QtGui.QPushButton(self.groupBox)
        self.boxA3Button.setGeometry(QtCore.QRect(160, 30, 41, 41))
        self.boxA3Button.setCheckable(False)
        self.boxA3Button.setChecked(False)
        self.boxA3Button.setObjectName("boxA3Button")
        self.boxA4Button = QtGui.QPushButton(self.groupBox)
        self.boxA4Button.setGeometry(QtCore.QRect(230, 30, 41, 41))
        self.boxA4Button.setCheckable(False)
        self.boxA4Button.setChecked(False)
        self.boxA4Button.setObjectName("boxA4Button")
        self.boxA8Button = QtGui.QPushButton(self.groupBox)
        self.boxA8Button.setGeometry(QtCore.QRect(230, 90, 41, 41))
        self.boxA8Button.setCheckable(False)
        self.boxA8Button.setChecked(False)
        self.boxA8Button.setObjectName("boxA8Button")
        self.boxA7Button = QtGui.QPushButton(self.groupBox)
        self.boxA7Button.setGeometry(QtCore.QRect(160, 90, 41, 41))
        self.boxA7Button.setCheckable(False)
        self.boxA7Button.setChecked(False)
        self.boxA7Button.setObjectName("boxA7Button")
        self.boxA6Button = QtGui.QPushButton(self.groupBox)
        self.boxA6Button.setGeometry(QtCore.QRect(90, 90, 41, 41))
        self.boxA6Button.setCheckable(False)
        self.boxA6Button.setObjectName("boxA6Button")
        self.boxA5Button = QtGui.QPushButton(self.groupBox)
        self.boxA5Button.setGeometry(QtCore.QRect(20, 90, 41, 41))
        self.boxA5Button.setCheckable(False)
        self.boxA5Button.setObjectName("boxA5Button")
        self.boxA9Button = QtGui.QPushButton(self.groupBox)
        self.boxA9Button.setGeometry(QtCore.QRect(20, 150, 41, 41))
        self.boxA9Button.setCheckable(False)
        self.boxA9Button.setObjectName("boxA9Button")
        self.boxA10Button = QtGui.QPushButton(self.groupBox)
        self.boxA10Button.setGeometry(QtCore.QRect(90, 150, 41, 41))
        self.boxA10Button.setCheckable(False)
        self.boxA10Button.setObjectName("boxA10Button")
        self.boxA11Button = QtGui.QPushButton(self.groupBox)
        self.boxA11Button.setGeometry(QtCore.QRect(160, 150, 41, 41))
        self.boxA11Button.setCheckable(False)
        self.boxA11Button.setObjectName("boxA11Button")
        self.boxA12Button = QtGui.QPushButton(self.groupBox)
        self.boxA12Button.setGeometry(QtCore.QRect(230, 150, 41, 41))
        self.boxA12Button.setCheckable(False)
        self.boxA12Button.setObjectName("boxA12Button")
        self.boxA13Button = QtGui.QPushButton(self.groupBox)
        self.boxA13Button.setGeometry(QtCore.QRect(20, 210, 41, 41))
        self.boxA13Button.setCheckable(False)
        self.boxA13Button.setObjectName("boxA13Button")
        self.boxA14Button = QtGui.QPushButton(self.groupBox)
        self.boxA14Button.setGeometry(QtCore.QRect(90, 210, 41, 41))
        self.boxA14Button.setCheckable(False)
        self.boxA14Button.setObjectName("boxA14Button")
        self.boxA15Button = QtGui.QPushButton(self.groupBox)
        self.boxA15Button.setGeometry(QtCore.QRect(160, 210, 41, 41))
        self.boxA15Button.setCheckable(False)
        self.boxA15Button.setObjectName("boxA15Button")
        self.boxA16Button = QtGui.QPushButton(self.groupBox)
        self.boxA16Button.setGeometry(QtCore.QRect(230, 210, 41, 41))
        self.boxA16Button.setCheckable(False)
        self.boxA16Button.setObjectName("boxA16Button")
        self.lineEditBoxID = QtGui.QLineEdit(Dialog)
        self.lineEditBoxID.setGeometry(QtCore.QRect(170, 10, 70, 30))
        self.lineEditBoxID.setMinimumSize(QtCore.QSize(70, 25))
        self.lineEditBoxID.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEditBoxID.setObjectName("lineEditBoxID")
        self.labelBoxID = QtGui.QLabel(Dialog)
        self.labelBoxID.setGeometry(QtCore.QRect(120, 10, 40, 30))
        self.labelBoxID.setMinimumSize(QtCore.QSize(40, 30))
        self.labelBoxID.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBoxID.setObjectName("labelBoxID")
        self.labelBoxIDShow = QtGui.QLabel(Dialog)
        self.labelBoxIDShow.setGeometry(QtCore.QRect(30, 10, 80, 30))
        self.labelBoxIDShow.setMinimumSize(QtCore.QSize(80, 30))
        self.labelBoxIDShow.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.labelBoxIDShow.setFont(font)
        self.labelBoxIDShow.setText("")
        self.labelBoxIDShow.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelBoxIDShow.setObjectName("labelBoxIDShow")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "FireImmediately", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonConfirm.setText(QtGui.QApplication.translate("Dialog", "Confirm", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "IgnitePoints", None, QtGui.QApplication.UnicodeUTF8))
        self.boxA1Button.setText(QtGui.QApplication.translate("Dialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.boxA2Button.setText(QtGui.QApplication.translate("Dialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.boxA3Button.setText(QtGui.QApplication.translate("Dialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.boxA4Button.setText(QtGui.QApplication.translate("Dialog", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.boxA8Button.setText(QtGui.QApplication.translate("Dialog", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.boxA7Button.setText(QtGui.QApplication.translate("Dialog", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.boxA6Button.setText(QtGui.QApplication.translate("Dialog", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.boxA5Button.setText(QtGui.QApplication.translate("Dialog", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.boxA9Button.setText(QtGui.QApplication.translate("Dialog", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.boxA10Button.setText(QtGui.QApplication.translate("Dialog", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.boxA11Button.setText(QtGui.QApplication.translate("Dialog", "11", None, QtGui.QApplication.UnicodeUTF8))
        self.boxA12Button.setText(QtGui.QApplication.translate("Dialog", "12", None, QtGui.QApplication.UnicodeUTF8))
        self.boxA13Button.setText(QtGui.QApplication.translate("Dialog", "13", None, QtGui.QApplication.UnicodeUTF8))
        self.boxA14Button.setText(QtGui.QApplication.translate("Dialog", "14", None, QtGui.QApplication.UnicodeUTF8))
        self.boxA15Button.setText(QtGui.QApplication.translate("Dialog", "15", None, QtGui.QApplication.UnicodeUTF8))
        self.boxA16Button.setText(QtGui.QApplication.translate("Dialog", "16", None, QtGui.QApplication.UnicodeUTF8))
        self.labelBoxID.setText(QtGui.QApplication.translate("Dialog", "BoxID:", None, QtGui.QApplication.UnicodeUTF8))

