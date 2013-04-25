#coding=utf-8
'''
Created on 2013-3-13

@author: pyroshow
'''

from Delegate.chooseFieldDelegate import ChooseFieldDelegate
from Models.EngineeringDB import *
from PySide.QtCore import *
from PySide.QtGui import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from Models.LocalDB import *
import json
import uuid
from datetime import datetime, timedelta




class ChooseField(QDialog):
    
    def __init__(self, FireworkID, parent = None):
        
        QDialog.__init__(self, parent)
        
        self.groupBox = QGroupBox("Choose Field:")
        self.view = QTableView(self)
        self.view.setAlternatingRowColors(True)
        self.model = QStandardItemModel(0, 2, self)
        self.model.setHorizontalHeaderLabels(["UUID", "FieldID", "Choose"])
        self.view.setModel(self.model)
        self.view.setMinimumWidth(self.view.horizontalHeader().length())
        self.view.setItemDelegateForColumn(2, ChooseFieldDelegate(self))
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
        
        self.engine = create_engine("sqlite:///engineering.db")
        self.session = scoped_session(sessionmaker(bind = self.engine, autocommit= True))
        self.FireworkID = FireworkID
        self.query()
        
        self.okBtn.clicked.connect(self.confirm)
        self.cancelBtn.clicked.connect(self.cancel)
        
        self.sess = session()
        
    def query(self):
        
        with self.session.begin():
            
            record = self.session.query(FieldsData).all()
            
            for row in record:
                newRow = []
                newRow.append (QStandardItem (row.UUID))
                newRow.append (QStandardItem (row.FieldID))
                newRow.append (QStandardItem ("0"))
                
                self.model.appendRow(newRow)
                
    def confirm(self):
        
        count = self.model.rowCount()
        
        UUID = []
        for i in range(count) :
            if self.model.item(i, 2).text() == "1":
                
                UUID.append(self.model.item(i, 1).text())

        if len(UUID) == 0:
                QMessageBox.information(self, "Information", " You must choose <b> One </b> ignition box!!!")
        else:
            self.engine = create_engine("sqlite:///engineering.db")
            self.session = scoped_session(sessionmaker(bind = self.engine, autocommit= True))
            base1.metadata.create_all(self.engine)
            with self.sess.begin():
                data = self.sess.query (FireworksData).filter_by(UUID = self.FireworkID).first()
                if data.Type == "Combination":
                    info = json.loads(data.Combination)
                    k = info.keys()
                    num = len(info[k[0]])
                    for i in range(num):
                        item = self.sess.query (FireworksData).filter_by(Name = info[k[0]][i][0]).first()
                            
                        self.addToScript(item.UUID, UUID)
                        
                else:
                    self.addToScript(self.FireworkID, UUID)
            self.accept()
            self.close()
                
        
                
    def cancel(self):
        self.close()
        
        
    def addToScript(self, FireworkID, UUID):
        for i in range(len(UUID)):
        
            with self.session.begin():
                record = ScriptData()
                record.UUID = str(uuid.uuid1())
                record.FieldID = UUID[i]
                record.CTime = datetime.utcnow()
                record.MTime = datetime.utcnow()
                record.IgnitionTime = timedelta(seconds = 2)
                record.FireworkID = FireworkID
                record.IgnitorID = "no choose"
                            
                self.session.add(record)
        
        
        
        
        
        

