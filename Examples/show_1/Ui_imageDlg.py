# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\python_work\show_1\imageDlg.ui'
#
# Created: Wed Jan 23 14:15:01 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(504, 415)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 95, 86, 20))
        self.label_4.setObjectName("label_4")
        self.widthSpinBox = QtGui.QSpinBox(Dialog)
        self.widthSpinBox.setGeometry(QtCore.QRect(162, 43, 85, 20))
        self.widthSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.widthSpinBox.setMinimum(8)
        self.widthSpinBox.setMaximum(512)
        self.widthSpinBox.setSingleStep(4)
        self.widthSpinBox.setProperty("value", 64)
        self.widthSpinBox.setObjectName("widthSpinBox")
        self.heightSpinBox = QtGui.QSpinBox(Dialog)
        self.heightSpinBox.setGeometry(QtCore.QRect(162, 69, 85, 20))
        self.heightSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.heightSpinBox.setMinimum(8)
        self.heightSpinBox.setMaximum(512)
        self.heightSpinBox.setSingleStep(4)
        self.heightSpinBox.setProperty("value", 64)
        self.heightSpinBox.setObjectName("heightSpinBox")
        self.colorButton = QtGui.QPushButton(Dialog)
        self.colorButton.setGeometry(QtCore.QRect(253, 121, 86, 23))
        self.colorButton.setObjectName("colorButton")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 121, 86, 23))
        self.label_3.setObjectName("label_3")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 43, 86, 20))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 69, 86, 20))
        self.label_2.setObjectName("label_2")
        self.brushComboBox = QtGui.QComboBox(Dialog)
        self.brushComboBox.setGeometry(QtCore.QRect(162, 95, 177, 20))
        self.brushComboBox.setObjectName("brushComboBox")
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(170, 320, 177, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.colorLabel = QtGui.QLabel(Dialog)
        self.colorLabel.setGeometry(QtCore.QRect(160, 140, 71, 31))
        self.colorLabel.setObjectName("colorLabel")
        self.label_4.setBuddy(self.brushComboBox)
        self.label.setBuddy(self.widthSpinBox)
        self.label_2.setBuddy(self.heightSpinBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "&Brush pattern:", None, QtGui.QApplication.UnicodeUTF8))
        self.widthSpinBox.setSuffix(QtGui.QApplication.translate("Dialog", " px", None, QtGui.QApplication.UnicodeUTF8))
        self.heightSpinBox.setSuffix(QtGui.QApplication.translate("Dialog", " px", None, QtGui.QApplication.UnicodeUTF8))
        self.colorButton.setText(QtGui.QApplication.translate("Dialog", "&Color...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "&Width:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "&Height:", None, QtGui.QApplication.UnicodeUTF8))
        self.colorLabel.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

