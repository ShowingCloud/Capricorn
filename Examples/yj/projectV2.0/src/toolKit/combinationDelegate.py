#coding=utf-8
'''
Created on 2013-1-31

@author: pyroshow
'''

from PySide import QtGui, QtCore
from resources import rc_picture
from popupWindow.uiCombinationDialog import CombinationDialog

class CombinationDelegate(QtGui.QStyledItemDelegate):
    
    def __init__(self, parent = None):
        QtGui.QStyledItemDelegate.__init__(self, parent)
    
        
    def createEditor (self, parent, option, index):
        
        combinationDialog = CombinationDialog("", parent)
        accept = combinationDialog.exec_()
        if accept == 1:
            p = parent
            p.model.clear()
            p.model.setHorizontalHeaderLabels(["ID", "Combination Info(Item/Time)"])
            p.query()
        
    def setEditorData(self, editor, index):
#        value = index.model().data(index, QtCore.Qt.EditRole)
#        editor.setValue(int(value))
        pass
        
    def setModelData(self, spinBox, model, index):
        pass
#        spinBox.interpretText()
#        value = spinBox.value()
#
#        model.setData(index, value, QtCore.Qt.EditRole)
        
        
        
        