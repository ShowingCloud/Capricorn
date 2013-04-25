#coding=utf-8
'''
Created on 2013-3-6

@author: pyroshow
'''

from PySide.QtGui import *
from PySide.QtCore import *
from UI import rc_picture


class FieldListWidget(QWidget):
    
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        
        self.listWidget = QListWidget()
        self.listWidget.setViewMode(QListView.IconMode)
        self.listWidget.setIconSize(QSize(96, 96))
        self.listWidget.setMovement(QListView.Static)
        self.listWidget.setMaximumWidth(150)
        self.listWidget.setSpacing(12)
        
        self.createIcons()
        
        layout = QHBoxLayout()
        layout.addWidget(self.listWidget)
        self.setLayout(layout)
        
    def createIcons(self):
        displayShellButton = QListWidgetItem(self.listWidget)
        displayShellButton.setIcon(QIcon(':/images/side1.png'))
        displayShellButton.setText("Field First")
        displayShellButton.setTextAlignment(Qt.AlignHCenter)
        displayShellButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        
        samllFireworksButton = QListWidgetItem(self.listWidget)
        samllFireworksButton.setIcon(QIcon(':/images/side2.png'))
        samllFireworksButton.setText("Field Second")
        samllFireworksButton.setTextAlignment(Qt.AlignHCenter)
        samllFireworksButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        
        rotatingLaunchButton = QListWidgetItem(self.listWidget)
        rotatingLaunchButton.setIcon(QIcon(':/images/side3.png'))
        rotatingLaunchButton.setText("Field Third")
        rotatingLaunchButton.setTextAlignment(Qt.AlignHCenter)
        rotatingLaunchButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        
        smokeFireworksButton = QListWidgetItem(self.listWidget)
        smokeFireworksButton.setIcon(QIcon(':/images/side4.png'))
        smokeFireworksButton.setText("Field Four")
        smokeFireworksButton.setTextAlignment(Qt.AlignHCenter)
        smokeFireworksButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        
        combinationFireworksButton = QListWidgetItem(self.listWidget)
        combinationFireworksButton.setIcon(QIcon(':/images/side5.png'))
        combinationFireworksButton.setText("Field Five")
        combinationFireworksButton.setTextAlignment(Qt.AlignHCenter)
        combinationFireworksButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        
        customFireworksButton = QListWidgetItem(self.listWidget)
        customFireworksButton.setIcon(QIcon(':/images/side6.png'))
        customFireworksButton.setText("Field Six")
        customFireworksButton.setTextAlignment(Qt.AlignHCenter)
        customFireworksButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
