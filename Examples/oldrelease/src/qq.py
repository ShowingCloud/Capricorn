#coding=utf-8

'''
Created on 2013-2-16

@author: Pyroshow
'''
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MyQQ(QToolBox):
    def __init__(self,parent=None):
        super(MyQQ, self).__init__(parent)
        self.setWindowTitle('QQ2013')
        self.setWindowIcon(QIcon('QQ.png'))
#        self.setAutoFillBackground(True)
#        QPalette().setBrush(self.backgroundRole(), QBrush('myplayer.png'))
#        self.setPalette(QPalette())
        
        toolButton1_1 = QToolButton()
        toolButton1_1.setText(u'子')
        toolButton1_1.setIcon(QIcon('11.png'))
        toolButton1_1.setIconSize(QSize(60, 60))
        toolButton1_1.setAutoRaise(True)
        toolButton1_1.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        toolButton1_2 = QToolButton()
        toolButton1_2.setText(u'丑')
        toolButton1_2.setIcon(QIcon('12.png'))
        toolButton1_2.setIconSize(QSize(60, 60))
        toolButton1_2.setAutoRaise(True)
        toolButton1_2.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        toolButton1_3 = QToolButton()
        toolButton1_3.setText(u'寅')
        toolButton1_3.setIcon(QIcon('13.png'))
        toolButton1_3.setIconSize(QSize(60, 60))
        toolButton1_3.setAutoRaise(True)
        toolButton1_3.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        toolButton1_4 = QToolButton()
        toolButton1_4.setText(u'卯')
        toolButton1_4.setIcon(QIcon('14.png'))
        toolButton1_4.setIconSize(QSize(60, 60))
        toolButton1_4.setAutoRaise(True)
        toolButton1_4.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        toolButton1_5 = QToolButton()
        toolButton1_5.setText(u'辰')
        toolButton1_5.setIcon(QIcon('15.png'))
        toolButton1_5.setIconSize(QSize(60, 60))
        toolButton1_5.setAutoRaise(True)
        toolButton1_5.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        toolButton2_1 = QToolButton()
        toolButton2_1.setText(u'巳')
        toolButton2_1.setIcon(QIcon('21.png'))
        toolButton2_1.setIconSize(QSize(60, 60))
        toolButton2_1.setAutoRaise(True)
        toolButton2_1.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        toolButton2_2 = QToolButton()
        toolButton2_2.setText(u'午')
        toolButton2_2.setIcon(QIcon('22.png'))
        toolButton2_2.setIconSize(QSize(60, 60))
        toolButton2_2.setAutoRaise(True)
        toolButton2_2.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        toolButton2_3 = QToolButton()
        toolButton2_3.setText(u'未')
        toolButton2_3.setIcon(QIcon('23.png'))
        toolButton2_3.setIconSize(QSize(60, 60))
        toolButton2_3.setAutoRaise(True)
        toolButton2_3.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        groupbox1 = QGroupBox()
        vlayout1 = QVBoxLayout(groupbox1)
        vlayout1.setMargin(10)
        vlayout1.setAlignment(Qt.AlignCenter)
        vlayout1.addWidget(toolButton1_1)
        vlayout1.addWidget(toolButton1_2)
        vlayout1.addWidget(toolButton1_3)
        vlayout1.addWidget(toolButton1_4)
        vlayout1.addWidget(toolButton1_5)
        vlayout1.addStretch()
        
        groupbox2 = QGroupBox()
        vlayout2 = QVBoxLayout(groupbox2)
        vlayout2.setMargin(10)
        vlayout2.setAlignment(Qt.AlignCenter)
        vlayout2.addWidget(toolButton2_1)
        vlayout2.addWidget(toolButton2_2)
        vlayout2.addWidget(toolButton2_3)
        
        self.addItem(groupbox1, u"A")
        self.addItem(groupbox2, u"地")
        
app = QApplication(sys.argv)
myqq = MyQQ()
myqq.show()
sys.exit(app.exec_())