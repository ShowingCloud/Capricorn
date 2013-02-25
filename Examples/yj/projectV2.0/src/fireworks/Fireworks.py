#coding=utf-8
'''
Created on 2013-2-22

@author: pyroshow
'''

from PySide.QtGui import *
from PySide.QtCore import *
from popupWindow.uiInputDialog import *
from toolKit.mergeDelegate import *
from alchemy.AlchemyOpereation import *
from popupWindow.uiCombinationDialog import CombinationDialog

class Fireworks(QWidget):
    
    def __init__(self, Type, parent = None):
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
        self.view.setItemDelegate(MergeDelegate(self))
        self.view.setModel(self.model)
        self.view.resize(960, 300)
        
        self.sess = session()
        base.metadata.create_all(engine)
        self.Type = Type
        self.query(Type)
        
        self.headView = self.view.horizontalHeader()
        self.headView.sectionClicked.connect(self.ascendingSort)
        self.headView.sectionDoubleClicked.connect(self.descendingSort)
        
        #设置右键菜单
        self.view.setContextMenuPolicy(Qt.CustomContextMenu)
        #设置右键菜单函数
        self.view.customContextMenuRequested.connect(self.on_view_customContextMenuRequested)
    #右键菜单函数
    @Slot(QPoint)    
    def on_view_customContextMenuRequested(self, point):
        
        #获得当前的选中列
        self.column = self.view.columnAt(point.x())
        self.row = self.view.rowAt(point.y())
        rightMenu = QMenu(self)
        insertDataAction = QAction("Insert", self)
        insertDataAction.setStatusTip("Insert the fireworks info into  database")
        insertDataAction.connect(SIGNAL("triggered()"), self.insert)
        rightMenu.addAction(insertDataAction)
        if self.row >= 0:
            addEditAction = QAction("Add", self)
            addEditAction.setStatusTip("Add  fireworks to the script")
            addEditAction.connect(SIGNAL("triggered()"), self.addCombinationFireworks)
            rightMenu.addAction(addEditAction)
        
        
        rightMenu.exec_(QCursor.pos())
        
    def query(self, Type):
        with self.sess.begin():
            record = self.sess.query (Data).all()
            
            for row in record:
                newrow = []
                if row.Type == Type :
                    newrow.append (QStandardItem (row.Item))
                    newrow.append (QStandardItem (row.Description))
                    newrow.append (QStandardItem (str(row.Size)))
                    newrow.append (QStandardItem (str(row.Stock)))
                    newrow.append (QStandardItem (str(row.Used_Effects)))
                    newrow.append (QStandardItem (str(row.Rising_Time)))
                    newrow.append (QStandardItem (row.Effect))
                    newrow.append (QStandardItem (str(row.Color)))
                    newrow.append (QStandardItem (str(row.Angle)))
                
                    #为model添加行数据
                    self.model.appendRow (newrow)
                
                  
    def insert(self):
        insertDialog = InsertDialog(self)
        accept = insertDialog.exec_()
        if accept == 1:
            self.model.clear()
            self.model.setHorizontalHeaderLabels (["Item", "Description", "Size", "Stock", "Used Effects", "Rising Time", "Effect", "Color", "Angel"])
            self.query(self.Type)
        
    @Slot(int)
    def ascendingSort(self, index):
        self.model.sort(index, Qt.AscendingOrder)
        
    @Slot(int)
    def descendingSort(self, index):
        self.model.sort(index, Qt.DescendingOrder)
        
    def addCombinationFireworks(self):
        item = self.model.item(self.row)
        combinationDialog = CombinationDialog(item.text(), self)
        combinationDialog.show()
        
        
        
        
        