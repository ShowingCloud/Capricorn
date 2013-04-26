#coding=utf-8
'''
Created on 2013-1-31

@author: pyroshow
'''

from PySide import QtGui, QtCore
from Models.EngineeringDB import IgnitorsData

class ChooseBoxDelegate(QtGui.QStyledItemDelegate):
    
    def __init__(self,session, parent = None):
        QtGui.QStyledItemDelegate.__init__(self, parent)
        self.parent = parent
        self.session = session
    def paint(self, painter, option, index):
        style = QtGui.QApplication.style()
            
        label = QtGui.QStyleOptionViewItemV4 (option)
        label.text = index.data()
        label.displayAlignment = QtCore.Qt.AlignCenter

        style.drawControl (QtGui.QStyle.CE_ItemViewItem, label, painter)
        
        
    def createEditor (self, parent, option, index):
        if self.parent.model.item(index.row(),2).text() == '0':
#            default_editor = QtGui.QItemDelegate.createEditor(self, parent, option, index)
            return 
            
        combox = QtGui.QComboBox(parent)
        combox.addItem('Not chosen')
        
        UUID = self.parent.model.item(index.row()).text()
        with self.session.begin():
            boxTable = self.session.query(IgnitorsData).filter_by(FieldID = UUID).all()
            for row in boxTable:
                combox.addItem(str(row.BoxID))
        return combox
    
    def setEditorData(self, editor, index):
        pass
    
    def updateEditorGeometry(self, editor, option, index):
        
        if type(editor) == QtGui.QComboBox:
            editor.setGeometry(option.rect)
        else:
            QtGui.QItemDelegate.updateEditorGeometry(self, editor, option, index)
        
    def setModelData(self, editor, model, index):
        if type(editor) == QtGui.QComboBox:
            model.setData(index, editor.currentText(), QtCore.Qt.EditRole)
        else:
            QtGui.QItemDelegate.setModelData(self, editor, model, index)

    def editorEvent(self, event, model, option, index):
        
#         if event.type() == QtCore.QEvent.MouseButtonRelease:
#             if index.data() == "0":
#                 model.setData(index, "1", QtCore.Qt.EditRole)
#             else:
#                 model.setData(index, "0", QtCore.Qt.EditRole)
#                 
        return False

            
        
        
        
        