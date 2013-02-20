#coding=utf-8
'''
Created on 2013-1-31

@author: pyroshow
'''

from PySide import QtGui, QtCore
from resources import rc_picture

class MergeDelegate(QtGui.QStyledItemDelegate):
    
    def __init__(self, parent = None):
        QtGui.QStyledItemDelegate.__init__(self, parent)
    
        
    #重写自带方法(参数自带)
    def paint(self, painter, option, index):
        
        style = QtGui.QApplication.style()
        
        if index.column() == 8:
            
            itemLabel = QtGui.QStyleOptionViewItemV4 (option)
            
            if index.data() == "white":
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.white)
                
            elif index.data() == "black":
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.black)
                
            elif index.data() == "red":
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.red)
                
            elif index.data() == "darkRed":
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.darkRed)
                
            elif index.data() == "green":
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.green)
                
            elif index.data() == "darkGreen":
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.darkGreen)
                
            elif index.data() == "blue":
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.blue)
                
            elif index.data() == "darkBlue":
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.darkBlue)
                
            elif index.data() == "cyan":   #蓝绿色
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.cyan)
                
            elif index.data() == "darkCyan":
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.darkCyan)
                
            elif index.data() == "magenta":   #洋红色
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.magenta)
                
            elif index.data() == "darkMagenta":
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.darkMagenta)
                
            elif index.data() == "yellow":
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.yellow)
                
            elif index.data() == "darkYellow":
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.darkYellow)
                
            elif index.data() == "gray":    #灰色
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.gray)
                
            elif index.data() == "darkGray":
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.darkGray)
                
            elif index.data() == "lightGray":
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.lightGray)
                
            elif index.data() == "transparent":
                itemLabel.backgroundBrush = QtGui.QBrush(QtCore.Qt.transparent)
                
            style.drawControl (QtGui.QStyle.CE_ItemViewItem, itemLabel, painter)

            
        
        elif index.column() == 9:
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
            
#    def createEditor (self, parent, option, index):
#        pass 
           
    
    
