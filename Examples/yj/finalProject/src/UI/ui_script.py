#coding=utf-8
'''
Created on 2013-3-6

@author: pyroshow
'''

from PySide.QtGui import *
from PySide.QtCore import *
from Delegate.scriptDelegate import ScriptDelegate

from Models.EngineeringDB import *
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

from Models.LocalDB import *
from datetime import datetime


class Script(QWidget):
    
    def __init__(self, Type, parent = None):
        QWidget.__init__(self, parent)

        self.mainGroupBox = QGroupBox("Script")
        
        self.model = QStandardItemModel (0, 12, self)
        self.model.setHorizontalHeaderLabels (["UUID", "Name", "Alias", "Size", "Ignition Time", "Rising Time(s)", "Effect Time", "Ignition ID", "Connector ID", "Tilt Angle", "Information", "Notes"])
        
        self.view = QTableView(self)
        self.view.setAlternatingRowColors(True)
        self.view.setModel(self.model)
        self.view.setItemDelegate(ScriptDelegate(self))
        
        self.view.hideColumn(0)
        
        scriptLayout = QVBoxLayout()
        scriptLayout.addWidget(self.view)
        
        self.mainGroupBox.setLayout(scriptLayout)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.mainGroupBox)
        self.setLayout(mainLayout)
        self.resize(1500, 800)
        
        self.Type = Type
        
        self.engine = create_engine("sqlite:///engineering.db")
        self.session = scoped_session(sessionmaker(bind = self.engine, autocommit= True))
        base1.metadata.create_all(self.engine)
        
        self.sess = session()
        self.query(self.Type)
        
        #设置右键菜单
        self.view.setContextMenuPolicy(Qt.CustomContextMenu)
        #设置右键菜单函数
        self.view.customContextMenuRequested.connect(self.on_view_customContextMenuRequested)
        
        
    def query(self, Type):
        with self.session.begin():
            record = self.session.query (ScriptData).filter_by(FieldID = Type).all()
            
            for row in record:
                newrow = []
                newrow.append (QStandardItem (row.UUID))
                UUID = row.FireworkID
                time = None
                infor = None
                with self.sess.begin():
                    data = self.sess.query (FireworksData).filter_by(UUID = UUID).first()
                    newrow.append (QStandardItem (data.Name))
                    newrow.append (QStandardItem (data.Alias))
                    newrow.append (QStandardItem(str(data.Size)))
                    time = data.RisingTime
                    infor = data.Information
                ignitionTime = row.IgnitionTime
                otherSecond = ignitionTime.second + time
                effectTime = None
                if otherSecond < 60 :
                    effectTime = str(ignitionTime.year)+"-"+str(ignitionTime.month)+"-"+str(ignitionTime.day)+" "+str(ignitionTime.hour)+":"+str(ignitionTime.minute)+":"+str(otherSecond)+"."+str(ignitionTime.microsecond)
                elif otherSecond >= 60:
                    effectTime = str(ignitionTime.year)+"-"+str(ignitionTime.month)+"-"+str(ignitionTime.day)+" "+str(ignitionTime.hour)+":"+str(ignitionTime.minute+1)+":"+str(otherSecond-60)+"."+str(ignitionTime.microsecond)
                newrow.append (QStandardItem (str(ignitionTime)))
                newrow.append (QStandardItem (str(time)))
                newrow.append (QStandardItem (effectTime))
                newrow.append (QStandardItem (row.IgnitorID))
                newrow.append (QStandardItem (str(row.ConnectorID)))
                newrow.append (QStandardItem (str(row.Angle)))
                newrow.append (QStandardItem (infor))
                newrow.append (QStandardItem (row.Notes))
                self.model.appendRow (newrow)
                
                
        #右键槽函数
    @Slot(QPoint)
    def on_view_customContextMenuRequested(self, point):
        #获取某行，某列
#        print self.view1.columnAt(point.x())
        #获得当前的选中行
        self.row = self.view.rowAt(point.y())
        rightMenu = QMenu(self)
        refreshAction = QAction("Refresh", self)
        refreshAction.setStatusTip("Refresh the fireworks from  database")
        refreshAction.connect(SIGNAL("triggered()"), self.refresh)
        rightMenu.addAction(refreshAction)
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
            record = self.session.query (ScriptData).filter_by(UUID = item1.text()).first()
            #删除表格里面数据
            self.model.takeRow(self.row)
            #删除数据库里面的数据
            self.session.delete(record)
        
        
        
        
        
    def refresh(self):
        self.model.clear()
        self.model.setHorizontalHeaderLabels (["UUID", "Name", "Alias", "Size", "Ignition Time", "Rising Time(s)", "Effect Time", "Ignition ID", "Connector ID", "Tilt Angle","Information", "Notes"])
        self.query(self.Type)
        self.view.hideColumn(0)


