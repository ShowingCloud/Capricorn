#coding=utf-8
'''
Created on 2013-3-6

@author: pyroshow
'''

from Delegate.scriptDelegate import ScriptDelegate
from Models.EngineeringDB import *
from Models.LocalDB import *
from PySide import QtCore
from PySide import QtGui
from PySide.QtGui import QStandardItem
from datetime import datetime, timedelta





class Script(QtGui.QWidget):
    
    def __init__(self,  sess, session,musicSignal, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.musicSignal = musicSignal
        self.session = session
        self.sess = sess
        
        self.mainGroupBox = QtGui.QGroupBox("Script")
        
        self.model = QtGui.QStandardItemModel (0, 11, self)
        self.model.setHorizontalHeaderLabels(["UUID","FieldID", "Ignition Time", "Rising Time(s)", "Effect Time", "Name", "Size (mm)",  "Ignition ID",  "Tilt Angle", "Information", "Notes"])
        
        self.view = QtGui.QTableView(self)
        self.view.setAlternatingRowColors(True)
        
##        self.proxyModel = QtGui.QSortFilterProxyModel()
##        self.proxyModel.setDynamicSortFilter(True)
##        self.proxyModel.setSourceModel(self.model)
##        self.proxyModel.setFilterKeyColumn(4)
##        self.view.setModel(self.proxyModel)
        self.view.setModel(self.model)
        self.view.setSortingEnabled(True)
        self.view.setItemDelegate(ScriptDelegate(self.session,self.musicSignal,self))
        
        self.view.hideColumn(0)
        self.view.hideColumn(1)
        
        
        
        scriptLayout = QtGui.QVBoxLayout()
        scriptLayout.addWidget(self.view)
        
        self.mainGroupBox.setLayout(scriptLayout)
        
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(self.mainGroupBox)
        self.setLayout(mainLayout)
        self.resize(1500, 800)
        
        
        #设置右键菜单
        self.view.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #设置右键菜单函数
        self.view.customContextMenuRequested.connect(self.on_view_customContextMenuRequested)
       
#        self.timer = QTimer()
#        self.connect(self.timer, SIGNAL("timeout()"), self.refresh)
#        self.timer.start(500)
    @QtCore.Slot(str)
    def setCurrentFireworksTop(self, scriptUUID):
#        print 'scriptUUID-=====',scriptUUID
        model = self.view.model()
        proxy = QtGui.QSortFilterProxyModel()
        proxy.setSourceModel(model)
        proxy.setFilterKeyColumn(0)
        proxy.setFilterFixedString(scriptUUID)
        matchIndex = proxy.mapToSource(proxy.index(0,0))
#        print matchIndex
#        print model.data(matchIndex)
#        self.view.setStyleSheet("selection-background-color: rgb(255, 246, 108);selection-color: rgb(0, 0, 0);")
        self.view.setStyleSheet("selection-background-color: rgb(51, 153, 255);selection-color: rgb(255, 255, 255);")
#        self.view.setStyleSheet("")
        self.view.selectRow(matchIndex.row())
        self.view.scrollTo (model.index(matchIndex.row(),3),hint = QtGui.QAbstractItemView.PositionAtTop)
#        self.view.keyboardSearch(scriptUUID)
        
        
    def query(self, Type):
        if Type == u'ALL':
            with self.session.begin():
                record = self.session.query (ScriptData).order_by(ScriptData.IgnitionTime).all()
        else:     
            with self.session.begin():
                record = self.session.query (ScriptData).filter_by(FieldID = Type).order_by(ScriptData.IgnitionTime).all()
                self.FieldID = Type
        for row in record:
            newrow = []
            newrow.append (QtGui.QStandardItem (row.UUID))
            newrow.append (QtGui.QStandardItem (row.FieldID))
            
#            ignitionTime = timedelta(seconds = row.IgnitionTime.seconds,milliseconds =row.IgnitionTime.microseconds/1000 )
            ignitionTime = row.IgnitionTime
            if row.IgnitionTime < timedelta(0):
                if row.IgnitionTime.microseconds == 0:
                    newrow.append (QStandardItem ("-" + str(-ignitionTime)))
                else:
                    newrow.append (QStandardItem ('-'+ str(-ignitionTime)[0:len(str(-ignitionTime))-4:1]))
            else:
                if row.IgnitionTime.microseconds == 0:
                    newrow.append (QStandardItem (str(ignitionTime)))
                else:
                    newrow.append (QStandardItem (str(ignitionTime)[0:len(str(ignitionTime))-4:1]))
                    
            UUID = row.FireworkID
            time = None
            infor = None
            effectTime = None
            size = None
            name =  None
                
            boxUUID  = row.IgnitorID
                
            with self.sess.begin():
                data = self.sess.query (FireworksData).filter_by(UUID = UUID).first()
                    
            time = timedelta(seconds = data.RisingTime.seconds,milliseconds = data.RisingTime.microseconds/1000)
            
            infor = data.Information
            effectTime = ignitionTime+ data.RisingTime
            EffectTime = timedelta(seconds = effectTime.seconds,milliseconds = effectTime.microseconds/1000)
            size = data.Size
            name = data.Name
            newrow.append (QStandardItem (str(time)))
            if effectTime.microseconds/1000 == 0:
                newrow.append (QStandardItem (str(EffectTime)))
            else:
                newrow.append (QStandardItem (str(EffectTime)[0:len(str(EffectTime))-4:1]))
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
#        self.view.sortByColumn(4, Qt.AscendingOrder)
        #右键槽函数
    @QtCore.Slot(QtCore.QPoint)
    def on_view_customContextMenuRequested(self, point):
        #获取某行，某列
#        print self.view1.columnAt(point.x())
        #获得当前的选中行
        self.row = self.view.rowAt(point.y())
        rightMenu = QtGui.QMenu(self)
#        refreshAction = QAction("Refresh", self)
#        refreshAction.setStatusTip("Refresh the fireworks from  database")
#        refreshAction.connect(SIGNAL("triggered()"), self.refresh)
#        rightMenu.addAction(refreshAction)
        if self.row >= 0:
            deleteAction = QtGui.QAction("Delete", self)
            deleteAction.setStatusTip("Delete selected line")
            deleteAction.connect(QtCore.SIGNAL("triggered()"), self.delete)
            rightMenu.addAction(deleteAction)
            
        rightMenu.exec_(QtGui.QCursor.pos())
        
    #从View里面删除选中的行   
    def delete(self):
        item1 = self.model.item(self.row)
        with self.session.begin():
            record = self.session.query (ScriptData).filter_by(UUID = item1.text()).first()
            UUID = record.IgnitorID
            #删除表格里面数据
            self.model.takeRow(self.row)
            #删除数据库里面的数据
            self.session.delete(record)
        
        if UUID != "no choose" :   
            with self.session.begin():
                row = self.session.query(IgnitorsData).filter_by(UUID = UUID).first()
                row.SurplusHeads = row.SurplusHeads + 1
        
        self.musicSignal.emit()
        
        
    def refresh(self, Type):
        pass
#        self.model.clear()
#        self.model.setHorizontalHeaderLabels (["UUID", "Ignition Time", "Rising Time(s)", "Effect Time", "Name", "Size",  "Ignition ID",  "Tilt Angle", "Information", "Notes"])
#        self.query(Type)
#        self.view.hideColumn(0)


