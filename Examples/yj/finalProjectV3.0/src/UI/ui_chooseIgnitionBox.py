#coding=utf-8
'''
Created on 2013-3-13

@author: pyroshow
'''

from Delegate.ignitionBoxDelegate import CheckBoxDelegate
from Models.EngineeringDB import *
from PySide.QtCore import *
from PySide.QtGui import *
from UI.ui_ignitionBoxDatabase import IgnitionBoxDatabase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session




class IgnitionBox(QDialog):
    
    def __init__(self, UUID, FieldID, parent = None):
        
        QDialog.__init__(self, parent)
        
        self.groupBox = QGroupBox("Choose Ignition Box:")
        self.view = QTableView(self)
        self.view.setAlternatingRowColors(True)
        self.model = QStandardItemModel(0, 7, self)
        self.model.setHorizontalHeaderLabels(["UUID", "IgnitorID", "FieldID", "BoxID", "Total Heads", "Surplus Heads", "Choose", "Notes"])
        self.view.setModel(self.model)
        self.view.setMinimumWidth(self.view.horizontalHeader().length())
        self.view.setItemDelegateForColumn(6, CheckBoxDelegate(self))
        self.view.hideColumn(0)
        self.view.hideColumn(1)
        
        
        self.okBtn = QPushButton("OK")
        self.cancelBtn = QPushButton("Cancel")
        
        btnLayout = QHBoxLayout()
        #可伸缩的
        btnLayout.addStretch(1)
        btnLayout.addWidget(self.okBtn)
        btnLayout.addWidget(self.cancelBtn)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.view)
        vbox.addLayout(btnLayout)
        
        self.groupBox.setLayout(vbox)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.groupBox)
        self.setLayout(mainLayout)
        
        self.engine = create_engine("sqlite:///engineering.db")
        self.session = scoped_session(sessionmaker(bind = self.engine, autocommit= True))
        self.UUID = UUID
        self.FieldID = FieldID
        self.query()
        
        self.okBtn.clicked.connect(self.confirm)
        self.cancelBtn.clicked.connect(self.cancel)
        
        #设置右键菜单
        self.view.setContextMenuPolicy(Qt.CustomContextMenu)
        #设置右键菜单函数
        self.view.customContextMenuRequested.connect(self.on_view_customContextMenuRequested)
        
        
        #右键槽函数
    @Slot(QPoint)
    def on_view_customContextMenuRequested(self, point):
        #获取某行，某列
#        print self.view1.columnAt(point.x())
        #获得当前的选中行
        self.row = self.view.rowAt(point.y())
        rightMenu = QMenu(self)
        addAction = QAction("Add ignition box", self)
        addAction.setStatusTip("add a  ignition box")
        addAction.connect(SIGNAL("triggered()"), self.addIgnitionBox)
        rightMenu.addAction(addAction)
        if self.row >= 0:
            deleteAction = QAction("Delete", self)
            deleteAction.setStatusTip("Delete selected line")
            deleteAction.connect(SIGNAL("triggered()"), self.delete)
            rightMenu.addAction(deleteAction)
            
        rightMenu.exec_(QCursor.pos())
        
    #从View里面删除选中的行   
    def delete(self):
        item1 = self.model.item(self.row)
        with self.session.begin():
            record = self.session.query (IgnitorsData).filter_by(UUID = item1.text()).first()
            #删除表格里面数据
            self.model.takeRow(self.row)
            #删除数据库里面的数据
            self.session.delete(record)
            
    def addIgnitionBox(self):
        ignitionBoxDatabase = IgnitionBoxDatabase(self.FieldID, self)
        
        accept = ignitionBoxDatabase.exec_()
        if accept == 1:
            self.model.clear()
            self.model.setHorizontalHeaderLabels(["UUID", "IgnitorID", "FieldID", "BoxID", "Total Heads", "Surplus Heads", "Choose", "Notes"])
            self.query()
            self.view.hideColumn(0)
            self.view.hideColumn(1)
        
        
    def query(self):
        
        with self.session.begin():
            
            record = self.session.query(IgnitorsData).filter_by(FieldID = self.FieldID).all()
            
            for row in record:
                newRow = []
                newRow.append (QStandardItem (row.UUID))
                newRow.append (QStandardItem (str(row.IgnitorID)))
                newRow.append (QStandardItem (str(row.FieldID)))
                newRow.append (QStandardItem (str(row.BoxID)))
                newRow.append (QStandardItem (str(row.TotalHeads)))
                newRow.append (QStandardItem (str(row.SurplusHeads)))
                newRow.append (QStandardItem ("0"))
                newRow.append (QStandardItem (row.Notes))
                
                self.model.appendRow(newRow)
                
    def confirm(self):
        
        count = self.model.rowCount()
        UUID = []
#        k = 0
        for i in range(count) :
            if self.model.item(i, 6).text() == "1":
                
                UUID.append(self.model.item(i, 0).text())
#                k = i
        if len(UUID) > 1:
                QMessageBox.information(self, "Information", " Can only choose <b> One </b> ignition box!!!")
        elif len(UUID) == 0:
                QMessageBox.information(self, "Information", " You must choose <b> One </b> ignition box!!!")
        else:
            with self.session.begin():
                data = self.session.query(IgnitorsData).filter_by(UUID = UUID[0]).first()
                other = self.session.query (ScriptData).filter_by(UUID = self.UUID).first()
                other.IgnitorID = data.UUID
                data.SurplusHeads -= 1
                
#                if data.SurplusHeads == 0:
#                    index = self.model.index(k, 6)
#                    self.model.setData(index, "2", Qt.EditRole)
#                else:
#                    other.IgnitorID = data.UUID
#                    data.SurplusHeads = 0
                    
                
            self.close()
        
                
    def cancel(self):
        self.close()
        
        
        
        
        
        

