#coding=utf-8
'''
Created on 2013-3-6

@author: pyroshow
'''

from PySide.QtGui import *
from PySide.QtCore import *
from UI import rc_picture


class TypeListWidget(QWidget):
    
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        
        self.listWidget = QListWidget()
        self.listWidget.setViewMode(QListView.IconMode)
        self.listWidget.setIconSize(QSize(96, 84))
        self.listWidget.setMovement(QListView.Static)
        self.listWidget.setMaximumWidth(150)
        self.listWidget.setSpacing(12)
        
        self.createIcons()
        
        layout = QHBoxLayout()
        layout.addWidget(self.listWidget)
        self.setLayout(layout)
        
    def createIcons(self):
        displayShellButton = QListWidgetItem(self.listWidget)
        displayShellButton.setIcon(QIcon(':/images/lihua.png'))
        displayShellButton.setText("Display Shell")
        displayShellButton.setTextAlignment(Qt.AlignHCenter)
        displayShellButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        
        samllFireworksButton = QListWidgetItem(self.listWidget)
        samllFireworksButton.setIcon(QIcon(':/images/xiaolihua.png'))
        samllFireworksButton.setText("Small Fireworks")
        samllFireworksButton.setTextAlignment(Qt.AlignHCenter)
        samllFireworksButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        
        rotatingLaunchButton = QListWidgetItem(self.listWidget)
        rotatingLaunchButton.setIcon(QIcon(':/images/xuanzhuan.png'))
        rotatingLaunchButton.setText("Rotating Launch")
        rotatingLaunchButton.setTextAlignment(Qt.AlignHCenter)
        rotatingLaunchButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        
        smokeFireworksButton = QListWidgetItem(self.listWidget)
        smokeFireworksButton.setIcon(QIcon(':/images/yanwu.png'))
        smokeFireworksButton.setText("Smoke Fireworks")
        smokeFireworksButton.setTextAlignment(Qt.AlignHCenter)
        smokeFireworksButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        
        combinationFireworksButton = QListWidgetItem(self.listWidget)
        combinationFireworksButton.setIcon(QIcon(':/images/zuhe.png'))
        combinationFireworksButton.setText("Group Fireworks")
        combinationFireworksButton.setTextAlignment(Qt.AlignHCenter)
        combinationFireworksButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        
        customFireworksButton = QListWidgetItem(self.listWidget)
        customFireworksButton.setIcon(QIcon(':/images/zidingyi.png'))
        customFireworksButton.setText("Custom Fireworks")
        customFireworksButton.setTextAlignment(Qt.AlignHCenter)
        customFireworksButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)




