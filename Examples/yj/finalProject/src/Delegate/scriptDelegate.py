#coding=utf-8
'''
Created on 2013-3-7

@author: pyroshow
'''
from PySide import QtGui, QtCore
from UI import rc_picture
#from popupWindow.uiModifyCombination import ModifyCombination

class ScriptDelegate(QtGui.QStyledItemDelegate):
    
    def __init__(self, parent = None):
        QtGui.QStyledItemDelegate.__init__(self, parent)
        self.parent = parent
        
    
        
    def createEditor (self, parent, option, index):
        button = QtGui.QMessageBox.question(parent, "Question", "Are you sure to change?", QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Ok)
        if button == QtGui.QMessageBox.Ok:
            pass
#            customDialog = CustomDialog(id ,parent)
##            accept = customDialog.exec_()
#            customDialog.show()
        elif button == QtGui.QMessageBox.Cancel:
            pass
        else:
            return
        
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
    
    
    
    