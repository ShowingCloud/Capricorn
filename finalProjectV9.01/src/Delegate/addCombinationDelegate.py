#coding=utf-8
'''
Created on 2013-5-8

@author: pyroshow
'''
from PySide import QtGui, QtCore
class AddCombinationDelegate(QtGui.QStyledItemDelegate):
    
    def __init__(self,  parent = None):
        QtGui.QStyledItemDelegate.__init__(self, parent)
        self.parent = parent
    
#    #重写自带方法(参数自带)
    def paint(self, painter, option, index):
        
        style = QtGui.QApplication.style()
            
        label = QtGui.QStyleOptionViewItemV4 (option)
        label.text = index.data()
        label.displayAlignment = QtCore.Qt.AlignCenter

        style.drawControl (QtGui.QStyle.CE_ItemViewItem, label, painter)
                
    def createEditor (self, parent, option, index):
        pass
       
        
    def setEditorData(self, editor, index):
        pass
        
    def setModelData(self, editor, model, index):
        pass
