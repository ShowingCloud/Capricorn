#coding=utf-8
'''
Created on 2013-5-8

@author: pyroshow
'''
from PySide import QtGui, QtCore
class ModifyCombinationDelegate(QtGui.QStyledItemDelegate):
    
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
        if index.column() == 0 :
            pass
        elif index.column() == 1 :
            print index.data(), "index.data"
            timeEdit = QtGui.QLineEdit(parent)
            doubleV = QtGui.QDoubleValidator()
            timeEdit.setValidator(doubleV)
            return timeEdit
       
        
    def setEditorData(self, editor, index):
        pass
        
    def setModelData(self, editor, model, index):
        print index.data(), "index.data"
        if editor.text() == "":
            model.setData(index, index.data(), QtCore.Qt.EditRole)
        else:
            model.setData(index, editor.text(), QtCore.Qt.EditRole)


