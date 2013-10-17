# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Thu Oct 17 19:47:35 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(764, 515)
        Form.setMinimumSize(QtCore.QSize(764, 515))
        Form.setMaximumSize(QtCore.QSize(764, 515))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/title.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
#         Form.setAutoFillBackground(False)
#         Form.setStyleSheet("image: url(:/Images/main.png);")
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap(":/Images/main.png")))
        Form.setPalette(palette)
        
        self.pushButtonConnect = QtGui.QPushButton(Form)
        self.pushButtonConnect.setGeometry(QtCore.QRect(290, 260, 150, 30))
        self.pushButtonConnect.setFlat(False)
        self.pushButtonConnect.setObjectName("pushButtonConnect")
        self.pushButtonFire = QtGui.QPushButton(Form)
        self.pushButtonFire.setGeometry(QtCore.QRect(290, 330, 150, 30))
        self.pushButtonFire.setObjectName("pushButtonFire")
        self.pushButtonProject = QtGui.QPushButton(Form)
        self.pushButtonProject.setGeometry(QtCore.QRect(290, 400, 150, 30))
        self.pushButtonProject.setObjectName("pushButtonProject")
        self.pushButtonExit = QtGui.QPushButton(Form)
        self.pushButtonExit.setGeometry(QtCore.QRect(674, 470, 61, 23))
        self.pushButtonExit.setObjectName("pushButtonExit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "音乐烟花V1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonConnect.setText(QtGui.QApplication.translate("Form", "连接测试", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFire.setText(QtGui.QApplication.translate("Form", "手动燃放", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonProject.setText(QtGui.QApplication.translate("Form", "工程编辑", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonExit.setText(QtGui.QApplication.translate("Form", "退出", None, QtGui.QApplication.UnicodeUTF8))

from Resource import images_rc
