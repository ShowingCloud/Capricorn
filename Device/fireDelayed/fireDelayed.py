# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fireDelayed.ui'
#
# Created: Mon Apr 22 15:41:52 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(556, 369)
        Dialog.setMinimumSize(QtCore.QSize(556, 369))
        Dialog.setMaximumSize(QtCore.QSize(556, 369))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        Dialog.setFont(font)
        self.labelBoxID = QtGui.QLabel(Dialog)
        self.labelBoxID.setGeometry(QtCore.QRect(10, 30, 85, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.labelBoxID.setFont(font)
        self.labelBoxID.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelBoxID.setObjectName("labelBoxID")
        self.lineEditBoxID = QtGui.QLineEdit(Dialog)
        self.lineEditBoxID.setGeometry(QtCore.QRect(120, 30, 80, 30))
        self.lineEditBoxID.setObjectName("lineEditBoxID")
        self.labelHead = QtGui.QLabel(Dialog)
        self.labelHead.setGeometry(QtCore.QRect(10, 90, 85, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.labelHead.setFont(font)
        self.labelHead.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelHead.setObjectName("labelHead")
        self.labelTime = QtGui.QLabel(Dialog)
        self.labelTime.setGeometry(QtCore.QRect(20, 150, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.labelTime.setFont(font)
        self.labelTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTime.setObjectName("labelTime")
        self.lineEditHead = QtGui.QLineEdit(Dialog)
        self.lineEditHead.setGeometry(QtCore.QRect(120, 90, 80, 30))
        self.lineEditHead.setObjectName("lineEditHead")
        self.lineEditTime = QtGui.QLineEdit(Dialog)
        self.lineEditTime.setGeometry(QtCore.QRect(120, 150, 80, 30))
        self.lineEditTime.setText("")
        self.lineEditTime.setObjectName("lineEditTime")
        self.pushButtonAdd = QtGui.QPushButton(Dialog)
        self.pushButtonAdd.setGeometry(QtCore.QRect(30, 240, 75, 40))
        self.pushButtonAdd.setMinimumSize(QtCore.QSize(60, 40))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.pushButtonAdd.setChecked(False)
        self.pushButtonDownload = QtGui.QPushButton(Dialog)
        self.pushButtonDownload.setGeometry(QtCore.QRect(130, 240, 75, 40))
        self.pushButtonDownload.setMinimumSize(QtCore.QSize(60, 40))
        self.pushButtonDownload.setObjectName("pushButtonDownload")
        self.pushButtonDownload.setChecked(False)
        self.pushButtonStart = QtGui.QPushButton(Dialog)
        self.pushButtonStart.setGeometry(QtCore.QRect(30, 300, 75, 40))
        self.pushButtonStart.setMinimumSize(QtCore.QSize(60, 40))
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.pushButtonStart.setChecked(False)
        self.pushButtonPause = QtGui.QPushButton(Dialog)
        self.pushButtonPause.setGeometry(QtCore.QRect(130, 300, 75, 40))
        self.pushButtonPause.setMinimumSize(QtCore.QSize(60, 40))
        self.pushButtonPause.setObjectName("pushButtonPause")
        self.pushButtonPause.setChecked(False)
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(220, 20, 321, 331))
        self.tableView.setObjectName("tableView")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Ignition test", None, QtGui.QApplication.UnicodeUTF8))
        self.labelBoxID.setText(QtGui.QApplication.translate("Dialog", "BoxID:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelHead.setText(QtGui.QApplication.translate("Dialog", "Ignitor Head:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTime.setText(QtGui.QApplication.translate("Dialog", "Time:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAdd.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDownload.setText(QtGui.QApplication.translate("Dialog", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonStart.setText(QtGui.QApplication.translate("Dialog", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonPause.setText(QtGui.QApplication.translate("Dialog", "Pause", None, QtGui.QApplication.UnicodeUTF8))
