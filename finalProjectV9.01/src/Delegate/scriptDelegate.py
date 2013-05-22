#coding=utf-8
'''
Created on 2013-3-7

@author: pyroshow
'''
from Models.ProjectDB import ScriptData, IgnitorsData
from PySide import QtGui, QtCore
from PySide.QtCore import QPoint, Slot
from UI.ui_changeTime import ChangeTime
from UI.ui_chooseIgnitionBox import IgnitionBox
from sqlalchemy import func
#from UI import rc_picture
#from datetime import timedelta

class ScriptDelegate(QtGui.QStyledItemDelegate):
    
    def __init__(self, session, musicSignal,parent = None):
        QtGui.QStyledItemDelegate.__init__(self, parent)
        self.parent = parent
        self.musicSignal = musicSignal
        self.session = session
        
#    #重写自带方法(参数自带)
    def paint(self, painter, option, index):
        
        style = QtGui.QApplication.style()
            
        label = QtGui.QStyleOptionViewItemV4 (option)
        label.text = index.data()
        label.displayAlignment = QtCore.Qt.AlignCenter

        style.drawControl (QtGui.QStyle.CE_ItemViewItem, label, painter)    
        
    @Slot(QPoint)
    def createEditor (self, parent, option, index):
        UUID = self.parent.model.item(index.row()).text() #脚本UUID
        FieldID = self.parent.model.item(index.row(), 1).text()
        risTime = self.parent.model.item(index.row(), 3).text() #上身时间
        time = self.parent.model.item(index.row(), 4).text()    #效果时间
        
        if index.column() == 4 :
            button = QtGui.QMessageBox.question(parent, "Question", "Are you sure to modify the effect of time??", QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Ok)
            if button == QtGui.QMessageBox.Ok:
                changeTime = ChangeTime(self.session, UUID, risTime, time, parent)
                accept = changeTime.exec_()
                if accept == 1:
                    self.parent.model.clear()
                    self.parent.model.setHorizontalHeaderLabels (["UUID","FieldID", "Ignition Time", "Rising Time(s)", "Effect Time", "Name", "Size (mm)",  "Ignition ID", "Tilt Angle", "Information", "Notes"])
                    self.parent.query(FieldID)
                    self.parent.view.hideColumn(0)
                    self.parent.view.hideColumn(1)
                    self.musicSignal.emit()
            elif button == QtGui.QMessageBox.Cancel:
                    pass
            else:
                return
        if index.column() == 8 or index.column() == 10:
            ignEdit = QtGui.QLineEdit(parent)
            return ignEdit
        elif index.column() == 7:
            box = {}
            
            with self.session.begin():
                record = self.session.query(func.count(ScriptData.ID), ScriptData.IgnitorID).group_by(ScriptData.IgnitorID).all()
            with self.session.begin():
                data = self.session.query(IgnitorsData.UUID).all()
            for i in range(len(data)):
                box[data[i][0]] = 0
                
            for j in range(len(record)):
                if record[j][1] == "no choose":
                    continue
                else:
                    box[record[j][1]] = record[j][0]
                    
            button = QtGui.QMessageBox.question(parent, "Question", "Are you sure to choose the ignition box now?", QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Ok)
            if button == QtGui.QMessageBox.Ok:
                with self.session.begin():
                    another = self.session.query(ScriptData).filter_by(UUID = UUID).first() 
                chooseIgnitionBox = IgnitionBox(self.session, UUID, another.IgnitorID, box,FieldID,self.musicSignal ,parent)
                
                accept = chooseIgnitionBox.exec_()
                if accept == 1:
                    self.parent.model.clear()
                    self.parent.model.setHorizontalHeaderLabels (["UUID", "FieldID", "Ignition Time", "Rising Time(s)", "Effect Time", "Name", "Size (mm)",  "Ignition ID", "Tilt Angle", "Information", "Notes"])
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
        if index.column() == 2:
            return
        pass
        
    def setModelData(self, editor, model, index):
        UUID = self.parent.model.item(index.row()).text()
        FieldID = self.parent.model.item(index.row(), 1).text()
        
        with self.session.begin():
            record = self.session.query (ScriptData).filter_by(UUID = UUID).first()
            if index.column() == 8:
                if editor.text() == "":
                    pass
                else:
                    record.Angle = editor.text()
            elif index.column() == 10:
                if editor.text() == "":
                    pass
                else:
                    record.Notes = editor.text()
                
        self.parent.model.clear()
        self.parent.model.setHorizontalHeaderLabels (["UUID","FieldID", "Ignition Time", "Rising Time(s)", "Effect Time", "Name", "Size (mm)",  "Ignition ID", "Tilt Angle", "Information", "Notes"])
        self.parent.query(FieldID)
        self.parent.view.hideColumn(0)
        self.parent.view.hideColumn(1)
    
    
    
    