#coding=utf-8
'''
Created on 2013-3-6

@author: pyroshow
'''

from Delegate.scriptDelegate import ScriptDelegate
from Models.EngineeringDB import *
from Models.LocalDB import *
from PySide.QtCore import *
from PySide.QtGui import *
from datetime import datetime, timedelta
import json




class Script(QWidget):
    
    def __init__(self,  sess, session,musicSignal, parent = None):
        QWidget.__init__(self, parent)
        self.musicSignal = musicSignal
        self.session = session
        self.sess = sess
        
        self.mainGroupBox = QGroupBox("Script")
        
        self.model = QStandardItemModel (0, 11, self)
        self.model.setHorizontalHeaderLabels(["UUID","FieldID", "Ignition Time", "Rising Time(s)", "Effect Time", "Name", "Size (mm)",  "Ignition ID",  "Tilt Angle", "Information", "Notes"])
        
        self.view = QTableView(self)
        self.view.setAlternatingRowColors(True)
        
        self.proxyModel = QSortFilterProxyModel()
        self.proxyModel.setDynamicSortFilter(True)
        self.proxyModel.setSourceModel(self.model)
        self.view.setModel(self.proxyModel)
        self.view.setSortingEnabled(True)
        self.view.setItemDelegate(ScriptDelegate(self.session,self.musicSignal,self))
        
        self.view.hideColumn(0)
        self.view.hideColumn(1)
        
        self.view.sortByColumn(4, Qt.AscendingOrder)
        
        scriptLayout = QVBoxLayout()
        scriptLayout.addWidget(self.view)
        
        self.mainGroupBox.setLayout(scriptLayout)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.mainGroupBox)
        self.setLayout(mainLayout)
        self.resize(1500, 800)
        
        
        #设置右键菜单
        self.view.setContextMenuPolicy(Qt.CustomContextMenu)
        #设置右键菜单函数
        self.view.customContextMenuRequested.connect(self.on_view_customContextMenuRequested)
       
#        self.timer = QTimer()
#        self.connect(self.timer, SIGNAL("timeout()"), self.refresh)
#        self.timer.start(500)
        
    def query(self, Type):
        print repr(Type)
        if Type == u'ALL':
            with self.session.begin():
                record = self.session.query (ScriptData).all()
        else:     
            with self.session.begin():
                record = self.session.query (ScriptData).filter_by(FieldID = Type).all()
                self.FieldID = Type
        for row in record:
            newrow = []
            newrow.append (QStandardItem (row.UUID))
            newrow.append (QStandardItem (row.FieldID))
            ignitionTime = row.IgnitionTime
            if ignitionTime < timedelta(0):
                newrow.append (QStandardItem ("-" + str(-ignitionTime)))
            else:
                newrow.append (QStandardItem (str(ignitionTime)))
            UUID = row.FireworkID
            time = None
            infor = None
            effectTime = None
            size = None
            name =  None
                
            boxUUID  = row.IgnitorID
                
            with self.sess.begin():
                data = self.sess.query (FireworksData).filter_by(UUID = UUID).first()
                    
            time = data.RisingTime
            infor = data.Information
            effectTime = ignitionTime+ data.RisingTime
            size = data.Size
            name = data.Name
                
            newrow.append (QStandardItem (str(time)))
            newrow.append (QStandardItem (str(effectTime)))
            newrow.append (QStandardItem (name))
            newrow.append (QStandardItem (str(size)))
            if boxUUID != "no choose":
                with self.session.begin():
                    box = self.session.query (IgnitorsData).filter_by(UUID = boxUUID).first()
                newrow.append (QStandardItem (str(box.BoxID)))
            else:
                newrow.append (QStandardItem (row.IgnitorID))
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
#        refreshAction = QAction("Refresh", self)
#        refreshAction.setStatusTip("Refresh the fireworks from  database")
#        refreshAction.connect(SIGNAL("triggered()"), self.refresh)
#        rightMenu.addAction(refreshAction)
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
        self.musicSignal.emit()
        
        
    def refresh(self, Type):
        pass
#        self.model.clear()
#        self.model.setHorizontalHeaderLabels (["UUID", "Ignition Time", "Rising Time(s)", "Effect Time", "Name", "Size",  "Ignition ID",  "Tilt Angle", "Information", "Notes"])
#        self.query(Type)
#        self.view.hideColumn(0)


