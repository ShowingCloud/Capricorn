# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\python_work\show_1\menu.ui'
#
# Created: Tue Jan 29 13:47:47 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1009, 563)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.textEdit = QtGui.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 30, 881, 171))
        self.textEdit.setObjectName("textEdit")
        self.sub_widget = QtGui.QWidget(self.centralWidget)
        self.sub_widget.setGeometry(QtCore.QRect(0, 210, 881, 151))
        self.sub_widget.setObjectName("sub_widget")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1009, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu_File = QtGui.QMenu(self.menuBar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Music = QtGui.QMenu(self.menuBar)
        self.menu_Music.setObjectName("menu_Music")
        self.menu_Zoom = QtGui.QMenu(self.menuBar)
        self.menu_Zoom.setObjectName("menu_Zoom")
        self.menuInfo = QtGui.QMenu(self.menuBar)
        self.menuInfo.setObjectName("menuInfo")
        self.menu_Database = QtGui.QMenu(self.menuBar)
        self.menu_Database.setObjectName("menu_Database")
        self.menu_Script = QtGui.QMenu(self.menuBar)
        self.menu_Script.setObjectName("menu_Script")
        self.menu_Advanced = QtGui.QMenu(self.menuBar)
        self.menu_Advanced.setObjectName("menu_Advanced")
        MainWindow.setMenuBar(self.menuBar)
        self.action_Open = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/fileopen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Open.setIcon(icon)
        self.action_Open.setObjectName("action_Open")
        self.action_Save = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/filesave.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Save.setIcon(icon1)
        self.action_Save.setObjectName("action_Save")
        self.action_Save_as = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/images/filesaveas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Save_as.setIcon(icon2)
        self.action_Save_as.setObjectName("action_Save_as")
        self.action_About = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_About.setIcon(icon3)
        self.action_About.setObjectName("action_About")
        self.action_Documentation = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/images/blender.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Documentation.setIcon(icon4)
        self.action_Documentation.setObjectName("action_Documentation")
        self.action_Exit = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/images/x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Exit.setIcon(icon5)
        self.action_Exit.setObjectName("action_Exit")
        self.action_Paste = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/images/vnc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Paste.setIcon(icon6)
        self.action_Paste.setObjectName("action_Paste")
        self.action_Copy = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/images/gv.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Copy.setIcon(icon7)
        self.action_Copy.setObjectName("action_Copy")
        self.action_Cut = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/images/editmirror.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Cut.setIcon(icon8)
        self.action_Cut.setObjectName("action_Cut")
        self.action_Properties = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/images/editmirrorhoriz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Properties.setIcon(icon9)
        self.action_Properties.setObjectName("action_Properties")
        self.action_Print = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/images/clock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Print.setIcon(icon10)
        self.action_Print.setObjectName("action_Print")
        self.action_Image = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/images/emacs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Image.setIcon(icon11)
        self.action_Image.setObjectName("action_Image")
        self.action_Undo = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/images/images/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Undo.setIcon(icon12)
        self.action_Undo.setObjectName("action_Undo")
        self.action_Redo = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/images/images/usb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Redo.setIcon(icon13)
        self.action_Redo.setObjectName("action_Redo")
        self.action_ImageWindow = QtGui.QAction(MainWindow)
        self.action_ImageWindow.setObjectName("action_ImageWindow")
        self.action_Config = QtGui.QAction(MainWindow)
        self.action_Config.setObjectName("action_Config")
        self.action_SetLayout = QtGui.QAction(MainWindow)
        self.action_SetLayout.setObjectName("action_SetLayout")
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.action_Save_as)
        self.menu_File.addAction(self.action_Copy)
        self.menu_File.addAction(self.action_Cut)
        self.menu_File.addAction(self.action_Paste)
        self.menu_File.addAction(self.action_Exit)
        self.menu_File.addAction(self.action_Print)
        self.menu_File.addAction(self.action_Undo)
        self.menu_File.addAction(self.action_Redo)
        self.menuInfo.addAction(self.action_About)
        self.menuInfo.addAction(self.action_Documentation)
        self.menu_Advanced.addAction(self.action_Properties)
        self.menu_Advanced.addAction(self.action_Image)
        self.menu_Advanced.addAction(self.action_ImageWindow)
        self.menu_Advanced.addAction(self.action_Config)
        self.menu_Advanced.addAction(self.action_SetLayout)
        self.menuBar.addAction(self.menu_File.menuAction())
        self.menuBar.addAction(self.menu_Music.menuAction())
        self.menuBar.addAction(self.menu_Zoom.menuAction())
        self.menuBar.addAction(self.menu_Database.menuAction())
        self.menuBar.addAction(self.menu_Script.menuAction())
        self.menuBar.addAction(self.menu_Advanced.menuAction())
        self.menuBar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Music.setTitle(QtGui.QApplication.translate("MainWindow", "&Music", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Zoom.setTitle(QtGui.QApplication.translate("MainWindow", "&Zoom", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInfo.setTitle(QtGui.QApplication.translate("MainWindow", "&Info", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Database.setTitle(QtGui.QApplication.translate("MainWindow", "&Database", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Script.setTitle(QtGui.QApplication.translate("MainWindow", "&Script", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Advanced.setTitle(QtGui.QApplication.translate("MainWindow", "&Advanced", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save_as.setText(QtGui.QApplication.translate("MainWindow", "&Save as", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save_as.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setShortcut(QtGui.QApplication.translate("MainWindow", "F1", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Documentation.setText(QtGui.QApplication.translate("MainWindow", "&Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Exit.setText(QtGui.QApplication.translate("MainWindow", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Exit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setText(QtGui.QApplication.translate("MainWindow", "&Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setText(QtGui.QApplication.translate("MainWindow", "&Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Properties.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Print.setText(QtGui.QApplication.translate("MainWindow", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Image.setText(QtGui.QApplication.translate("MainWindow", "Image", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Undo.setText(QtGui.QApplication.translate("MainWindow", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Redo.setText(QtGui.QApplication.translate("MainWindow", "Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ImageWindow.setText(QtGui.QApplication.translate("MainWindow", "ImageWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Config.setText(QtGui.QApplication.translate("MainWindow", "Config", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SetLayout.setText(QtGui.QApplication.translate("MainWindow", "setLayout", None, QtGui.QApplication.UnicodeUTF8))

import MenuResources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

