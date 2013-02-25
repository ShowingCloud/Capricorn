#coding=utf-8
'''
Created on 2013-2-22

@author: pyroshow
'''

from PySide.QtGui import *
from PySide.QtCore import *
from popupWindow.uiInputDialog import *
from toolKit.customDelegate import CustomDelegate


class Script(QWidget):

    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.view = QTableView(self)
        self.view.setAutoScroll(False)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.view.setSelectionMode(QAbstractItemView.SingleSelection)
        #设置交互颜色
        self.view.setAlternatingRowColors (True)
        #行和列显示都按内容来
        self.view.resizeColumnsToContents()
        self.view.resizeRowsToContents()
        
        self.model = QStandardItemModel (0, 9, self)
        self.model.setHorizontalHeaderLabels (["Item", "Description", "Size", "Stock", "Used Effects", "Rising Time", "Effect", "Color", "Angel"])
        self.view.setModel (self.model)
        self.view.setItemDelegate(CustomDelegate(self))
        self.view.setModel(self.model)
        self.view.resize(960, 300)
        self.sess = session()
        self.query()
        
#        #设置右键菜单
#        self.view.setContextMenuPolicy(Qt.CustomContextMenu)
#        #设置右键菜单函数
#        self.view.customContextMenuRequested.connect(self.on_view_customContextMenuRequested)
#    #右键菜单函数
#    @Slot(QPoint)    
#    def on_view_customContextMenuRequested(self, point):
#        
#        rightMenu = QMenu(self)
#        insertDataAction = QAction("Insert", self)
#        insertDataAction.setStatusTip("Insert a line below the selected line")
#        insertDataAction.connect(SIGNAL("triggered()"), self.add)
#        rightMenu.addAction(insertDataAction)
#        rightMenu.exec_(QCursor.pos())
#        
#    def add(self):
#        insertDialog = InsertDialog(self)
#        insertDialog.show()
        
        
        
        
        
        
    def query(self):
        with self.sess.begin():
            record = self.sess.query (Data1).all()
            
            for row in record:
                newrow = []
                newrow.append (QStandardItem (row.Item))
                newrow.append (QStandardItem (row.Description))
                newrow.append (QStandardItem (str(row.Size)))
                newrow.append (QStandardItem (str(row.Stock)))
                newrow.append (QStandardItem (str(row.Used_Effects)))
                newrow.append (QStandardItem (str(row.Rising_Time)))
                newrow.append (QStandardItem (row.Effect))
                newrow.append (QStandardItem (row.Color))
                newrow.append (QStandardItem (row.Angle))
                
                #为model添加行数据
                self.model.appendRow (newrow)