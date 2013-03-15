#coding=utf-8
'''
Created on 2013-3-15

@author: pyroshow
'''
from Delegate.fieldDelegate import FieldDelegate
from Models.EngineeringDB import *
from PySide.QtCore import *
from PySide.QtGui import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from UI.ui_fieldDatabase import FieldDatabase


class FieldDirectory(QWidget):    
    def __init__(self,  parent = None):
        QWidget.__init__(self, parent)
        
        self.groupDir = QGroupBox("FieldList:")
        
        self.view = QTreeView(self)
        self.view.setRootIsDecorated(False)
        self.view.setAlternatingRowColors(True)
        
        self.model = QStandardItemModel (0, 1, self)
        self.model.setHorizontalHeaderLabels (["UUID", "FieldID"])
        self.view.setModel(self.model)
        self.view.setItemDelegate(FieldDelegate())
        self.view.hideColumn(0)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.view)
        
        self.groupDir.setLayout(vbox)
        
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.groupDir)
        self.setLayout(mainLayout)
        self.view.setMaximumWidth(120)
        
        self.engine = create_engine("sqlite:///engineering.db")
        self.session = scoped_session(sessionmaker(bind = self.engine, autocommit= True))
        base1.metadata.create_all(self.engine)
        
        #设置右键菜单
        self.view.setContextMenuPolicy(Qt.CustomContextMenu)
        #设置右键菜单函数
        self.view.customContextMenuRequested.connect(self.on_view_customContextMenuRequested)
        
        self.query()
        
        
    def query(self):
        with self.session.begin():
            record = self.session.query (FieldsData).all()
            
            for row in record:
                newrow = []
                newrow.append (QStandardItem (row.UUID))
                newrow.append (QStandardItem (row.FieldID))
                
                self.model.appendRow (newrow)
                
        #右键槽函数
    @Slot(QPoint)
    def on_view_customContextMenuRequested(self, point):
        #获取某行，某列
#        print self.view1.columnAt(point.x())
        #获得当前的选中行
#        self.row = self.view.rowAt(point.y())
        rightMenu = QMenu(self)
        addAction = QAction("Add field", self)
        addAction.setStatusTip("Add a field to  database")
        addAction.connect(SIGNAL("triggered()"), self.addField)
        rightMenu.addAction(addAction)
            
        rightMenu.exec_(QCursor.pos())
        
    def addField(self):
        field = FieldDatabase()
        accept = field.exec_()
        if accept == 1:
            self.model.clear()
            self.model.setHorizontalHeaderLabels(["UUID", "FieldID"])
            self.query()
            self.view.hideColumn(0)




