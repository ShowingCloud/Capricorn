#coding=utf-8
'''
Created on 2013-1-31

@author: pyroshow
'''

from PySide import QtGui, QtCore
from tuesday import rc_picture

class MergeDelegate(QtGui.QStyledItemDelegate):
    
    def __init__(self, parent = None):
        QtGui.QStyledItemDelegate.__init__(self, parent)
    
        
    #重写自带方法(参数自带)
    def paint(self, painter, option, index):
        
        style = QtGui.QApplication.style()
        
        if index.column() == 6:
            
            itemLabel = QtGui.QStyleOptionViewItemV4 (option)
            
            if index.data() == 0:
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.transparent)
            
            elif index.data() == 1:
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.white)
                
            elif index.data() == 2:
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.black)
                
            elif index.data() == 3:
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.red)
                
            elif index.data() == 4:
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.green)
                
            elif index.data() == 5:
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.blue)
                
            elif index.data() == 6:   #蓝绿色
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.cyan)
                
            elif index.data() == 7:   #洋红色
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.magenta)
                
            elif index.data() == 8:
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.yellow)
                
            elif index.data() == 9:    #灰色
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.gray)
                
            elif index.data() == 10:
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.lightGray)
                
            style.drawControl (QtGui.QStyle.CE_ItemViewItem, itemLabel, painter)

            
        
        elif index.column() == 7:
            #直接填充背景颜色
            path1 = "I:\python-workspace\project\src\\resources\images\\"
#            print option.rect
            #自定义封装方法（设置不同的角度显示）
            def changeAngle(pathStr, height, width, left):
                path = path1+ pathStr
                image = QtGui.QImage(path)
                pixmap = QtGui.QPixmap.fromImage(image)
                #这个是设置象图的长款比例，
                pixmap.scaled(50, 40, QtCore.Qt.KeepAspectRatio)
                painter.fillRect(option.rect, QtCore.Qt.white)
                rect = option.rect
                rect.setHeight(height)
                rect.setWidth(width)
                rect.moveLeft(left)
                painter.drawPixmap(rect, pixmap)
                
            if index.data() == "90":
                
                changeAngle("jt_90.jpg", 29, 10, 940)
                
            elif index.data() == "0":
                
                changeAngle("jt_0.jpg", 10, 29, 940)
                
            elif index.data() == "180":
                
                changeAngle("jt_180.jpg", 10, 29, 940)

            elif index.data() == "30":
                
                changeAngle("jt_30.jpg", 29, 15, 940)

            elif index.data() == "45":

                changeAngle("jt_45.jpg", 29, 15, 940)
                
            elif index.data() == "60":

                changeAngle("jt_60.jpg", 29, 15, 940)
                
            elif index.data() == "120":

                changeAngle("jt_120.jpg", 29, 15, 940)

            elif index.data() == "135":

                changeAngle("jt_135.jpg", 29, 15, 940)

            elif index.data() == "150":

                changeAngle("jt_150.jpg", 29, 15, 940)
            
        else:
            label = QtGui.QStyleOptionViewItemV4 (option)
            label.text = index.data()
            label.displayAlignment = QtCore.Qt.AlignCenter

            style.drawControl (QtGui.QStyle.CE_ItemViewItem, label, painter)
            
    def createEditor (self, parent, option, index):
        pass 
           
    
    
