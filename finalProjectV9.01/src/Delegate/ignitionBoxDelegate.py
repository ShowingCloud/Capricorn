#coding=utf-8
'''
Created on 2013-1-31

@author: pyroshow
'''

from PySide import QtGui, QtCore


class CheckBoxDelegate(QtGui.QStyledItemDelegate):
    
    def __init__(self, parent = None):
        QtGui.QStyledItemDelegate.__init__(self, parent)
        self.parent = parent
        
        self.chkboxSize = 19
        
        
    def createEditor (self, parent, option, index):
        pass
    
    def paint(self, painter, option, index):
        style = QtGui.QApplication.style()
        if index.column() == 5:
            value = index.data() 
            opt = QtGui.QStyleOptionButton()  
            opt.state |= (QtGui.QStyle.State_Enabled if value != "2" else 0) | (QtGui.QStyle.State_On if value == "1" else QtGui.QStyle.State_Off)  
            opt.text = ''  
            left = option.rect.x() + (option.rect.width() - self.chkboxSize) / 2  
            top  = option.rect.y() + (option.rect.height() - self.chkboxSize) / 2  
            opt.rect = QtCore.QRect(left, top, self.chkboxSize, self.chkboxSize)  
            style.drawControl(QtGui.QStyle.CE_CheckBox, opt, painter)
        else:
            label = QtGui.QStyleOptionViewItemV4 (option)
            label.text = index.data()
            label.displayAlignment = QtCore.Qt.AlignCenter

            style.drawControl (QtGui.QStyle.CE_ItemViewItem, label, painter)
    
    def setEditorData(self, editor, index):
        pass
    def updateEditorGeometry(self, editor, option, index):
        pass
        
    def setModelData(self, editor, model, index):
        pass

    def editorEvent(self, event, model, option, index):
        if index.column() == 5:
            if event.type() == QtCore.QEvent.MouseButtonRelease:
                if index.data() == "0":
                    model.setData(index, "1", QtCore.Qt.EditRole)
                elif index.data() == "1":
                    model.setData(index, "0", QtCore.Qt.EditRole)
        else :
            pass
                
        return False
            
        
            
        
        
        
        