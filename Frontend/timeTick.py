# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timeTick.ui'
#
# Created: Sun Oct 13 23:45:52 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(246, 111)
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowSystemMenuHint)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lcdNumber = QtGui.QLCDNumber(Dialog)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout.addWidget(self.lcdNumber)

class TimeTickShow(QtGui.QDialog):
    def __init__(self,delaySeconds,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.timeRemains = delaySeconds 
        displayTime = QtCore.QTime(0, (self.timeRemains / 60) % 60, (self.timeRemains) % 60)
        self.ui.lcdNumber.display(displayTime.toString('mm:ss'))
        
    
        


