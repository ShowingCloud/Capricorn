# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newProject.ui'
#
# Created: Thu May 02 09:47:18 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(403, 473)
        Dialog.setMinimumSize(QtCore.QSize(403, 400))
        Dialog.setMaximumSize(QtCore.QSize(403, 705))
        Dialog.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.groupBox_project = QtGui.QGroupBox(Dialog)
        self.groupBox_project.setGeometry(QtCore.QRect(10, 10, 381, 451))
        self.groupBox_project.setObjectName("groupBox_project")
        self.labelShowName = QtGui.QLabel(self.groupBox_project)
        self.labelShowName.setGeometry(QtCore.QRect(30, 20, 80, 25))
        self.labelShowName.setMinimumSize(QtCore.QSize(80, 25))
        self.labelShowName.setMaximumSize(QtCore.QSize(80, 25))
        self.labelShowName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelShowName.setObjectName("labelShowName")
        self.labelShowDate = QtGui.QLabel(self.groupBox_project)
        self.labelShowDate.setGeometry(QtCore.QRect(30, 60, 80, 25))
        self.labelShowDate.setMinimumSize(QtCore.QSize(80, 25))
        self.labelShowDate.setMaximumSize(QtCore.QSize(80, 25))
        self.labelShowDate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelShowDate.setObjectName("labelShowDate")
        self.labelShootSite = QtGui.QLabel(self.groupBox_project)
        self.labelShootSite.setGeometry(QtCore.QRect(30, 100, 80, 25))
        self.labelShootSite.setMinimumSize(QtCore.QSize(80, 25))
        self.labelShootSite.setMaximumSize(QtCore.QSize(80, 25))
        self.labelShootSite.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelShootSite.setObjectName("labelShootSite")
        self.labelDesigner = QtGui.QLabel(self.groupBox_project)
        self.labelDesigner.setGeometry(QtCore.QRect(30, 140, 80, 25))
        self.labelDesigner.setMinimumSize(QtCore.QSize(80, 25))
        self.labelDesigner.setMaximumSize(QtCore.QSize(80, 25))
        self.labelDesigner.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDesigner.setObjectName("labelDesigner")
        self.labelFiredBy = QtGui.QLabel(self.groupBox_project)
        self.labelFiredBy.setGeometry(QtCore.QRect(30, 180, 80, 25))
        self.labelFiredBy.setMinimumSize(QtCore.QSize(80, 25))
        self.labelFiredBy.setMaximumSize(QtCore.QSize(80, 25))
        self.labelFiredBy.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelFiredBy.setObjectName("labelFiredBy")
        self.labelNotes = QtGui.QLabel(self.groupBox_project)
        self.labelNotes.setGeometry(QtCore.QRect(30, 220, 80, 25))
        self.labelNotes.setMinimumSize(QtCore.QSize(80, 25))
        self.labelNotes.setMaximumSize(QtCore.QSize(80, 25))
        self.labelNotes.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelNotes.setObjectName("labelNotes")
        self.checkBoxMusic = QtGui.QCheckBox(self.groupBox_project)
        self.checkBoxMusic.setGeometry(QtCore.QRect(130, 340, 130, 25))
        self.checkBoxMusic.setObjectName("checkBoxMusic")
        self.lineEditShowName = QtGui.QLineEdit(self.groupBox_project)
        self.lineEditShowName.setGeometry(QtCore.QRect(130, 20, 160, 25))
        self.lineEditShowName.setMinimumSize(QtCore.QSize(25, 25))
        self.lineEditShowName.setMaximumSize(QtCore.QSize(160, 25))
        self.lineEditShowName.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditShowName.setObjectName("lineEditShowName")
##        self.lineEditShowDate = QtGui.QLineEdit(self.groupBox_project)
        self.lineEditShowDate = QtGui.QDateTimeEdit(self.groupBox_project)
        self.lineEditShowDate.setDateTime(QtCore.QDateTime.currentDateTime())
        self.lineEditShowDate.setDisplayFormat("yyyy/MM/dd")
        self.lineEditShowDate.setCalendarPopup(True)
        self.lineEditShowDate.date()
        
        self.lineEditShowDate.setGeometry(QtCore.QRect(130, 60, 200, 25))
        self.lineEditShowDate.setMinimumSize(QtCore.QSize(25, 25))
        self.lineEditShowDate.setMaximumSize(QtCore.QSize(200, 25))
        self.lineEditShowDate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditShowDate.setObjectName("lineEditShowDate")
        self.lineEditDesigner = QtGui.QLineEdit(self.groupBox_project)
        self.lineEditDesigner.setGeometry(QtCore.QRect(130, 140, 200, 25))
        self.lineEditDesigner.setMinimumSize(QtCore.QSize(25, 25))
        self.lineEditDesigner.setMaximumSize(QtCore.QSize(200, 25))
        self.lineEditDesigner.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditDesigner.setObjectName("lineEditDesigner")
        self.lineEditFiredBy = QtGui.QLineEdit(self.groupBox_project)
        self.lineEditFiredBy.setGeometry(QtCore.QRect(130, 180, 200, 25))
        self.lineEditFiredBy.setMinimumSize(QtCore.QSize(25, 25))
        self.lineEditFiredBy.setMaximumSize(QtCore.QSize(200, 25))
        self.lineEditFiredBy.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditFiredBy.setObjectName("lineEditFiredBy")
        self.lineEditSoundTrack = QtGui.QLineEdit(self.groupBox_project)
        self.lineEditSoundTrack.setGeometry(QtCore.QRect(130, 370, 131, 25))
        self.lineEditSoundTrack.setMinimumSize(QtCore.QSize(25, 25))
        self.lineEditSoundTrack.setMaximumSize(QtCore.QSize(200, 25))
        self.lineEditSoundTrack.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditSoundTrack.setObjectName("lineEditSoundTrack")
        self.textEditNotes = QtGui.QTextEdit(self.groupBox_project)
        self.textEditNotes.setGeometry(QtCore.QRect(130, 220, 201, 71))
        self.textEditNotes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEditNotes.setObjectName("textEditNotes")
        self.labelSoundTrack = QtGui.QLabel(self.groupBox_project)
        self.labelSoundTrack.setGeometry(QtCore.QRect(20, 370, 80, 25))
        self.labelSoundTrack.setMinimumSize(QtCore.QSize(80, 25))
        self.labelSoundTrack.setMaximumSize(QtCore.QSize(80, 25))
        self.labelSoundTrack.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelSoundTrack.setObjectName("labelSoundTrack")
        self.pushButtonSoundTrack = QtGui.QPushButton(self.groupBox_project)
        self.pushButtonSoundTrack.setGeometry(QtCore.QRect(270, 370, 60, 25))
        self.pushButtonSoundTrack.setMinimumSize(QtCore.QSize(60, 25))
        self.pushButtonSoundTrack.setMaximumSize(QtCore.QSize(60, 30))
        self.pushButtonSoundTrack.setObjectName("pushButtonSoundTrack")
        self.pushButtonSave = QtGui.QPushButton(self.groupBox_project)
        self.pushButtonSave.setGeometry(QtCore.QRect(160, 410, 80, 30))
        self.pushButtonSave.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButtonSave.setMaximumSize(QtCore.QSize(80, 30))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.labelDuration = QtGui.QLabel(self.groupBox_project)
        self.labelDuration.setGeometry(QtCore.QRect(20, 310, 80, 25))
        self.labelDuration.setMinimumSize(QtCore.QSize(80, 25))
        self.labelDuration.setMaximumSize(QtCore.QSize(80, 25))
        self.labelDuration.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDuration.setObjectName("labelDuration")
        self.lineEditDurationMin = QtGui.QLineEdit(self.groupBox_project)
        self.lineEditDurationMin.setGeometry(QtCore.QRect(130, 310, 50, 25))
        self.lineEditDurationMin.setMinimumSize(QtCore.QSize(50, 25))
        self.lineEditDurationMin.setMaximumSize(QtCore.QSize(50, 25))
        self.lineEditDurationMin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditDurationMin.setObjectName("lineEditDurationMin")
        self.labelDurationMin = QtGui.QLabel(self.groupBox_project)
        self.labelDurationMin.setGeometry(QtCore.QRect(190, 310, 20, 25))
        self.labelDurationMin.setMinimumSize(QtCore.QSize(20, 25))
        self.labelDurationMin.setMaximumSize(QtCore.QSize(20, 25))
        self.labelDurationMin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDurationMin.setObjectName("labelDurationMin")
        self.lineEditDurationSec = QtGui.QLineEdit(self.groupBox_project)
        self.lineEditDurationSec.setGeometry(QtCore.QRect(220, 310, 50, 25))
        self.lineEditDurationSec.setMinimumSize(QtCore.QSize(50, 25))
        self.lineEditDurationSec.setMaximumSize(QtCore.QSize(50, 25))
        self.lineEditDurationSec.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditDurationSec.setObjectName("lineEditDurationSec")
        self.labelDurationSec = QtGui.QLabel(self.groupBox_project)
        self.labelDurationSec.setGeometry(QtCore.QRect(280, 310, 20, 25))
        self.labelDurationSec.setMinimumSize(QtCore.QSize(20, 25))
        self.labelDurationSec.setMaximumSize(QtCore.QSize(20, 25))
        self.labelDurationSec.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDurationSec.setObjectName("labelDurationSec")
        self.pushButtonImport = QtGui.QPushButton(self.groupBox_project)
        self.pushButtonImport.setGeometry(QtCore.QRect(300, 20, 60, 25))
        self.pushButtonImport.setMinimumSize(QtCore.QSize(60, 25))
        self.pushButtonImport.setMaximumSize(QtCore.QSize(60, 30))
        self.pushButtonImport.setObjectName("pushButtonImport")
        self.comboBoxShootSite = QtGui.QComboBox(self.groupBox_project)
        self.comboBoxShootSite.setGeometry(QtCore.QRect(130, 100, 200, 25))
        self.comboBoxShootSite.setMinimumSize(QtCore.QSize(200, 25))
        self.comboBoxShootSite.setMaximumSize(QtCore.QSize(200, 25))
        self.comboBoxShootSite.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBoxShootSite.setEditable(True)
        self.comboBoxShootSite.setObjectName("comboBoxShootSite")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_project.setTitle(QtGui.QApplication.translate("Dialog", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self.labelShowName.setText(QtGui.QApplication.translate("Dialog", "ShowName:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelShowDate.setText(QtGui.QApplication.translate("Dialog", "ShowDate:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelShootSite.setText(QtGui.QApplication.translate("Dialog", "ShootSite:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDesigner.setText(QtGui.QApplication.translate("Dialog", "Designer:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFiredBy.setText(QtGui.QApplication.translate("Dialog", "Fired By:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelNotes.setText(QtGui.QApplication.translate("Dialog", "Notes:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxMusic.setText(QtGui.QApplication.translate("Dialog", "Use Music Duration", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSoundTrack.setText(QtGui.QApplication.translate("Dialog", "Sound track:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSoundTrack.setText(QtGui.QApplication.translate("Dialog", "Find", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSave.setText(QtGui.QApplication.translate("Dialog", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDuration.setText(QtGui.QApplication.translate("Dialog", "Duration:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDurationMin.setText(QtGui.QApplication.translate("Dialog", "min", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDurationSec.setText(QtGui.QApplication.translate("Dialog", "Sec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonImport.setText(QtGui.QApplication.translate("Dialog", "Import", None, QtGui.QApplication.UnicodeUTF8))

