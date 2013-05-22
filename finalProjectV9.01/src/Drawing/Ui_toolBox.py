# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'toolBox.ui'
#
# Created: Thu May 09 10:44:32 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_toolBoxWidget(object):
    def setupUi(self, toolBoxWidget):
        toolBoxWidget.setObjectName("toolBoxWidget")
        toolBoxWidget.resize(1332, 86)
        toolBoxWidget.setAutoFillBackground(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(toolBoxWidget)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.timeEdit_music = QtGui.QTimeEdit(toolBoxWidget)
        self.timeEdit_music.setMinimumSize(QtCore.QSize(60, 25))
        self.timeEdit_music.setMaximumSize(QtCore.QSize(100, 16777215))
        self.timeEdit_music.setTime(QtCore.QTime(0, 0, 0))
        self.timeEdit_music.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.timeEdit_music.setCalendarPopup(True)
        self.timeEdit_music.setObjectName("timeEdit_music")
        self.horizontalLayout.addWidget(self.timeEdit_music)
        self.pushButton_musicReplay = QtGui.QPushButton(toolBoxWidget)
        self.pushButton_musicReplay.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_musicReplay.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Image/Image/replay.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_musicReplay.setIcon(icon)
        self.pushButton_musicReplay.setIconSize(QtCore.QSize(33, 30))
        self.pushButton_musicReplay.setShortcut("")
        self.pushButton_musicReplay.setCheckable(True)
        self.pushButton_musicReplay.setChecked(False)
        self.pushButton_musicReplay.setAutoRepeat(False)
        self.pushButton_musicReplay.setAutoExclusive(False)
        self.pushButton_musicReplay.setObjectName("pushButton_musicReplay")
        self.horizontalLayout.addWidget(self.pushButton_musicReplay)
        self.pushButton_musicPlay = QtGui.QPushButton(toolBoxWidget)
        self.pushButton_musicPlay.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_musicPlay.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Image/Image/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_musicPlay.setIcon(icon1)
        self.pushButton_musicPlay.setIconSize(QtCore.QSize(33, 30))
        self.pushButton_musicPlay.setObjectName("pushButton_musicPlay")
        self.horizontalLayout.addWidget(self.pushButton_musicPlay)
        self.pushButton_musicStop = QtGui.QPushButton(toolBoxWidget)
        self.pushButton_musicStop.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_musicStop.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Image/Image/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_musicStop.setIcon(icon2)
        self.pushButton_musicStop.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_musicStop.setObjectName("pushButton_musicStop")
        self.horizontalLayout.addWidget(self.pushButton_musicStop)
        self.volumeSlider_music = phonon.Phonon.VolumeSlider(toolBoxWidget)
        self.volumeSlider_music.setMaximumSize(QtCore.QSize(200, 16777215))
        self.volumeSlider_music.setObjectName("volumeSlider_music")
        self.horizontalLayout.addWidget(self.volumeSlider_music)
        self.label_5 = QtGui.QLabel(toolBoxWidget)
        self.label_5.setMinimumSize(QtCore.QSize(10, 0))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.volumeSlider_bombMusic = phonon.Phonon.VolumeSlider(toolBoxWidget)
        self.volumeSlider_bombMusic.setMaximumSize(QtCore.QSize(120, 16777215))
        self.volumeSlider_bombMusic.setObjectName("volumeSlider_bombMusic")
        self.horizontalLayout.addWidget(self.volumeSlider_bombMusic)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(toolBoxWidget)
        self.label_2.setMinimumSize(QtCore.QSize(20, 0))
        self.label_2.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.pushButton_zoomIn = QtGui.QPushButton(toolBoxWidget)
        self.pushButton_zoomIn.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_zoomIn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Image/Image/zoomIn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_zoomIn.setIcon(icon3)
        self.pushButton_zoomIn.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_zoomIn.setObjectName("pushButton_zoomIn")
        self.horizontalLayout.addWidget(self.pushButton_zoomIn)
        self.pushButton_zoomOut = QtGui.QPushButton(toolBoxWidget)
        self.pushButton_zoomOut.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_zoomOut.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Image/Image/zoomOut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_zoomOut.setIcon(icon4)
        self.pushButton_zoomOut.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_zoomOut.setObjectName("pushButton_zoomOut")
        self.horizontalLayout.addWidget(self.pushButton_zoomOut)
        self.pushButton_goLeft = QtGui.QPushButton(toolBoxWidget)
        self.pushButton_goLeft.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_goLeft.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Image/Image/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_goLeft.setIcon(icon5)
        self.pushButton_goLeft.setIconSize(QtCore.QSize(32, 30))
        self.pushButton_goLeft.setObjectName("pushButton_goLeft")
        self.horizontalLayout.addWidget(self.pushButton_goLeft)
        self.pushButton_goRight = QtGui.QPushButton(toolBoxWidget)
        self.pushButton_goRight.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_goRight.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Image/Image/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_goRight.setIcon(icon6)
        self.pushButton_goRight.setIconSize(QtCore.QSize(32, 30))
        self.pushButton_goRight.setObjectName("pushButton_goRight")
        self.horizontalLayout.addWidget(self.pushButton_goRight)
        self.pushButton_ampDecrease = QtGui.QPushButton(toolBoxWidget)
        self.pushButton_ampDecrease.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_ampDecrease.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Image/Image/in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ampDecrease.setIcon(icon7)
        self.pushButton_ampDecrease.setIconSize(QtCore.QSize(35, 30))
        self.pushButton_ampDecrease.setObjectName("pushButton_ampDecrease")
        self.horizontalLayout.addWidget(self.pushButton_ampDecrease)
        self.pushButton_ampIncrease = QtGui.QPushButton(toolBoxWidget)
        self.pushButton_ampIncrease.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_ampIncrease.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Image/Image/out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ampIncrease.setIcon(icon8)
        self.pushButton_ampIncrease.setIconSize(QtCore.QSize(35, 30))
        self.pushButton_ampIncrease.setCheckable(False)
        self.pushButton_ampIncrease.setObjectName("pushButton_ampIncrease")
        self.horizontalLayout.addWidget(self.pushButton_ampIncrease)
        self.lcdNumber = QtGui.QLCDNumber(toolBoxWidget)
        self.lcdNumber.setMaximumSize(QtCore.QSize(75, 30))
        self.lcdNumber.setNumDigits(5)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.label_3 = QtGui.QLabel(toolBoxWidget)
        self.label_3.setMinimumSize(QtCore.QSize(20, 0))
        self.label_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.seekSlider_musicProgress = phonon.Phonon.SeekSlider(toolBoxWidget)
        self.seekSlider_musicProgress.setEnabled(True)
        self.seekSlider_musicProgress.setMaximumSize(QtCore.QSize(16777215, 167))
        self.seekSlider_musicProgress.setIconSize(QtCore.QSize(9, 23))
        self.seekSlider_musicProgress.setObjectName("seekSlider_musicProgress")
        self.horizontalLayout_2.addWidget(self.seekSlider_musicProgress)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(toolBoxWidget)
        QtCore.QMetaObject.connectSlotsByName(toolBoxWidget)

    def retranslateUi(self, toolBoxWidget):
        toolBoxWidget.setWindowTitle(QtGui.QApplication.translate("toolBoxWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.timeEdit_music.setDisplayFormat(QtGui.QApplication.translate("toolBoxWidget", "mm:ss", None, QtGui.QApplication.UnicodeUTF8))

from PySide import phonon
import waveIcon_rc
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    toolBoxWidget = QtGui.QWidget()
    ui = Ui_toolBoxWidget()
    ui.setupUi(toolBoxWidget)
    toolBoxWidget.show()
    sys.exit(app.exec_())
