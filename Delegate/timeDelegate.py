#coding=utf-8
'''
Created on 2013-10-12

@author: YuJin
'''
from PySide import QtGui, QtCore
from Models.ProjectDB import ProFireworksData
from Models.LocalDB import FireworksData
import json

class TimeDelegate(QtGui.QStyledItemDelegate):

    def __init__(self, localSession, proSession, parent = None):
        QtGui.QStyledItemDelegate.__init__(self, parent)
        self.parent = parent
        self.localSession = localSession
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
        print data
        print index.column()
        #获取该行脚本烟花
        scriptUUID = self.parent.proModel.item(index.row(), 0).text()
        with self.proSession.begin():
            scriptData = self.proSession.query(ProFireworksData).filter_by(UUID = scriptUUID).first()
        with self.localSession.begin():
            fireworks = self.localSession.query(FireworksData).filter_by(UUID = scriptData.FireworkID).first()
        
        if index.column() == 1: #开爆时刻
            with self.proSession.begin():
                recordEffectMoment = self.proSession.query(ProFireworksData).filter_by(UUID = scriptUUID).first()
                recordEffectMoment.IgnitionTime = data - fireworks.RisingTime
        
        if index.column() == 6: #点火时刻
            with self.proSession.begin():
                recordIgnitionMoment = self.proSession.query(ProFireworksData).filter_by(UUID = scriptUUID).first()
                recordIgnitionMoment.IgnitionTime = data
            
        if index.column() == 7: #上升时间
            with self.localSession.begin():
                recordRisingTime = self.localSession.query(FireworksData).filter_by(UUID = scriptData.FireworkID).first()
                recordRisingTime.RisingTime = data
        
        if index.column() == 8: #效果时间
            with self.localSession.begin():
                recordEffectTime = self.localSession.query(FireworksData).filter_by(UUID = scriptData.FireworkID).first()
                info = json.loads(recordEffectTime.EffectsInfo)
                info["EffectsInfo"][0][2] = str(data / 1000.0)
                recordEffectTime.EffectsInfo = json.dumps(info)
                
        if index.column() == 9: #结束时刻
            print index.column()
            
        self.parent.refreshScript()
        
