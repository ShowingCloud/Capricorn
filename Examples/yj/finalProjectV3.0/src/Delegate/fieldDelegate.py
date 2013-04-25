#coding=utf-8
'''
Created on 2013-3-15

@author: pyroshow
'''

from PySide import QtGui

class FieldDelegate(QtGui.QStyledItemDelegate):
    
    def __init__(self, parent = None):
        QtGui.QStyledItemDelegate.__init__(self, parent)
        self.parent = parent
        
        
    def createEditor (self, parent, option, index):
#        self.UUID = self.parent.model.item(index.row().text())
        pass
        
    def setEditorData(self, editor, index):
        pass
        
    def setModelData(self, spinBox, model, index):
        pass



