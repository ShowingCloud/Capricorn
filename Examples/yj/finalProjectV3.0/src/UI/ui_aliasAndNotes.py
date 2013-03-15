#coding=utf-8
'''
Created on 2013-3-8

@author: pyroshow
'''
from PySide.QtGui import *
from Models.LocalDB import *
from datetime import datetime

class ModifyAliasNotes(QDialog):
    
    def __init__(self, UUID, Alias, Notes, parent =None):
        
        QDialog.__init__(self, parent)
        
        self.group = QGroupBox("Modify")
        
        self.aliasLab = QLabel("Alias:")
        self.aliasEdit = QLineEdit()
        self.notesLab = QLabel("Notes:")
        self.notesTxt = QTextEdit()
        
        vbox = QVBoxLayout()
        
        vbox.addWidget(self.aliasLab)
        vbox.addWidget(self.aliasEdit)
        vbox.addWidget(self.notesLab)
        vbox.addWidget(self.notesTxt)
        
        self.group.setLayout(vbox)
        
        self.saveBtn = QPushButton("Save")
        self.cancelBtn = QPushButton("Cancel")
        
        btnLayout = QHBoxLayout()
        btnLayout.addStretch(1)
        btnLayout.addWidget(self.saveBtn)
        btnLayout.addWidget(self.cancelBtn)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.group)
        mainLayout.addLayout(btnLayout)
        
        self.setLayout(mainLayout)
        
        self.Alias = Alias
        self.Notes = Notes
        self.UUID = UUID
        
        self.aliasEdit.setText(self.Alias)
        self.notesTxt.setText(self.Notes)
        
        self.saveBtn.clicked.connect(self.saveData)
        self.cancelBtn.clicked.connect(self.cancel)
        
        self.sess = session()
        
        
    def saveData(self):
        with self.sess.begin():
            record = self.sess.query (FireworksData).filter_by(UUID = self.UUID).first()
            record.CTime = datetime.utcnow()
            record.Alias = self.aliasEdit.text()
            record.Notes = self.notesTxt.toPlainText()
            
            
        
        self.aliasEdit.setText("")
        self.notesTxt.setText("")
        self.accept()
        
        self.close()
        
        
    def cancel(self):
        self.close()
        
        
        
        
        
        
        
