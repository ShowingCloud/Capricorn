#coding=utf-8
'''
Created on 2013-3-15

@author: pyroshow
'''

from PySide import QtGui

from Models.EngineeringDB import *

import uuid
from datetime import datetime

class FieldDatabase(QtGui.QDialog):
    
    def __init__(self, session, fieldUUID , parent = None):
        QtGui.QDialog.__init__(self, parent)
        
        self.groupBox = QtGui.QGroupBox("FieldDatabase:") 
        
        self.idLab = QtGui.QLabel("FIieldID:")
        self.idEdit = QtGui.QLineEdit()
        
        self.notesLab = QtGui.QLabel("Notes:")
        self.notesText = QtGui.QTextEdit()
        
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.idLab)
        vbox.addWidget(self.idEdit)
        vbox.addWidget(self.notesLab)
        vbox.addWidget(self.notesText)
        
        self.groupBox.setLayout(vbox)
        
        self.saveBtn = QtGui.QPushButton("Save")
        self.cancelBtn = QtGui.QPushButton("Cancel")
        
        btnLayout = QtGui.QHBoxLayout()
        btnLayout.addStretch(1)
        btnLayout.addWidget(self.saveBtn)
        btnLayout.addWidget(self.cancelBtn)
        
        mainLayut = QtGui.QVBoxLayout()
        mainLayut.addWidget(self.groupBox)
        mainLayut.addLayout(btnLayout)
        
        self.setLayout(mainLayut)
        
        self.saveBtn.clicked.connect(self.save)
        self.cancelBtn.clicked.connect(self.cancel)
        
        self.session = session
        self.fieldUUID = fieldUUID
        
    def save(self):
        with self.session.begin():
            data = self.session.query(FieldsData).filter_by(UUID = self.fieldUUID).first()
        with self.session.begin():
            record = FieldsData()
            
            record.UUID = str(uuid.uuid1())
            record.CTime = datetime.utcnow()
            record.MTime = datetime.utcnow()
            record.FieldID = self.idEdit.text()
            record.Parent = data.Parent
            record.Location = data.Location
            record.Notes = self.notesText.toPlainText()
            
            self.session.add(record)
        self.accept()
        self.close()
    
    def cancel(self):
        self.close()
        
        
        


