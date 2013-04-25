#coding=utf-8
'''
Created on 2013-3-6

@author: pyroshow
'''

from PySide.QtGui import QWidget,QGroupBox,QRadioButton,QHBoxLayout,QButtonGroup,QVBoxLayout

class ChooseSizeWidget(QWidget):
    
    def __init__(self, parent = None):
        
        QWidget.__init__(self, parent)
        
        self.groupButton = QGroupBox("Choose Size:")
        
        self.sizeGroup = QButtonGroup()
        self.button1 = QRadioButton("5", self)
        self.button2 = QRadioButton("10", self)
        self.button3 = QRadioButton("15", self)
        self.button4 = QRadioButton("20", self)
        self.button5 = QRadioButton("25", self)
        self.button6 = QRadioButton("All", self)
        self.sizeGroup.addButton(self.button1)
        self.sizeGroup.addButton(self.button2)
        self.sizeGroup.addButton(self.button3)
        self.sizeGroup.addButton(self.button4)
        self.sizeGroup.addButton(self.button5)
        self.sizeGroup.addButton(self.button6)
        
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        layout.addWidget(self.button6)
        self.groupButton.setLayout(layout)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.groupButton)
        self.setLayout(mainLayout)
        self.setMaximumWidth(270)

