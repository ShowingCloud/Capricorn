#coding=utf-8
'''
Created on 2013-3-15

@author: pyroshow
'''
from PySide import QtGui
from datetime import timedelta, datetime

from Models.EngineeringDB import *

class ChangeTime(QtGui.QDialog):
    
    def __init__(self, session, UUID, risTime, effectTime, parent = None):
        QtGui.QDialog.__init__(self, parent)
        
        self.groupBox = QtGui.QGroupBox("Change time:")
        
        
        self.EffectLable = QtGui.QLabel("Effect Time:")
        self.hourBox_e = QtGui.QSpinBox()
        self.hourBox_e.setRange(0, 23)
        self.label_h_e = QtGui.QLabel(":")
        self.minuteBox_e = QtGui.QSpinBox()
        self.minuteBox_e.setRange(0, 59)    
        self.label_m_e = QtGui.QLabel(":")
        self.secondBox_e = QtGui.QSpinBox()
        self.secondBox_e.setRange(0, 59)
        self.label_s_e = QtGui.QLabel(".")
        self.microBox_e = QtGui.QSpinBox()
        self.microBox_e.setRange(0, 999999)
        
        
        grid = QtGui.QGridLayout()
        
        self.UUID = UUID
        self.risTime = risTime
        self.effectTime = effectTime
        
        hbox1 = QtGui.QHBoxLayout()
        hbox1.addWidget(self.hourBox_e)
        hbox1.addWidget(self.label_h_e)
        hbox1.addWidget(self.minuteBox_e)
        hbox1.addWidget(self.label_m_e)
        hbox1.addWidget(self.secondBox_e)
        hbox1.addWidget(self.label_s_e)
        hbox1.addWidget(self.microBox_e)
        grid.addWidget(self.EffectLable, 0, 0)
        
        grid.addLayout(hbox1, 1, 0)
        
        self.groupBox.setLayout(grid)
        
        self.okBtn = QtGui.QPushButton("OK")
        self.cancelBtn = QtGui.QPushButton("Cancel")
        
        btnLayout = QtGui.QHBoxLayout()
        #可伸缩的
        btnLayout.addStretch(1)
        btnLayout.addWidget(self.okBtn)
        btnLayout.addWidget(self.cancelBtn)
        
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(self.groupBox)
        mainLayout.addLayout(btnLayout)
        
        self.okBtn.clicked.connect(self.saveData)
        self.cancelBtn.clicked.connect(self.cancel)
        self.getData()
        
        self.setLayout(mainLayout)
        
        self.session = session
        
    def getData(self):
        self.hourBox_e.setValue(int(self.effectTime[0]))
        self.minuteBox_e.setValue(int(self.effectTime[2:4]))
        self.secondBox_e.setValue(int(self.effectTime[5:7]))
        if len(self.effectTime) > 8:
            self.microBox_e.setValue(int(self.effectTime[8:]))
        
        
    def saveData(self):
        rTime = None
        if len(self.risTime) > 8:
            rTime = timedelta(hours = int(self.risTime[0]), minutes = int(self.risTime[2:4]), seconds = int(self.risTime[5:7]), microseconds = int(self.risTime[8:]))
        else:
            rTime = timedelta(hours = int(self.risTime[0]), minutes = int(self.risTime[2:4]), seconds = int(self.risTime[5:7]))
        effTime = timedelta(hours = self.hourBox_e.value(), minutes = self.minuteBox_e.value(), seconds = self.secondBox_e.value(), microseconds = self.microBox_e.value())
        with self.session.begin():
            record = self.session.query(ScriptData).filter_by(UUID = self.UUID).first()
            record.IgnitionTime = effTime - rTime
            record.MTime = datetime.utcnow()
        
        self.accept()
        self.close()
        
        
    def cancel(self):
        self.close()
        




