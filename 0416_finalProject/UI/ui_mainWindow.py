# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainWindow.ui'
#
# Created: Sat Mar 23 16:03:04 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from Drawing.waveModule import WaveWidget
from PySide import QtCore, QtGui
from UI.mainWidget import MainWidget

class Ui_MainWindow(object):
    def __init__(self, sess, session, fieldUUID,musicPath):
        self.sess = sess
        self.session = session
        self.fieldUUID = fieldUUID
        self.musicPath = musicPath
        print self.musicPath
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1245, 903)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.widgetDatabase = MainWidget(self.sess, self.session, self.fieldUUID)
        self.widgetDatabase.setContentsMargins(-10,-10,-10,-10)

        self.widgetDatabase.setObjectName("widgetDatabase")
        self.verticalLayout.addWidget(self.widgetDatabase)
        self.groupBox_wave = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_wave.setObjectName("groupBox_wave")
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.groupBox_wave)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
 #       self.widget_wave = QtGui.QWidget(self.groupBox_wave)
        self.widget_wave = WaveWidget(self.session,self.musicPath,self.sess)
        
        self.widget_wave.setObjectName("widget_wave")
        self.horizontalLayout_11.addWidget(self.widget_wave)
        self.verticalLayout_13.addLayout(self.horizontalLayout_11)
        self.verticalLayout.addWidget(self.groupBox_wave)
        self.verticalLayout.setStretch(0, 45)
        self.verticalLayout.setStretch(1, 45)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1245, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuMusic = QtGui.QMenu(self.menubar)
        self.menuMusic.setObjectName("menuMusic")
        self.menuZoom = QtGui.QMenu(self.menubar)
        self.menuZoom.setObjectName("menuZoom")

        self.menuScript = QtGui.QMenu(self.menubar)
        self.menuScript.setObjectName("menuScript")
        self.menuExtras = QtGui.QMenu(self.menubar)
        self.menuExtras.setObjectName("menuExtras")
        self.menuWindow = QtGui.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuInfo = QtGui.QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")
        self.menuPFM_Advanced = QtGui.QMenu(self.menubar)
        self.menuPFM_Advanced.setObjectName("menuPFM_Advanced")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionProjectExport = QtGui.QAction(MainWindow)
        self.actionProjectExport.setObjectName("actionProjectExport")
#        self.actionProjectSave_as = QtGui.QAction(MainWindow)
#        self.actionProjectSave_as.setObjectName("actionProjectSave_as")
        
        self.actionDownload = QtGui.QAction(MainWindow)
        self.actionDownload.setObjectName("actionDownload")
        self.actionExportPDF = QtGui.QAction(MainWindow)
        self.actionDownload.setObjectName("actionExportPDF")
        
        
#        self.actionImport_music = QtGui.QAction(MainWindow)
#        self.actionImport_music.setObjectName("actionImport_music")
        self.actionPlay = QtGui.QAction(MainWindow)
        self.actionPlay.setObjectName("actionPlay")
        self.actionPause = QtGui.QAction(MainWindow)
        self.actionPause.setObjectName("actionPause")
        self.actionStop = QtGui.QAction(MainWindow)
        self.actionStop.setObjectName("actionStop")
#        self.actionDelete = QtGui.QAction(MainWindow)
#        self.actionDelete.setObjectName("actionDelete")
        self.actionZoom_in = QtGui.QAction(MainWindow)
        self.actionZoom_in.setObjectName("actionZoom_in")
        self.actionZoom_out = QtGui.QAction(MainWindow)
        self.actionZoom_out.setObjectName("actionZoom_out")
  

        self.actionMinimize = QtGui.QAction(MainWindow)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionVersion = QtGui.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.actionAbout_us = QtGui.QAction(MainWindow)
        self.actionAbout_us.setObjectName("actionAbout_us")
        
     

        
        self.menuFile.addAction(self.actionProjectExport)
#        self.menuFile.addAction(self.actionProjectSave_as)
        self.menuFile.addAction(self.actionDownload)
        self.menuFile.addAction(self.actionExportPDF)
       
        self.menuMusic.addAction(self.actionPlay)
        self.menuMusic.addAction(self.actionPause)
        self.menuMusic.addAction(self.actionStop)
#        self.menuMusic.addAction(self.actionDelete)
        self.menuZoom.addAction(self.actionZoom_in)
        self.menuZoom.addAction(self.actionZoom_out)
     
        self.menuWindow.addAction(self.actionMinimize)
        self.menuInfo.addAction(self.actionVersion)
        self.menuInfo.addAction(self.actionAbout_us)
        self.menuInfo.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMusic.menuAction())
        self.menubar.addAction(self.menuZoom.menuAction())
   
        self.menubar.addAction(self.menuExtras.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.menubar.addAction(self.menuPFM_Advanced.menuAction())

        self.toolBar.addAction(self.actionProjectExport)
#        self.toolBar.addAction(self.actionProjectSave_as)
        self.toolBar.addAction(self.actionDownload)
        self.toolBar.addAction(self.actionExportPDF)
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.widget_wave.upAndDownWaveWidget.plotWidget.figure.signal.freshScreenTime.connect(self.widgetDatabase.fireworksA.getTime)
        self.widget_wave.upAndDownWaveWidget.plotWidget.figure.signal.freshScreenTime.connect(self.widgetDatabase.fireworksB.getTime)
        self.widget_wave.upAndDownWaveWidget.plotWidget.figure.signal.freshScreenTime.connect(self.widgetDatabase.fireworksC.getTime)
        self.widget_wave.upAndDownWaveWidget.plotWidget.figure.signal.freshScreenTime.connect(self.widgetDatabase.fireworksD.getTime)
        self.widget_wave.upAndDownWaveWidget.plotWidget.figure.signal.freshScreenTime.connect(self.widgetDatabase.combinationFireworks.getTime)
        self.widget_wave.upAndDownWaveWidget.plotWidget.figure.signal.freshScreenTime.connect(self.widgetDatabase.customFireworks.getTime)
#         self.widget_wave.upAndDownWaveWidget.upperPlotWidget.plotWidget.figure.signal.freshScreenTime.connect(self.widgetDatabase.fireworksA.getTime)
#         self.widget_wave.upAndDownWaveWidget.upperPlotWidget.plotWidget.figure.signal.freshScreenTime.connect(self.widgetDatabase.fireworksB.getTime)
#         self.widget_wave.upAndDownWaveWidget.upperPlotWidget.plotWidget.figure.signal.freshScreenTime.connect(self.widgetDatabase.fireworksC.getTime)
#         self.widget_wave.upAndDownWaveWidget.upperPlotWidget.plotWidget.figure.signal.freshScreenTime.connect(self.widgetDatabase.fireworksD.getTime)
#         self.widget_wave.upAndDownWaveWidget.upperPlotWidget.plotWidget.figure.signal.freshScreenTime.connect(self.widgetDatabase.combinationFireworks.getTime)
#         self.widget_wave.upAndDownWaveWidget.upperPlotWidget.plotWidget.figure.signal.freshScreenTime.connect(self.widgetDatabase.customFireworks.getTime)
        self.actionZoom_in.triggered.connect(self.widget_wave.upAndDownWaveWidget.plotWidget.figure.zoomIn)
        self.actionZoom_out.triggered.connect(self.widget_wave.upAndDownWaveWidget.plotWidget.figure.zoomOut)
        self.widgetDatabase.musicSignal.connect(self.widget_wave.getData)
        
        
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_wave.setTitle(QtGui.QApplication.translate("MainWindow", "Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "file", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMusic.setTitle(QtGui.QApplication.translate("MainWindow", "Music", None, QtGui.QApplication.UnicodeUTF8))
        self.menuZoom.setTitle(QtGui.QApplication.translate("MainWindow", "Zoom", None, QtGui.QApplication.UnicodeUTF8))
        
        
        self.menuExtras.setTitle(QtGui.QApplication.translate("MainWindow", "Extras", None, QtGui.QApplication.UnicodeUTF8))
        self.menuWindow.setTitle(QtGui.QApplication.translate("MainWindow", "Window", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInfo.setTitle(QtGui.QApplication.translate("MainWindow", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPFM_Advanced.setTitle(QtGui.QApplication.translate("MainWindow", "PFM Advanced", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProjectExport.setText(QtGui.QApplication.translate("MainWindow", "Export project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDownload.setText(QtGui.QApplication.translate("MainWindow", "Download to device", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportPDF.setText(QtGui.QApplication.translate("MainWindow", "Export PDF", None, QtGui.QApplication.UnicodeUTF8))
#        self.actionProjectSave_as.setText(QtGui.QApplication.translate("MainWindow", "project save as", None, QtGui.QApplication.UnicodeUTF8))
#        self.actionImport_music.setText(QtGui.QApplication.translate("MainWindow", "import music", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlay.setText(QtGui.QApplication.translate("MainWindow", "play", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPause.setText(QtGui.QApplication.translate("MainWindow", "pause", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop.setText(QtGui.QApplication.translate("MainWindow", "stop", None, QtGui.QApplication.UnicodeUTF8))
#        self.actionDelete.setText(QtGui.QApplication.translate("MainWindow", "delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_in.setText(QtGui.QApplication.translate("MainWindow", "zoom in", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_out.setText(QtGui.QApplication.translate("MainWindow", "zoom out", None, QtGui.QApplication.UnicodeUTF8))
  
        self.actionMinimize.setText(QtGui.QApplication.translate("MainWindow", "minimize", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVersion.setText(QtGui.QApplication.translate("MainWindow", "version", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_us.setText(QtGui.QApplication.translate("MainWindow", "help", None, QtGui.QApplication.UnicodeUTF8))
