#coding=utf-8
'''
Created on 2013-2-20

@author: pyroshow
'''
from PySide.QtCore import *
from PySide.QtGui import *
import sys

class InsertDialog(QDialog):
    
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.FireworkIDLabel = QLabel("FireworkID:")
        self.IgnitorIDLabel = QLabel("IgnitorID:")
        self.ConnectorIDLabel = QLabel("ConnectorID:")
        self.DurationLabel = QLabel("Duration:")
        self.InventoryLabel = QLabel("Inventory:")
        self.ColorLabel = QLabel("Color:")
        self.AngleLabel = QLabel("Angle:")

        self.FireworkIDEidt = QLineEdit()
        self.IgnitorIDEidt = QLineEdit()
        self.ConnectorIDEidt = QLineEdit()
        self.DurationEidt = QLineEdit()
        self.InventoryEidt = QLineEdit()
        self.ColorEidt = QLineEdit()
        self.AngleEidt = QLineEdit()
        
        self.saveButton = QPushButton("Save")
        self.cancelButton = QPushButton("Cancel")
        
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.saveButton)
        self.hbox.addWidget(self.cancelButton)
        
        self.layout = QGridLayout()
        self.layout.addWidget(self.FireworkIDLabel, 0, 0)
        self.layout.addWidget(self.FireworkIDEidt, 0, 1)
        self.layout.addWidget(self.IgnitorIDLabel, 1, 0)
        self.layout.addWidget(self.IgnitorIDEidt, 1, 1)
        self.layout.addWidget(self.ConnectorIDLabel, 2, 0)
        self.layout.addWidget(self.ConnectorIDEidt, 2, 1)
        self.layout.addWidget(self.DurationLabel, 3, 0)
        self.layout.addWidget(self.DurationEidt, 3, 1)
        self.layout.addWidget(self.InventoryLabel, 4, 0)
        self.layout.addWidget(self.InventoryEidt, 4, 1)
        self.layout.addWidget(self.ColorLabel, 5, 0)
        self.layout.addWidget(self.ColorEidt, 5, 1)
        self.layout.addWidget(self.AngleLabel, 6, 0)
        self.layout.addWidget(self.AngleEidt, 6, 1)
        self.layout.addLayout(self.hbox, 8, 0, 1, 2)
        self.setLayout(self.layout)
        
        
        
        
app = QApplication(sys.argv)
demo = InsertDialog()
demo.show()
app.exec_()
