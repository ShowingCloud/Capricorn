#coding=utf-8
'''
Created on 2013-1-31

@author: pyroshow
'''

from PySide import QtGui, QtCore
from resources import rc_picture
#from popupWindow.uiCustomDialog import CustomDialog

class CustomDelegate(QtGui.QStyledItemDelegate):
    
    def __init__(self, parent = None):
        QtGui.QStyledItemDelegate.__init__(self, parent)
    
        
    #重写自带方法(参数自带)
    def paint(self, painter, option, index):
        
        style = QtGui.QApplication.style()
        self.rect = option.rect
        self.painter = painter
        if index.column() == 7:
            
            itemLabel = QtGui.QStyleOptionViewItemV4 (option)
            
            if index.data() == 'transparent':
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.transparent)
            
            elif index.data() == 'white':
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.white)
                
            elif index.data() == 'black':
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.black)
                
            elif index.data() == 'red':
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.red)
                
            elif index.data() == 'green':
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.green)
                
            elif index.data() == 'blue':
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.blue)
                
            elif index.data() == 'cyan':   #蓝绿色
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.cyan)
                
            elif index.data() == 'magenta':   #洋红色
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.magenta)
                
            elif index.data() == 'yellow':
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.yellow)
                
            elif index.data() == 'gray':    #灰色
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.gray)
                
            elif index.data() == 'lightGray':
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.lightGray)
                
            style.drawControl (QtGui.QStyle.CE_ItemViewItem, itemLabel, painter)

            
        
        elif index.column() == 8:
#            print option.rect
            if index.data() == '90':
                
                self.changeAngle("jt_90.jpg", 29, 10, 840)
                
            elif index.data() == '0':
                
                self.changeAngle("jt_0.jpg", 10, 29, 840)
                
            elif index.data() == '180':
                
                self.changeAngle("jt_180.jpg", 10, 29, 840)

            elif index.data() == '30':
                
                self.changeAngle("jt_30.jpg", 29, 15, 840)

            elif index.data() == '45':

                self.changeAngle("jt_45.jpg", 29, 15, 840)
                
            elif index.data() == '60':

                self.changeAngle("jt_60.jpg", 29, 15, 840)
                
            elif index.data() == '120':

                self.changeAngle("jt_120.jpg", 29, 15, 840)

            elif index.data() == '135':

                self.changeAngle("jt_135.jpg", 29, 15, 840)

            elif index.data() == '150':

                self.changeAngle("jt_150.jpg", 29, 15, 840)
            
        else:
            label = QtGui.QStyleOptionViewItemV4 (option)
            label.text = index.data()
            label.displayAlignment = QtCore.Qt.AlignCenter

            style.drawControl (QtGui.QStyle.CE_ItemViewItem, label, painter)
            
    #自定义封装方法（设置不同的角度显示）        
    def changeAngle(self, pathStr, height, width, left):
        #直接填充背景颜色
        path1 = "I:\python-workspace\projectV2.0\src\\resources\images\\"
        path = path1+ pathStr
        image = QtGui.QImage(path)
        pixmap = QtGui.QPixmap.fromImage(image)
        #这个是设置象图的长款比例，
        pixmap.scaled(50, 40, QtCore.Qt.KeepAspectRatio)
        self.painter.fillRect(self.rect, QtCore.Qt.white)
            
        self.rect.setHeight(height)
        self.rect.setWidth(width)
        self.rect.moveLeft(left)
        self.painter.drawPixmap(self.rect, pixmap)
            
    def createEditor (self, parent, option, index):
        pass
#        if index.column() == 7:
#            editor = QtGui.QSpinBox(parent)
#            editor.setMinimum(0)
#            editor.setMaximum(10)
#            
#            return editor
#        
#        
#        elif index.column() == 8:
#            pass
#        
#        else :
#            pass
        
    
    def setEditorData(self, editor, index):
        pass
#        value = index.model().data(index, QtCore.Qt.EditRole)
#        editor.setValue(int(value))
        
    def setModelData(self, spinBox, model, index):
        pass
#        spinBox.interpretText()
#        value = spinBox.value()
#
#        model.setData(index, value, QtCore.Qt.EditRole)
    
    