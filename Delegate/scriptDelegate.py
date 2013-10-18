#coding=utf-8
'''
Created on 2013-10-11

@author: YuJin
'''

from PySide import QtGui, QtCore
from Models.ProjectDB import ProFireworksData

class ScriptDelegate(QtGui.QStyledItemDelegate):
    
    def __init__(self, proSession, parent = None):
        QtGui.QStyledItemDelegate.__init__(self, parent)
        self.parent = parent
        self.proSession = proSession
    
        
#    #重写自带方法(参数自带)
    def paint(self, painter, option, index):
        
        style = QtGui.QApplication.style()
        label = QtGui.QStyleOptionViewItemV4 (option)
        if index.column() == 2 or index.column() == 4:
            label.text = index.data()
        else:
            label.text = str(index.data())
        label.displayAlignment = QtCore.Qt.AlignCenter
    
        style.drawControl (QtGui.QStyle.CE_ItemViewItem, label, painter)
            
    def createEditor (self, parent, option, index):
        if index.column() == 11 and index.data() != 0:
            spinBox = QtGui.QSpinBox(parent)
            spinBox.setMinimum(1)
            spinBox.setMaximum(16)
            spinBox.installEventFilter(self)
            return spinBox
        else:
            pass
    
    def setEditorData(self, editor, index):
        if index.column() == 11 and editor != None :
            editor.setValue(index.data())
        else:
            pass
        
    def setModelData(self, editor, model, index):
        if index.column() == 11 and editor != None :
            if editor.value() == index.data():
                return
            scriptUUID = self.parent.proModel.item(index.row(), 0).text()
            with self.proSession.begin():
                scriptData = self.proSession.query(ProFireworksData).filter_by(UUID = scriptUUID).first()
                scriptData.ConnectorID = editor.value() 
            self.parent.refreshScript()
        else:
            pass
