# -*- coding:utf8 -*-
from PySide.QtCore import *
from PySide.QtGui import *
import MenuResources_rc

class HelpForm(QDialog):
    
    def __init__(self,  page,  parent = None):
        super(HelpForm,  self).__init__(parent)
        
        self.textBrowser = QTextBrowser()
        backAction = QAction(QIcon("images/back.png"), "&Back", self)
        backAction.setShortcut(QKeySequence.Back)
        homeAction = QAction(QIcon("images/home.png"), "&Home", self)
        homeAction.setShortcut("Home")
        self.pageLabel = QLabel('i am pagelabel')
        
        toolBar = QToolBar()
        toolBar.addAction(backAction)
        toolBar.addAction(homeAction)
        toolBar.addWidget(self.pageLabel)
        
        layout = QVBoxLayout()
        layout.addWidget(toolBar)
        layout.addWidget(self.textBrowser, 0)
        self.setLayout(layout)
        
        
        self.connect(backAction, SIGNAL("triggered()"),
                     self.textBrowser, SLOT("backward()"))
        self.connect(homeAction, SIGNAL("triggered()"),
                     self.textBrowser, SLOT("home()"))
        self.connect(self.textBrowser, SIGNAL("sourceChanged(QUrl)"),
                     self.updatePageTitle)
                     
        self.textBrowser.setSearchPaths(["help"])
        self.textBrowser.setSource(QUrl(page))
        self.resize(400, 600)
        self.setWindowTitle("HelpForm")
    def updatePageTitle(self):
        self.pageLabel.setText(self.textBrowser.documentTitle())
        
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = HelpForm("index.html")
    form.show()
    app.exec_()
