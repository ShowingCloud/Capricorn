#coding=utf-8
'''
Created on 2013-2-5

@author: pyroshow
'''

import sys, rc_picture
from PySide.QtGui import *
from PySide.QtCore import *

class MainWindow(QMainWindow):
    
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        
        self.setWindowTitle(u"打印图片")
        self.setWindowIcon(QIcon(":/images/title.png"))
        
        self.imageLabel = QLabel()
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored) 
        self.setCentralWidget(self.imageLabel)
        
        self.image = QImage()
        
        self.createActions()
        self.createMenus()
        self.createToolBars()
        
        if self.image.load(":/images/girl.jpg"):
            self.imageLabel.setPixmap(QPixmap.fromImage(self.image))
            self.resize(self.image.width(), self.image.height())
            
    def createActions(self):
        self.printAction = QAction(QIcon(":/images/print.png"), u"打印", self)
        self.printAction.setShortcut("Ctrl+P")
        self.printAction.setStatusTip(u"打印")
        self.connect(self.printAction, SIGNAL("triggered()"), self.printSlot)
        
    def createMenus(self):
        printMenu = self.menuBar().addMenu(u"打印")
        printMenu.addAction(self.printAction)
        
    def createToolBars(self):
        fileToolBar = self.addToolBar('Print')
        fileToolBar.addAction(self.printAction)
        
    def printSlot(self):
        printer = QPrinter()
        printDialog = QPrintDialog(printer, self)
        
        if printDialog.exec_():
            painter = QPainter(printer)
            rect = painter.viewport()
            size = self.image.size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(),rect.y(),size.width(),size.height()) 
            painter.setWindow(self.image.rect())
            painter.drawImage(0,0,self.image)
            

app = QApplication(sys.argv)
mw = MainWindow()
mw.show()
sys.exit(app.exec_())





