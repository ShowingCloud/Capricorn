#coding=utf-8
'''
Created on 2013-1-31

@author: pyroshow
'''

from PySide import QtGui, QtCore
#from UI import rc_picture
from UI.ui_CustomDatabaseShow import uiCustomShow

class MergeDelegate(QtGui.QStyledItemDelegate):
    
    def __init__(self, sess,  parent = None):
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
        button = QtGui.QMessageBox.question(parent, "Question", "The fireworks database resources data do not give change, want to modify the add to custom fireworks library, sure?", QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Ok)
        if button == QtGui.QMessageBox.Ok:
            pass
            customShow = uiCustomShow(self.sess, UUID ,parent)
            customShow.show()
        elif button == QtGui.QMessageBox.Cancel:
            pass
        else:
            return
    
    def setEditorData(self, editor, index):
        pass
#        value = index.model().data(index, QtCore.Qt.EditRole)
#        editor.setValue(int(value))
        
    def setModelData(self, editor, model, index):
        pass
#        spinBox.interpretText()
#        value = spinBox.value()
#
#        model.setData(index, value, QtCore.Qt.EditRole)
    
    
