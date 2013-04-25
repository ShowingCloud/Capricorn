#coding=utf-8
'''
Created on 2013-3-6

@author: pyroshow
'''

from PySide.QtGui import *
from PySide.QtCore import *
from Delegate.scriptDelegate import ScriptDelegate

class Script(QWidget):
    
    def __init__(self, Type, parent = None):
        QWidget.__init__(self, parent)

        self.mainGroupBox = QGroupBox("Script")
        
        self.model = QStandardItemModel (0, 11, self)
        self.model.setHorizontalHeaderLabels (["UUID", "Name", "Alias", "Size", "Ignition Time", "Rising Time", "Effect Time", "Ignition ID", "Connector ID", "Information", "Notes"])
        
        self.view = QTableView(self)
        self.view.setAlternatingRowColors(True)
        self.view.setModel(self.model)
        self.view.setItemDelegate(ScriptDelegate(self))
        
        self.view.hideColumn(0)
        
        scriptLayout = QVBoxLayout()
        scriptLayout.addWidget(self.view)
        
        self.mainGroupBox.setLayout(scriptLayout)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.mainGroupBox)
        self.setLayout(mainLayout)
        self.resize(1500, 800)
        
        self.Type = Type



