#coding=utf-8
'''
Created on 2013-3-6

@author: pyroshow
'''

from PySide.QtGui import *
from PySide.QtCore import *
from Delegate.combinationDelegate import CombinationDelegate
from Models.LocalDB import *
import json


class Combination(QWidget):

    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        
        self.sourceGroupBox = QGroupBox("Combination")
        self.view = QTableView(self)
        self.view.setAutoScroll(True)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.view.setSelectionMode(QAbstractItemView.SingleSelection)
        #设置交互颜色
        self.view.setAlternatingRowColors (True)
        #行和列显示都按内容来
        self.view.resizeColumnsToContents()
        self.view.resizeRowsToContents()
        self.model = QStandardItemModel (0, 1, self)
        self.model.setHorizontalHeaderLabels(["UUID", "ID", "Combination Info(Item/Time)"])
        
        self.sess = session()
        base.metadata.create_all(engine)
        self.query()
        self.view.setItemDelegate(CombinationDelegate(self))   
        self.view.setModel(self.model)
        self.view.hideColumn(0)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.view)
        
        self.sourceGroupBox.setLayout(vbox)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.sourceGroupBox)
        
        self.setLayout(mainLayout)
        
        self.resize(1060, 500)
        
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
        refreshAction = QAction("Refresh", self)
        refreshAction.setStatusTip("Refresh the fireworks from  database")
        refreshAction.connect(SIGNAL("triggered()"), self.refresh)
        rightMenu.addAction(refreshAction)
        rightMenu.exec_(QCursor.pos())
        
    def query(self):
        with self.sess.begin():
            
            record = self.sess.query (FireworksData).filter_by(Type = 'Combination').all()
            for row in record:
                newrow = []
                info = json.loads(row.Combination)
                k = info.keys()
                newrow.append (QStandardItem (str(row.UUID)))
                newrow.append (QStandardItem (k[0]))
                newrow.append (QStandardItem (str(info[k[0]])))
                
                #为model添加行数据
                self.model.appendRow (newrow)
                
    def refresh(self):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["UUId", "ID", "Combination Info(Item/Time)"])
        self.query()
        self.view.hideColumn(0)



