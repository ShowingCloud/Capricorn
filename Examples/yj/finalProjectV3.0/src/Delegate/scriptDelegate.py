#coding=utf-8
'''
Created on 2013-3-7

@author: pyroshow
'''
from Models.EngineeringDB import *
from PySide import QtGui, QtCore
from UI import rc_picture
from UI.ui_chooseIgnitionBox import IgnitionBox
from datetime import timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import sys
#from popupWindow.uiModifyCombination import ModifyCombination

class ScriptDelegate(QtGui.QStyledItemDelegate):
    
    def __init__(self,  parent = None):
        QtGui.QStyledItemDelegate.__init__(self, parent)
        self.parent = parent
        
        self.engine = create_engine("sqlite:///engineering.db")
        self.session = scoped_session(sessionmaker(bind = self.engine, autocommit= True))
        
        
    
        
    def createEditor (self, parent, option, index):
#        pass
#        print index.column()
#        print index.data()
        if index.column() == 2 or index.column() == 8 or index.column() == 10:
            ignEdit = QtGui.QLineEdit(parent)
            return ignEdit
        elif index.column() == 7:
            button = QtGui.QMessageBox.question(parent, "Question", "You have not chosen the ignition box,\n Choose now?", QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Ok)
            if button == QtGui.QMessageBox.Ok:
                UUID = self.parent.model.item(index.row()).text()
                FieldID = self.parent.model.item(index.row(), 1).text()
                chooseIgnitionBox = IgnitionBox(UUID, FieldID, parent)
                accept = chooseIgnitionBox.exec_()
                if accept == 1:
                    pass
                    self.parent.model.clear()
                    self.parent.model.setHorizontalHeaderLabels (["UUID", "FieldID", "Ignition Time", "Rising Time(s)", "Effect Time", "Name", "Size",  "Ignition ID", "Tilt Angle", "Information", "Notes"])
                    self.parent.query(FieldID)
                    self.parent.view.hideColumn(0)
                    self.parent.view.hideColumn(1)
            elif button == QtGui.QMessageBox.Cancel:
                    pass
            else:
                return
            
        else:
            pass
                
        
    def setEditorData(self, editor, index):
        
        pass
        
    def setModelData(self, editor, model, index):
        UUID = self.parent.model.item(index.row()).text()
        FieldID = self.parent.model.item(index.row(), 1).text()
        
        with self.session.begin():
            record = self.session.query (ScriptData).filter_by(UUID = UUID).first()
            if index.column() == 2:
                record.IgnitionTime = timedelta(seconds = float(editor.text()))
            elif index.column() == 8:
                record.Angle = editor.text()
            elif index.column() == 10:
                record.Notes = editor.text()
                
        self.parent.model.clear()
        self.parent.model.setHorizontalHeaderLabels (["UUID","FieldID", "Ignition Time", "Rising Time(s)", "Effect Time", "Name", "Size",  "Ignition ID", "Tilt Angle", "Information", "Notes"])
        self.parent.query(FieldID)
        self.parent.view.hideColumn(0)
        self.parent.view.hideColumn(1)
    
    
    
    