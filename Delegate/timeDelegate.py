#coding=utf-8
'''
Created on 2013-10-12

@author: YuJin
'''
from PySide import QtGui, QtCore
from Models.ProjectDB import ProFireworksData

class TimeDelegate(QtGui.QStyledItemDelegate):

    def __init__(self, proSession, parent = None):
        QtGui.QStyledItemDelegate.__init__(self, parent)
        self.parent = parent
        self.proSession = proSession
        
#    #重写自带方法(参数自带)
    def paint(self, painter, option, index):
         
        style = QtGui.QApplication.style()
        label = QtGui.QStyleOptionViewItemV4 (option)
          
        displayTime = QtCore.QTime(index.data() / 3600000, (index.data() / 60000) % 60, (index.data() / 1000) % 60, index.data() % 1000)
        label.text = displayTime.toString('h:mm:ss.z')
        label.displayAlignment = QtCore.Qt.AlignCenter
        
        style.drawControl (QtGui.QStyle.CE_ItemViewItem, label, painter)

    def createEditor (self, parent, option, index):
        
        timeEdit = QtGui.QTimeEdit(parent)
        timeEdit.setDisplayFormat('h:mm:ss.z')
        timeEdit.installEventFilter(self)
        return timeEdit
    
    def setEditorData(self, editor, index):
        displayTime = QtCore.QTime(index.data() / 3600000, (index.data() / 60000) % 60, (index.data() / 1000) % 60, index.data() % 1000)
        editor.setTime(displayTime)
        
    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
        
    def setModelData(self, editor, model, index):
        
        data = editor.time().hour()*3600000 + editor.time().minute() * 60000 + editor.time().second() *1000 + editor.time().msec()
        model.setData(index, data)
#         print data
#         print index.column()
        #获取该行脚本烟花
        scriptUUID = self.parent.proModel.item(index.row(), 0).text()
        
        if index.column() == 1: #开爆时刻
            with self.proSession.begin():
                recordEffectMoment = self.proSession.query(ProFireworksData).filter_by(UUID = scriptUUID).first()
                notes = recordEffectMoment.Notes.split(',')
                recordEffectMoment.IgnitionTime = data - int(notes[0])
        
        if index.column() == 6: #点火时刻
            with self.proSession.begin():
                recordIgnitionMoment = self.proSession.query(ProFireworksData).filter_by(UUID = scriptUUID).first()
                recordIgnitionMoment.IgnitionTime = data
            
        if index.column() == 7: #上升时间
            with self.proSession.begin():
                recordRisingTime = self.proSession.query(ProFireworksData).filter_by(UUID = scriptUUID).first()
                recordRisingTime.Notes = str(data) + ',' + recordRisingTime.Notes.split(',')[1]
        
        if index.column() == 8: #效果时间
            with self.proSession.begin():
                recordEffectTime = self.proSession.query(ProFireworksData).filter_by(UUID = scriptUUID).first()
                recordEffectTime.Notes = recordEffectTime.Notes.split(',')[0] + ',' + str(data)
                
        if index.column() == 9: #结束时刻
            with self.proSession.begin():
                recordOverMoment = self.proSession.query(ProFireworksData).filter_by(UUID = scriptUUID).first()
                overNotes = recordOverMoment.Notes.split(',')
                recordOverMoment.IgnitionTime = data - int(overNotes[0]) - int(overNotes[1])
            
        self.parent.refreshScript()
        
