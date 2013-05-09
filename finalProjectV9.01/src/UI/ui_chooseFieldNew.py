#coding=utf-8
'''
Created on 2013-3-13

@author: pyroshow
'''

from Delegate.chooseFieldDelegate import ChooseFieldDelegate
from Delegate.chooseBoxDelegate import ChooseBoxDelegate
from Models.ProjectDB import *
from PySide.QtCore import *
from PySide.QtGui import *
from Models.LocalDB import *
import json
import uuid
from datetime import datetime, timedelta


class ChooseField(QDialog):
    
    def __init__(self, sess, session, FireworkID, time, musicSignal,parent = None):
        
        QDialog.__init__(self, parent)
        self.session = session
        self.musicSignal = musicSignal
        self.FireworkID = FireworkID
        self.groupBox = QGroupBox("Choose Field:")
        self.view = QTableView(self)
        self.view.setAlternatingRowColors(True)
        self.model = QStandardItemModel(0, 3, self)
        self.model.setHorizontalHeaderLabels(["UUID", "FieldID", "Choose","Choose Box"])
        
        self.view.setModel(self.model)
        self.view.setMinimumWidth(self.view.horizontalHeader().length())
        self.view.setItemDelegateForColumn(2, ChooseFieldDelegate(self))
        self.view.setItemDelegateForColumn(3, ChooseBoxDelegate(self.session,self))
        
        self.view.hideColumn(0)
        
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
        
        
        
        self.time = time
        self.query()
        
        self.okBtn.clicked.connect(self.confirm)
        self.cancelBtn.clicked.connect(self.cancel)
        
        self.sess = sess
        
    def query(self):
        
        with self.session.begin():
            
            record = self.session.query(FieldsData).all()
            
            for row in record:
                newRow = []
                newRow.append (QStandardItem (row.UUID))
                newRow.append (QStandardItem (row.Name))
                newRow.append (QStandardItem ("0"))
                newRow.append (QStandardItem ("Not chosen"))
                self.model.appendRow(newRow)
                
    def confirm(self):
        
        count = self.model.rowCount()
        
        UUID = []
        for i in range(count) :
            if self.model.item(i, 2).text() == "1":
                rowDict = {'FieldID':None,'BoxID':None,'Choose':None}
                rowDict['FieldID'] = self.model.item(i, 1).text()
                rowDict['BoxID'] = self.model.item(i,3).text()
                rowDict['Choose'] = self.model.item(i,2).text()
                UUID.append(rowDict)
                print rowDict['FieldID'],'',rowDict['BoxID'],' ',rowDict['Choose']
        if len(UUID) == 0:
                QMessageBox.information(self, "Information", " You must choose <b> One </b> field!!!")
        else:
            with self.sess.begin():
                data = self.sess.query (FireworksData).filter_by(UUID = self.FireworkID).first()
            if data.Type == "Combination":
                info = json.loads(data.Combination)
                k = info.keys()
                num = len(info[k[0]])
                for i in range(len(UUID)):
                    if UUID[i]['BoxID'] != 'Not chosen' and UUID[i]['Choose']=='1':
                        with self.session.begin():
                            row = self.session.query(IgnitorsData).filter_by(BoxID = UUID[i]['BoxID']).first()
                            if row.SurplusHeads < num -1:
                                QMessageBox.information(self, "Information", "SurplusHeads not enough!!!")
                                return
                for i in range(num):
                    if i == 0:
                        continue
                    with self.sess.begin():
                        item = self.sess.query (FireworksData).filter_by(Name = info[k[0]][i][0]).first()
                    risTime = item.RisingTime
                    time = self.time - risTime + timedelta(seconds = float(info[k[0]][i][1])) 
                    self.addToScript(item.UUID, time, UUID)
                        
            else:
                risTime = data.RisingTime  
                time = self.time - risTime
                self.addToScript(self.FireworkID, time, UUID)
            self.accept()
            self.musicSignal.emit()
            self.close()
                
        
                
    def cancel(self):
        self.close()
        
        
    def addToScript(self, FireworkID, time,  UUID):
        for i in range(len(UUID)):
            BoxUUID = "no choose"
            if UUID[i]['BoxID'] != "Not chosen":
                with self.session.begin():
                    boxRow = self.session.query(IgnitorsData).filter_by(BoxID = UUID[i]['BoxID']).first()
                    BoxUUID = boxRow.UUID
                    
            with self.session.begin():
                record = ScriptData()
                record.UUID = str(uuid.uuid1())
                record.FieldID = UUID[i]['FieldID']
                record.CTime = datetime.utcnow()
                record.MTime = datetime.utcnow()
                record.IgnitionTime = time
                record.FireworkID = FireworkID
                record.IgnitorID = BoxUUID            
                self.session.add(record)
            if UUID[i]['BoxID'] != "Not chosen":
                self.assignIgnitionHead(record.UUID)
                print 'assignIgnitionHead fun'
                
    def assignIgnitionHead(self,scriptUUID):    
        with self.session.begin():
            other = self.session.query (ScriptData).filter_by(UUID = scriptUUID).first()
            data = self.session.query(IgnitorsData).filter_by(UUID = other.IgnitorID).first()
                ##点火头分配
            if data.TotalHeads == data.SurplusHeads:
                other.ConnectorID = 1
                data.SurplusHeads = data.SurplusHeads -1
                return
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
        with self.session.begin():
            data1 = self.session.query(IgnitorsData).filter_by(UUID = other.IgnitorID).first()
            data1.SurplusHeads = data1.SurplusHeads-1
        with self.session.begin():
            other = self.session.query (ScriptData).filter_by(UUID = scriptUUID).first()
        print 'other.ConnectorID = ',other.ConnectorID
        with self.session.begin():
            data = self.session.query(IgnitorsData).filter_by(UUID = other.IgnitorID).first()
        print 'data.SurplusHeads = ',data.SurplusHeads

