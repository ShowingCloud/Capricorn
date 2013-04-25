#coding=utf-8
'''
Created on 2013-1-31

@author: pyroshow
'''

from PySide import QtGui, QtCore
from UI import rc_picture
#from popupWindow.uiModifyCombination import ModifyCombination

class CustomDelegate(QtGui.QStyledItemDelegate):
    
    def __init__(self, parent = None):
        QtGui.QStyledItemDelegate.__init__(self, parent)
        self.parent = parent
    
        
    def createEditor (self, parent, option, index):
        pass
        
#        Id = int(self.parent.model.item(index.row()).text())
#
#        modifyCombination = ModifyCombination(Id, parent)
#        accept = modifyCombination.exec_()
#        if accept == 1:
#            self.parent.model.clear()
#            self.parent.model.setHorizontalHeaderLabels(["UUId", "ID", "Combination Info(Item/Time)"])
#            self.parent.query()
#            self.parent.view.hideColumn(0)
#            
        
    def setEditorData(self, editor, index):
        pass
        
    def setModelData(self, spinBox, model, index):
        pass
        
        
        
        