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




class IgnitionBox(QDialog):
    
    def __init__(self, session, UUID, boxUUID, residue, parent = None):
        
        QDialog.__init__(self, parent)
        
        self.groupBox = QGroupBox("Choose Ignition Box:")
        self.view = QTableView(self)
        self.view.setAlternatingRowColors(True)
        self.model = QStandardItemModel(0, 6, self)
        self.model.setHorizontalHeaderLabels(["UUID", "IgnitorID", "BoxID", "Total Heads", "Surplus Heads", "Choose", "Notes"])
        self.view.setModel(self.model)
        self.view.setMinimumWidth(self.view.horizontalHeader().length())
        self.view.setItemDelegate(CheckBoxDelegate(self))
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
        
        self.session = session
        self.UUID = UUID
        self.residue = residue
        self.boxUUID = boxUUID
        
        
        self.reset()
        self.query()
        self.constraints()
        
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
#        if self.row >= 0:
#            deleteAction = QAction("Delete", self)
#            deleteAction.setStatusTip("Delete selected line")
#            deleteAction.connect(SIGNAL("triggered()"), self.delete)
#            rightMenu.addAction(deleteAction)
            
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
        ignitionBoxDatabase = IgnitionBoxDatabase(self.session, self)
        
        accept = ignitionBoxDatabase.exec_()
        if accept == 1:
            self.model.clear()
            self.model.setHorizontalHeaderLabels(["UUID", "IgnitorID", "BoxID", "Total Heads", "Surplus Heads", "Choose", "Notes"])
            self.query()
            self.view.hideColumn(0)
            self.view.hideColumn(1)
            
    def constraints(self):
        
        with self.session.begin():
                record = self.session.query(IgnitorsData).all()
        for row in record:
            if row.SurplusHeads == 0:
                print "*****************"
                m = 0
                for k in range(self.model.rowCount()) :
                    if self.model.item(k, 0).text() == row.UUID:
                        m = k
                        break
                index = self.model.index(m , 5)
                self.model.setData(index, "2", Qt.EditRole)
            
        
        
    def reset(self):
        
        for i in self.residue.keys():
            with self.session.begin():
                record = self.session.query(IgnitorsData).filter_by(UUID= i).first()
                if record != None:
                    record.SurplusHeads = record.TotalHeads - self.residue[i]
                
            
            
    def query(self):
        
        with self.session.begin():
            
            record = self.session.query(IgnitorsData).all()

        for row in record:
            newRow = []
            newRow.append (QStandardItem (row.UUID))
            newRow.append (QStandardItem (str(row.IgnitorID)))
            newRow.append (QStandardItem (row.BoxID))
            newRow.append (QStandardItem (str(row.TotalHeads)))
            newRow.append (QStandardItem (str(row.SurplusHeads)))
            newRow.append (QStandardItem ("0"))
            newRow.append (QStandardItem (row.Notes))
                
            self.model.appendRow(newRow)
        if self.boxUUID != "no choose":
            row = 0
            for k in range(self.model.rowCount()) :
                if self.model.item(k, 0).text() == self.boxUUID:
                    row = k
                    break
            index = self.model.index(row , 5)
            self.model.setData(index, "1", Qt.EditRole)
                
    def confirm(self):
        
        count = self.model.rowCount()
        UUID = []
        for i in range(count) :
            if self.model.item(i, 5).text() == "1":
                UUID.append(self.model.item(i, 0).text())
                
        if len(UUID) > 1:
                QMessageBox.information(self, "Information", " Can only choose <b> One </b> ignition box!!!")
        elif len(UUID) == 0:
                QMessageBox.information(self, "Information", " You must choose <b> One </b> ignition box!!!")
        else:
            with self.session.begin():
                data = self.session.query(IgnitorsData).filter_by(UUID = UUID[0]).first()
                other = self.session.query (ScriptData).filter_by(UUID = self.UUID).first()
                other.IgnitorID = data.UUID
            if data.TotalHeads == data.SurplusHeads:
                other.ConnectorID = 1
            else:
                with self.session.begin():
                    Box = self.session.query (ScriptData).filter_by(IgnitorID = data.UUID)
                headList = [0]*data.TotalHeads
                for row in Box:
                    if row.ConnectorID !=None:
                        headList[row.ConnectorID-1] = 1
                for i in range(data.TotalHeads):
                    if headList[i] == 0:
                        other.ConnectorID = i+1
                        break
            print 'Ignition head is ',other.ConnectorID
                
                            
            ###点火头分配
                
            
            self.accept() 
            self.close()
          
        
                
    def cancel(self):
        self.close()
        
        
        
        
        
        

