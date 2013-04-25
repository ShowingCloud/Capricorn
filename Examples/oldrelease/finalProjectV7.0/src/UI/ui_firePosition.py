# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_firePosition.ui'
#
# Created: Tue Apr 02 10:56:58 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FirePositionDialog(object):
    def setupUi(self, FirePositionDialog):
        FirePositionDialog.setObjectName("FirePositionDialog")
        FirePositionDialog.resize(645, 426)
        FirePositionDialog.setMinimumSize(QtCore.QSize(645, 426))
        FirePositionDialog.setMaximumSize(QtCore.QSize(645, 426))
        self.pushButtonAdd = QtGui.QPushButton(FirePositionDialog)
        self.pushButtonAdd.setGeometry(QtCore.QRect(20, 10, 60, 30))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.pushButtonClone = QtGui.QPushButton(FirePositionDialog)
        self.pushButtonClone.setGeometry(QtCore.QRect(90, 10, 60, 30))
        self.pushButtonClone.setObjectName("pushButtonClone")
        self.pushButtonDelete = QtGui.QPushButton(FirePositionDialog)
        self.pushButtonDelete.setGeometry(QtCore.QRect(210, 10, 60, 30))
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.comboBoxPosition = QtGui.QComboBox(FirePositionDialog)
        self.comboBoxPosition.setGeometry(QtCore.QRect(20, 50, 250, 25))
        self.comboBoxPosition.setEditable(True)
        self.comboBoxPosition.setObjectName("comboBoxPosition")
        self.listWidgetPosition = QtGui.QListWidget(FirePositionDialog)
        self.listWidgetPosition.setGeometry(QtCore.QRect(20, 80, 250, 290))
        self.listWidgetPosition.setObjectName("listWidgetPosition")
        #QtGui.QListWidgetItem(self.listWidgetPosition)
        self.radioButtonFeet = QtGui.QRadioButton(FirePositionDialog)
        self.radioButtonFeet.setGeometry(QtCore.QRect(380, 50, 89, 25))
        self.radioButtonFeet.setChecked(True)
        self.radioButtonFeet.setObjectName("radioButtonFeet")
        self.radioButtonMeter = QtGui.QRadioButton(FirePositionDialog)
        self.radioButtonMeter.setGeometry(QtCore.QRect(470, 50, 89, 25))
        self.radioButtonMeter.setObjectName("radioButtonMeter")
        self.groupBoxField = QtGui.QGroupBox(FirePositionDialog)
        self.groupBoxField.setGeometry(QtCore.QRect(290, 70, 331, 191))
        self.groupBoxField.setObjectName("groupBoxField")
        self.labelName = QtGui.QLabel(self.groupBoxField)
        self.labelName.setGeometry(QtCore.QRect(10, 20, 80, 25))
        self.labelName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelName.setObjectName("labelName")
        self.labelPosition = QtGui.QLabel(self.groupBoxField)
        self.labelPosition.setGeometry(QtCore.QRect(10, 80, 80, 25))
        self.labelPosition.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPosition.setObjectName("labelPosition")
        self.labelAngle = QtGui.QLabel(self.groupBoxField)
        self.labelAngle.setGeometry(QtCore.QRect(170, 120, 60, 25))
        self.labelAngle.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelAngle.setObjectName("labelAngle")
        self.labelDirection = QtGui.QLabel(self.groupBoxField)
        self.labelDirection.setGeometry(QtCore.QRect(10, 120, 80, 25))
        self.labelDirection.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDirection.setObjectName("labelDirection")
        self.labelReference = QtGui.QLabel(self.groupBoxField)
        self.labelReference.setGeometry(QtCore.QRect(10, 160, 80, 25))
        self.labelReference.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelReference.setObjectName("labelReference")
        self.lineEditName = QtGui.QLineEdit(self.groupBoxField)
        self.lineEditName.setGeometry(QtCore.QRect(100, 20, 200, 25))
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditPositionX = QtGui.QLineEdit(self.groupBoxField)
        self.lineEditPositionX.setGeometry(QtCore.QRect(100, 80, 50, 25))
        self.lineEditPositionX.setObjectName("lineEditPositionX")
        self.labelX = QtGui.QLabel(self.groupBoxField)
        self.labelX.setGeometry(QtCore.QRect(110, 50, 30, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.labelX.setFont(font)
        self.labelX.setAlignment(QtCore.Qt.AlignCenter)
        self.labelX.setObjectName("labelX")
        self.labelY = QtGui.QLabel(self.groupBoxField)
        self.labelY.setGeometry(QtCore.QRect(180, 50, 30, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.labelY.setFont(font)
        self.labelY.setAlignment(QtCore.Qt.AlignCenter)
        self.labelY.setObjectName("labelY")
        self.labelZ = QtGui.QLabel(self.groupBoxField)
        self.labelZ.setGeometry(QtCore.QRect(250, 50, 30, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.labelZ.setFont(font)
        self.labelZ.setAlignment(QtCore.Qt.AlignCenter)
        self.labelZ.setObjectName("labelZ")
        self.lineEditPositionY = QtGui.QLineEdit(self.groupBoxField)
        self.lineEditPositionY.setGeometry(QtCore.QRect(170, 80, 50, 25))
        self.lineEditPositionY.setObjectName("lineEditPositionY")
        self.lineEditPositionZ = QtGui.QLineEdit(self.groupBoxField)
        self.lineEditPositionZ.setGeometry(QtCore.QRect(240, 80, 50, 25))
        self.lineEditPositionZ.setObjectName("lineEditPositionZ")
        self.lineEditAngle = QtGui.QLineEdit(self.groupBoxField)
        self.lineEditAngle.setGeometry(QtCore.QRect(240, 120, 50, 25))
        self.lineEditAngle.setObjectName("lineEditAngle")
        self.lineEditDirection = QtGui.QLineEdit(self.groupBoxField)
        self.lineEditDirection.setGeometry(QtCore.QRect(100, 120, 50, 25))
        self.lineEditDirection.setObjectName("lineEditDirection")
        self.comboBoxReference = QtGui.QComboBox(self.groupBoxField)
        self.comboBoxReference.setGeometry(QtCore.QRect(100, 160, 200, 25))
        self.comboBoxReference.setEditable(True)
        self.comboBoxReference.setObjectName("comboBoxReference")
        self.checkBoxPosition = QtGui.QCheckBox(self.groupBoxField)
        self.checkBoxPosition.setGeometry(QtCore.QRect(300, 80, 25, 25))
        self.checkBoxPosition.setText("")
        self.checkBoxPosition.setObjectName("checkBoxPosition")
        self.checkBoxAngle = QtGui.QCheckBox(self.groupBoxField)
        self.checkBoxAngle.setGeometry(QtCore.QRect(300, 120, 25, 25))
        self.checkBoxAngle.setText("")
        self.checkBoxAngle.setObjectName("checkBoxAngle")
        self.pushButtonDone = QtGui.QPushButton(FirePositionDialog)
        self.pushButtonDone.setGeometry(QtCore.QRect(420, 380, 60, 30))
        self.pushButtonDone.setObjectName("pushButtonDone")
        self.pushButtonCancel = QtGui.QPushButton(FirePositionDialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(500, 380, 60, 30))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.pushButtonHelp = QtGui.QPushButton(FirePositionDialog)
        self.pushButtonHelp.setGeometry(QtCore.QRect(590, 380, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButtonHelp.setFont(font)
        self.pushButtonHelp.setObjectName("pushButtonHelp")
        self.groupBoxIgnition = QtGui.QGroupBox(FirePositionDialog)
        self.groupBoxIgnition.setGeometry(QtCore.QRect(290, 270, 331, 101))
        self.groupBoxIgnition.setObjectName("groupBoxIgnition")
        self.labelIgnitionBoxID = QtGui.QLabel(self.groupBoxIgnition)
        self.labelIgnitionBoxID.setGeometry(QtCore.QRect(20, 20, 100, 25))
        self.labelIgnitionBoxID.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelIgnitionBoxID.setObjectName("labelIgnitionBoxID")
        self.labelIgnitionPoints = QtGui.QLabel(self.groupBoxIgnition)
        self.labelIgnitionPoints.setGeometry(QtCore.QRect(20, 60, 100, 25))
        self.labelIgnitionPoints.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelIgnitionPoints.setObjectName("labelIgnitionPoints")
        self.comboBoxIgnitionBoxPoints = QtGui.QComboBox(self.groupBoxIgnition)
        self.comboBoxIgnitionBoxPoints.setGeometry(QtCore.QRect(140, 60, 80, 25))
        self.comboBoxIgnitionBoxPoints.setObjectName("comboBoxIgnitionBoxPoints")
        self.comboBoxIgnitionBoxPoints.addItem("")
        self.comboBoxIgnitionBoxPoints.addItem("")
        self.comboBoxIgnitionBoxID = QtGui.QComboBox(self.groupBoxIgnition)
        self.comboBoxIgnitionBoxID.setGeometry(QtCore.QRect(140, 20, 80, 25))
        self.comboBoxIgnitionBoxID.setObjectName("comboBoxIgnitionBoxID")
        self.comboBoxIgnitionBoxID.addItem("")
        self.comboBoxIgnitionBoxID.addItem("")
        self.comboBoxIgnitionBoxID.addItem("")
        self.comboBoxIgnitionBoxID.addItem("")
        self.comboBoxIgnitionBoxID.addItem("")
        self.comboBoxIgnitionBoxID.addItem("")

        self.retranslateUi(FirePositionDialog)
        QtCore.QMetaObject.connectSlotsByName(FirePositionDialog)

    def retranslateUi(self, FirePositionDialog):
        FirePositionDialog.setWindowTitle(QtGui.QApplication.translate("FirePositionDialog", "FirePositionEditor", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAdd.setText(QtGui.QApplication.translate("FirePositionDialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonClone.setText(QtGui.QApplication.translate("FirePositionDialog", "Clone", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDelete.setText(QtGui.QApplication.translate("FirePositionDialog", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidgetPosition.isSortingEnabled()
        self.listWidgetPosition.setSortingEnabled(False)
        #self.listWidgetPosition.item(0).setText(QtGui.QApplication.translate("FirePositionDialog", "Court - center", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetPosition.setSortingEnabled(__sortingEnabled)
        self.radioButtonFeet.setText(QtGui.QApplication.translate("FirePositionDialog", "feet", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonMeter.setText(QtGui.QApplication.translate("FirePositionDialog", "meters", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxField.setTitle(QtGui.QApplication.translate("FirePositionDialog", "Field info", None, QtGui.QApplication.UnicodeUTF8))
        self.labelName.setText(QtGui.QApplication.translate("FirePositionDialog", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPosition.setText(QtGui.QApplication.translate("FirePositionDialog", "Position:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelAngle.setText(QtGui.QApplication.translate("FirePositionDialog", "Angle:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDirection.setText(QtGui.QApplication.translate("FirePositionDialog", "Direction:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelReference.setText(QtGui.QApplication.translate("FirePositionDialog", "Reference:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelX.setText(QtGui.QApplication.translate("FirePositionDialog", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.labelY.setText(QtGui.QApplication.translate("FirePositionDialog", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.labelZ.setText(QtGui.QApplication.translate("FirePositionDialog", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDone.setText(QtGui.QApplication.translate("FirePositionDialog", "Done", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancel.setText(QtGui.QApplication.translate("FirePositionDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonHelp.setText(QtGui.QApplication.translate("FirePositionDialog", "?", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxIgnition.setTitle(QtGui.QApplication.translate("FirePositionDialog", "Ignition Box", None, QtGui.QApplication.UnicodeUTF8))
        self.labelIgnitionBoxID.setText(QtGui.QApplication.translate("FirePositionDialog", "Ignition box ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelIgnitionPoints.setText(QtGui.QApplication.translate("FirePositionDialog", "Ignition points:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxIgnitionBoxPoints.setItemText(0, QtGui.QApplication.translate("FirePositionDialog", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxIgnitionBoxPoints.setItemText(1, QtGui.QApplication.translate("FirePositionDialog", "50", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxIgnitionBoxID.setItemText(0, QtGui.QApplication.translate("FirePositionDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxIgnitionBoxID.setItemText(1, QtGui.QApplication.translate("FirePositionDialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxIgnitionBoxID.setItemText(2, QtGui.QApplication.translate("FirePositionDialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxIgnitionBoxID.setItemText(3, QtGui.QApplication.translate("FirePositionDialog", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxIgnitionBoxID.setItemText(4, QtGui.QApplication.translate("FirePositionDialog", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxIgnitionBoxID.setItemText(5, QtGui.QApplication.translate("FirePositionDialog", "6", None, QtGui.QApplication.UnicodeUTF8))

