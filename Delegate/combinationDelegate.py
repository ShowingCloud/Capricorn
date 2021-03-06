#coding=utf-8
'''
Created on 2013-1-31

@author: pyroshow
'''

from PySide import QtGui, QtCore
from UI import rc_picture
from UI.ui_modifyCombination import ModifyCombination

class CombinationDelegate(QtGui.QStyledItemDelegate):
    
    def __init__(self, sess, parent = None):
        QtGui.QStyledItemDelegate.__init__(self, parent)
        self.parent = parent
        self.sess = sess
    
#    #重写自带方法(参数自带)
    def paint(self, painter, option, index):
        
        style = QtGui.QApplication.style()
            
        label = QtGui.QStyleOptionViewItemV4 (option)
        label.text = index.data()
        label.displayAlignment = QtCore.Qt.AlignCenter

        style.drawControl (QtGui.QStyle.CE_ItemViewItem, label, painter)
                
    def createEditor (self, parent, option, index):
        
        UUID = self.parent.model.item(index.row()).text()

        modifyCombination = ModifyCombination(self.sess, UUID, parent)
        accept = modifyCombination.exec_()
        if accept == 1:
            self.parent.model.clear()
            self.parent.model.setHorizontalHeaderLabels(["UUID", "ID", "Contents", "Total Time (sec)"])
            self.parent.query()
            self.parent.view.hideColumn(0)
            
        
    def setEditorData(self, editor, index):
        pass
        
    def setModelData(self, spinBox, model, index):
        pass
        
        
        
        