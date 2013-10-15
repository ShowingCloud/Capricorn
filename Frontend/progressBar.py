# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progressBar.ui'
#
# Created: Mon Oct 14 17:02:12 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 48)
        Dialog.setMinimumSize(QtCore.QSize(450, 48))
        Dialog.setMaximumSize(QtCore.QSize(450, 48))
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowSystemMenuHint)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 30))
        self.progressBar.setMaximumSize(QtCore.QSize(450, 30))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)


class ProgressBarShow(QtGui.QDialog):
    def __init__(self,fireworksCount,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.progressBar.setMinimum(0)  
        self.ui.progressBar.setMaximum(fireworksCount)
