#coding=utf-8
'''
Created on 2013-10-11

@author: YuJin
'''

from PySide import QtGui, QtCore

class LocalDelegate(QtGui.QStyledItemDelegate):
    
    def __init__(self, parent = None):
        QtGui.QStyledItemDelegate.__init__(self, parent)
        self.parent = parent
    
        
#    #重写自带方法(参数自带)
    def paint(self, painter, option, index):
        
        style = QtGui.QApplication.style()
            
        label = QtGui.QStyleOptionViewItemV4 (option)
        
        if index.column() == 1:
            label.text = index.data()
        else:
            label.text = str(index.data())
        label.displayAlignment = QtCore.Qt.AlignCenter

        style.drawControl (QtGui.QStyle.CE_ItemViewItem, label, painter)
            
    def createEditor (self, parent, option, index):
        pass
    
    def setEditorData(self, editor, index):
        pass
        
    def setModelData(self, editor, model, index):
        pass
