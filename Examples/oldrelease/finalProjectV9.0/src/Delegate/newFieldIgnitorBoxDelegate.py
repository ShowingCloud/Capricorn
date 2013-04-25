from PySide import QtGui, QtCore

class ignitorBoxDelegate(QtGui.QStyledItemDelegate):
    
    def __init__(self, parent = None):
        QtGui.QStyledItemDelegate.__init__(self, parent)
        self.parent = parent
        
        
        
    def createEditor (self, parent, option, index):
        pass
    
    def paint(self, painter, option, index):
        style = QtGui.QApplication.style()
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
        return False
    
            
        
            