#coding=utf-8
'''
Created on 2013-2-22

@author: pyroshow
'''
from PySide.QtGui import *
from PySide.QtCore import *

#产生渐变的格式
class FaderWidget(QWidget):
    
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        
        if parent:
            self.startColor=parent.palette().window().color()  
        else:
            self.startColor = Qt.white
            
        self.currentAlpha = 0
        self.duration = 1000
        
        self.timer = QTimer(self)
        self.connect(self.timer, SIGNAL("timeout()"), self.update)
        #设置FaderWidget的窗体属性为Qt.WA_DeleteOnClose，当整个对话框关闭时，此渐变窗体也同时关闭。
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.resize(parent.size())
        
    def start(self):
        self.currentAlpha = 255
        self.timer.start(100)
        self.show()
        
    def paintEvent(self, event):
        #半透明色
        semiTransparentColor = self.startColor
        semiTransparentColor.setAlpha(self.currentAlpha)
        
        painter = QPainter(self)
        painter.fillRect(self.rect(), semiTransparentColor)
        
        self.currentAlpha -= (255*self.timer.interval()/self.duration)
        
        if self.currentAlpha <= 0:  
            self.timer.stop()  
            self.close() 