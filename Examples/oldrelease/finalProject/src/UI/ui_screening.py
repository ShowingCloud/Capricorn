#coding=utf-8
'''
Created on 2013-3-6

@author: pyroshow
'''

from PySide.QtGui import QWidget, QGroupBox, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout

class ScreeningWidget(QWidget):
    
    def __init__(self, parent = None):
        
        QWidget.__init__(self, parent)
        
        self.groupButton = QGroupBox("Screening:")
        
        self.filterPatternLineEdit = QLineEdit()
        self.filterPatternLineEdit.setText("")
        self.filterPatternLabel = QLabel("&Filter pattern:")
        self.filterPatternLabel.setBuddy(self.filterPatternLineEdit)
        tabLayout = QHBoxLayout()
        tabLayout.addStretch(1)
        tabLayout.addWidget(self.filterPatternLabel)
        tabLayout.addWidget(self.filterPatternLineEdit)
        
        
        self.groupButton.setLayout(tabLayout)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.groupButton)
        self.setLayout(mainLayout)
        self.setMaximumWidth(270)


