#coding=utf-8
'''
Created on 2013-3-6

@author: pyroshow
'''

import sys, json
from PySide.QtGui import *
from PySide.QtCore import *
from Models.LocalDB import *

class CombinationDialog(QDialog):
    
    def __init__(self, Item, UUID, parent = None):
        QDialog.__init__(self, parent)
        self.IDLabel = QLabel("ID:")
        self.combinationLabel = QLabel("Combination:")
        self.Item = Item
        self.UUID = UUID

        self.IDCombo = QComboBox()
        self.IDCombo.addItems(['pyro-101', 'pyro-102', 'pyro-103', 'pyro-104'])
        
        self.view = QTableView()
        self.model = QStandardItemModel(1, 2, self)
        self.model.setHorizontalHeaderLabels (["Item", "Time"])
        
        self.model.setData(self.model.index(0, 0, QModelIndex()), self.Item)
        self.view.setModel (self.model)
        
        
        self.saveButton = QPushButton("Save")
        self.cancelButton = QPushButton("Cancel")
        
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.IDLabel)
        hbox1.addWidget(self.IDCombo)
        
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.saveButton)
        hbox2.addWidget(self.cancelButton)
        
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addWidget(self.combinationLabel)
        vbox.addWidget(self.view)
        vbox.addLayout(hbox2)
        self.setLayout(vbox)
        
        self.saveButton.clicked.connect(self.saveData)
        self.cancelButton.clicked.connect(self.cancel)
        
        #设置右键菜单
        self.view.setContextMenuPolicy(Qt.CustomContextMenu)
        #设置右键菜单函数
        self.view.customContextMenuRequested.connect(self.on_view_customContextMenuRequested)
        
        self.sess = session()
        
        
        
    #右键槽函数
    @Slot(QPoint)
    def on_view_customContextMenuRequested(self, point):
        #获取某行，某列
#        print self.view1.columnAt(point.x())
        #获得当前的选中行
        self.row = self.view.rowAt(point.y())
        rightMenu = QMenu(self)
        if self.row >= 0:
            deleteAction = QAction("Delete", self)
            deleteAction.setStatusTip("Delete selected line")
            deleteAction.connect(SIGNAL("triggered()"), self.delete)
            rightMenu.addAction(deleteAction)
            
            addLineAction = QAction("Add", self)
            addLineAction.setStatusTip("Insert a line below the selected line")
            addLineAction.connect(SIGNAL("triggered()"), self.add)
            rightMenu.addAction(addLineAction)
            
        rightMenu.exec_(QCursor.pos())
        
    #从View里面删除选中的行   
    def delete(self):
        self.model.takeRow(self.row)
        
        
    #在选中行的下面添加空白行 
    def add(self):
        item = QStandardItem()
        self.model.insertRow(self.row+1, item)
        
    def saveData(self):
        l = []
        for count in range(self.model.rowCount()):
            item0 = self.model.item(count, 0)
            item1 = self.model.item(count, 1)
            t = (item0.text(), item1.text())
            l.append(t)
        data = {self.IDCombo.currentText():l}
        d = json.dumps(data)
        with self.sess.begin():
            record = FireworksData()
            record.Name = self.IDCombo.currentText()
            record.Type = "Combination"
            record.Size = 0
            record.UUID = self.UUID+"C"
            record.Combination = d
            record.Perm = 0
            
            self.sess.add(record)

        self.IDCombo.setCurrentIndex(0)
        
        self.accept()
        
        self.close()
        
        
    def cancel(self):
        self.close()



