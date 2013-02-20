#coding=utf-8
'''
Created on 2013-2-19

@author: pyroshow
'''

import sys, rc_picture
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ShapeWidget(QWidget):
    
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        
        pix = QPixmap(":/images/title.png", "0", Qt.AvoidDither|Qt.ThresholdDither|Qt.ThresholdAlphaDither)
        
        self.resize(pix.size())
        self.setMask(pix.mask())
        
        self.dragPosition = None
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
        
        if event.button() == Qt.RightButton:
            self.close()
            
            
    def mouseMoveEvent(self, event):
        
        if event.buttons() & Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()
            
    def paintEvent(self, event):
        painter=QPainter(self)  
        painter.drawPixmap(0,0,QPixmap(":images/title.png")) 
        
app = QApplication(sys.argv)
demo = ShapeWidget()
demo.show()
sys.exit(app.exec_())



