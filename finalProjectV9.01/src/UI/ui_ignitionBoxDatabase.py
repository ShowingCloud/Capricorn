#coding=utf-8
'''
Created on 2013-3-15

@author: pyroshow
'''

from Models.ProjectDB import FieldsData, IgnitorsData
from PySide import QtGui
from datetime import datetime
import uuid

#from Models.ProjectDB import *


class IgnitionBoxDatabase(QtGui.QDialog):
    
    def __init__(self, session,fieldID, parent = None):
        QtGui.QDialog.__init__(self, parent)
        
        self.groupBox = QtGui.QGroupBox("IgnitionBoxDatabase:") 
        
        self.boxLab = QtGui.QLabel("BoxID:")
        self.boxEdit = QtGui.QLineEdit()
#         self.boxEdit = QtGui.QComboBox()
#         self.boxEdit.addItems(["1", "2", "3", "4", "5", "6"])
        intVal = QtGui.QIntValidator()
        self.boxEdit.setValidator(intVal)
        self.FieldID = fieldID
        self.headsLab = QtGui.QLabel("Total Heads:")
        self.headsEdit = QtGui.QComboBox()
        self.headsEdit.addItems(["10", "50"])
        
        self.notesLab = QtGui.QLabel("Notes:")
        self.notesText = QtGui.QTextEdit()
        
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.boxLab)
        vbox.addWidget(self.boxEdit)
        vbox.addWidget(self.headsLab)
        vbox.addWidget(self.headsEdit)
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
        
    def save(self):
        with self.session.begin():
            row = self.session.query(FieldsData).filter_by(FieldID = self.FieldID).first()
        with self.session.begin():
            record = IgnitorsData()
            
            record.UUID = str(uuid.uuid1())
            record.CTime = datetime.utcnow()
            record.MTime = datetime.utcnow()
#            record.IgnitorID = 
            record.BoxID = self.boxEdit.text()
            record.TotalHeads = int(self.headsEdit.currentText())
            record.SurplusHeads = int(self.headsEdit.currentText())
            record.Notes = self.notesText.toPlainText()
            record.FieldID = row.UUID
            self.session.add(record)
        self.accept()
        self.close()

    def cancel(self):
        self.close()
        
        
        


