# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\python_work\plotWav\0330_waveModule\waveModule.ui'
#
# Created: Tue Apr 02 14:18:35 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_widget_waveModule(object):
    def setupUi(self, widget_waveModule):
        widget_waveModule.setObjectName("widget_waveModule")
        widget_waveModule.setWindowModality(QtCore.Qt.NonModal)
        widget_waveModule.resize(1053, 413)
        widget_waveModule.setAutoFillBackground(False)
        self.gridLayout = QtGui.QGridLayout(widget_waveModule)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_musicToolBox = QtGui.QHBoxLayout()
        self.horizontalLayout_musicToolBox.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_musicToolBox.setObjectName("horizontalLayout_musicToolBox")
        self.verticalLayout.addLayout(self.horizontalLayout_musicToolBox)
        self.horizontalLayout_plots = QtGui.QHBoxLayout()
        self.horizontalLayout_plots.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_plots.setObjectName("horizontalLayout_plots")
        self.verticalLayout.addLayout(self.horizontalLayout_plots)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(widget_waveModule)
        QtCore.QMetaObject.connectSlotsByName(widget_waveModule)

    def retranslateUi(self, widget_waveModule):
        widget_waveModule.setWindowTitle(QtGui.QApplication.translate("widget_waveModule", "Form", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    widget_waveModule = QtGui.QWidget()
    ui = Ui_widget_waveModule()
    ui.setupUi(widget_waveModule)
    widget_waveModule.show()
    sys.exit(app.exec_())

