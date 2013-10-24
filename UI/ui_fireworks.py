# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fireworks.ui'
#
# Created: Mon Oct 21 15:20:54 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_widgetWaveModule(object):
    def setupUi(self, widgetWaveModule):
        widgetWaveModule.setObjectName("widgetWaveModule")
        widgetWaveModule.resize(897, 526)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/title.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        widgetWaveModule.setWindowIcon(icon)
        widgetWaveModule.setAutoFillBackground(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(widgetWaveModule)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayoutButton = QtGui.QHBoxLayout()
        self.horizontalLayoutButton.setSpacing(10)
        self.horizontalLayoutButton.setObjectName("horizontalLayoutButton")
        self.lcdNumber = QtGui.QLCDNumber(widgetWaveModule)
        self.lcdNumber.setMinimumSize(QtCore.QSize(80, 30))
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayoutButton.addWidget(self.lcdNumber)
        self.pushButtonOpenMusic = QtGui.QPushButton(widgetWaveModule)
        self.pushButtonOpenMusic.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButtonOpenMusic.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Images/openMusic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonOpenMusic.setIcon(icon1)
        self.pushButtonOpenMusic.setIconSize(QtCore.QSize(25, 27))
        self.pushButtonOpenMusic.setObjectName("pushButtonOpenMusic")
        self.horizontalLayoutButton.addWidget(self.pushButtonOpenMusic)
        self.pushButtonPlayOrPause = QtGui.QPushButton(widgetWaveModule)
        self.pushButtonPlayOrPause.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButtonPlayOrPause.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Images/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonPlayOrPause.setIcon(icon2)
        self.pushButtonPlayOrPause.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonPlayOrPause.setObjectName("pushButtonPlayOrPause")
        self.horizontalLayoutButton.addWidget(self.pushButtonPlayOrPause)
        self.pushButtonStop = QtGui.QPushButton(widgetWaveModule)
        self.pushButtonStop.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButtonStop.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Images/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonStop.setIcon(icon3)
        self.pushButtonStop.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonStop.setObjectName("pushButtonStop")
        self.horizontalLayoutButton.addWidget(self.pushButtonStop)
        self.volumeSlider = phonon.Phonon.VolumeSlider(widgetWaveModule)
        self.volumeSlider.setMinimumSize(QtCore.QSize(80, 30))
        self.volumeSlider.setMaximumSize(QtCore.QSize(180, 30))
        self.volumeSlider.setIconSize(QtCore.QSize(30, 30))
        self.volumeSlider.setObjectName("volumeSlider")
        self.horizontalLayoutButton.addWidget(self.volumeSlider)
        spacerItem = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayoutButton.addItem(spacerItem)
        self.pushButtonDelay = QtGui.QPushButton(widgetWaveModule)
        self.pushButtonDelay.setMinimumSize(QtCore.QSize(29, 30))
        self.pushButtonDelay.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButtonDelay.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Images/clock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDelay.setIcon(icon4)
        self.pushButtonDelay.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonDelay.setObjectName("pushButtonDelay")
        self.horizontalLayoutButton.addWidget(self.pushButtonDelay)
        self.pushButtonUpLoad = QtGui.QPushButton(widgetWaveModule)
        self.pushButtonUpLoad.setMinimumSize(QtCore.QSize(29, 30))
        self.pushButtonUpLoad.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButtonUpLoad.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Images/upLoad.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonUpLoad.setIcon(icon5)
        self.pushButtonUpLoad.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonUpLoad.setObjectName("pushButtonUpLoad")
        self.horizontalLayoutButton.addWidget(self.pushButtonUpLoad)
        self.pushButtonOpenPro = QtGui.QPushButton(widgetWaveModule)
        self.pushButtonOpenPro.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButtonOpenPro.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Images/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonOpenPro.setIcon(icon6)
        self.pushButtonOpenPro.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonOpenPro.setShortcut("")
        self.pushButtonOpenPro.setCheckable(False)
        self.pushButtonOpenPro.setChecked(False)
        self.pushButtonOpenPro.setAutoRepeat(False)
        self.pushButtonOpenPro.setAutoExclusive(False)
        self.pushButtonOpenPro.setObjectName("pushButtonOpenPro")
        self.horizontalLayoutButton.addWidget(self.pushButtonOpenPro)
        self.pushButtonSavePro = QtGui.QPushButton(widgetWaveModule)
        self.pushButtonSavePro.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButtonSavePro.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSavePro.setIcon(icon7)
        self.pushButtonSavePro.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonSavePro.setShortcut("")
        self.pushButtonSavePro.setCheckable(False)
        self.pushButtonSavePro.setChecked(False)
        self.pushButtonSavePro.setAutoRepeat(False)
        self.pushButtonSavePro.setAutoExclusive(False)
        self.pushButtonSavePro.setObjectName("pushButtonSavePro")
        self.horizontalLayoutButton.addWidget(self.pushButtonSavePro)
        self.labelTotal = QtGui.QLabel(widgetWaveModule)
        self.labelTotal.setText("")
        self.labelTotal.setObjectName("labelTotal")
        self.horizontalLayoutButton.addWidget(self.labelTotal)
        self.comboBoxMode = QtGui.QComboBox(widgetWaveModule)
        self.comboBoxMode.setMinimumSize(QtCore.QSize(80, 30))
        self.comboBoxMode.setObjectName("comboBoxMode")
        self.comboBoxMode.addItem("")
        self.comboBoxMode.addItem("")
        self.horizontalLayoutButton.addWidget(self.comboBoxMode)
        self.verticalLayout.addLayout(self.horizontalLayoutButton)
        self.horizontalLayoutSilider = QtGui.QHBoxLayout()
        self.horizontalLayoutSilider.setSpacing(0)
        self.horizontalLayoutSilider.setObjectName("horizontalLayoutSilider")
        self.seekSlider = phonon.Phonon.SeekSlider(widgetWaveModule)
        self.seekSlider.setObjectName("seekSlider")
        self.horizontalLayoutSilider.addWidget(self.seekSlider)
        self.verticalLayout.addLayout(self.horizontalLayoutSilider)
        self.horizontalLayoutTable = QtGui.QHBoxLayout()
        self.horizontalLayoutTable.setSpacing(6)
        self.horizontalLayoutTable.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutTable.setObjectName("horizontalLayoutTable")
        self.listWidgetLocal = QtGui.QListWidget(widgetWaveModule)
        self.listWidgetLocal.setMinimumSize(QtCore.QSize(75, 0))
        self.listWidgetLocal.setMaximumSize(QtCore.QSize(75, 16777215))
        self.listWidgetLocal.setIconSize(QtCore.QSize(48, 48))
        self.listWidgetLocal.setMovement(QtGui.QListView.Static)
        self.listWidgetLocal.setViewMode(QtGui.QListView.IconMode)
        self.listWidgetLocal.setObjectName("listWidgetLocal")
        self.horizontalLayoutTable.addWidget(self.listWidgetLocal)
        self.tableViewLocal = QtGui.QTableView(widgetWaveModule)
        self.tableViewLocal.setObjectName("tableViewLocal")
        self.horizontalLayoutTable.addWidget(self.tableViewLocal)
        self.scriptTableView = QtGui.QTableView(widgetWaveModule)
        self.scriptTableView.setObjectName("scriptTableView")
        self.horizontalLayoutTable.addWidget(self.scriptTableView)
        self.horizontalLayoutTable.setStretch(0, 2)
        self.horizontalLayoutTable.setStretch(1, 2)
        self.horizontalLayoutTable.setStretch(2, 15)
        self.verticalLayout.addLayout(self.horizontalLayoutTable)
        self.widget = QtGui.QWidget(widgetWaveModule)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 12)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(widgetWaveModule)
        QtCore.QMetaObject.connectSlotsByName(widgetWaveModule)

    def retranslateUi(self, widgetWaveModule):
        widgetWaveModule.setWindowTitle(QtGui.QApplication.translate("widgetWaveModule", "Fireworks Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxMode.setItemText(0, QtGui.QApplication.translate("widgetWaveModule", "Edit mode", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxMode.setItemText(1, QtGui.QApplication.translate("widgetWaveModule", "Control mode", None, QtGui.QApplication.UnicodeUTF8))

from PySide import phonon
from Resource import images_rc
