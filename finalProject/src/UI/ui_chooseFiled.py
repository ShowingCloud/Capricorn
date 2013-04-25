#coding=utf-8
'''
Created on 2013-3-8

@author: pyroshow
'''

from PySide.QtGui import QDialog, QGroupBox, QRadioButton, QHBoxLayout, \
    QButtonGroup, QVBoxLayout, QPushButton, QMessageBox

class ChooseFiledWidget(QDialog):
    
    def __init__(self, parent = None):
        
        QDialog.__init__(self, parent)
        
        self.groupButton = QGroupBox("Choose Filed:")
        
        self.filedGroup = QButtonGroup()
        self.button1 = QRadioButton("1", self)
        self.button2 = QRadioButton("2", self)
        self.button3 = QRadioButton("3", self)
        self.button4 = QRadioButton("4", self)
        self.button5 = QRadioButton("5", self)
        self.button6 = QRadioButton("6", self)
        self.filedGroup.addButton(self.button1)
        self.filedGroup.addButton(self.button2)
        self.filedGroup.addButton(self.button3)
        self.filedGroup.addButton(self.button4)
        self.filedGroup.addButton(self.button5)
        self.filedGroup.addButton(self.button6)
        
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        layout.addWidget(self.button6)
        self.groupButton.setLayout(layout)
        
        self.okBtn = QPushButton("OK")
        self.cancelBtn = QPushButton("Cancel")
        
        btnLayout = QHBoxLayout()
        #可伸缩的
        btnLayout.addStretch(1)
        btnLayout.addWidget(self.okBtn)
        btnLayout.addWidget(self.cancelBtn)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.groupButton)
        mainLayout.addLayout(btnLayout)
        self.setLayout(mainLayout)
        
        self.Filed = None
        
        self.filedGroup.buttonClicked.connect(self.getField)
        
        self.okBtn.clicked.connect(self.showScript)
        self.cancelBtn.clicked.connect(self.cancel)
        
        
    def getField(self, button):
        
        self.Filed = button.text()
        print self.Filed
        
        
    def showScript(self):
        print self.Filed
        if self.Filed == None:
            QMessageBox.information(self, "Information", "Must choose <b> Field </b>!!!")
        else:
            self.close()
        
        
    
    def cancel(self):
        self.close()
        
        




