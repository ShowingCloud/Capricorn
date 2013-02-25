#coding=utf-8
'''
Created on 2013-2-22

@author: pyroshow
'''

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtSql import *
from faderWidget.FaderWidget import FaderWidget
from fireworks.Fireworks import Fireworks
from script.Script import Script
from combination.Combination import Combination



class MainDialog(QDialog):
    
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        
        self.setWindowTitle(u"综合显示")
        self.setWindowIcon(QIcon(":/images/title.png"))
        #设置分离器为水平方向
        mainSplitter = QSplitter(Qt.Horizontal)
        #设置分离器为不透明的
        mainSplitter.setOpaqueResize(True)
        
        self.listWidget = QListWidget(mainSplitter)
        self.listWidget.insertItem(0, u"礼花弹类")
        self.listWidget.insertItem(1, u"小礼花类")
        self.listWidget.insertItem(2, u"旋转升空类")
        self.listWidget.insertItem(3, u"烟雾类")
        self.listWidget.insertItem(4, u"组合类烟花")
        self.listWidget.insertItem(5, u"自定义烟花")
        self.listWidget.setSpacing(4)
        
        frame = QFrame(mainSplitter)
        frame.resize(1150, 380)
        
        self.stack = QStackedWidget()
        #设置栈窗口的格式为内嵌凸起的
        self.stack.setFrameStyle(QFrame.Panel | QFrame.Raised)
        
        
        combination = Combination()
        script = Script()
        a = Fireworks('A')
        b = Fireworks('B')
        c = Fireworks('C')
        d = Fireworks('D')
        self.stack.addWidget(a)
        self.stack.addWidget(b)
        self.stack.addWidget(c)
        self.stack.addWidget(d)
        self.stack.addWidget(combination)
        self.stack.addWidget(script)
        
        amendBtn = QPushButton(u"导出")
        closeBtn = QPushButton(u"关闭")
        
        
        btnLayout = QHBoxLayout()
        #可伸缩的
        btnLayout.addStretch(1)
        btnLayout.addWidget(amendBtn)
        btnLayout.addWidget(closeBtn)
        
        mainLayout = QVBoxLayout(frame)
        mainLayout.setSpacing(6)
        mainLayout.addWidget(self.stack)
        mainLayout.addLayout(btnLayout)
        mainLayout.setStretchFactor(self.stack, 1)
        
        self.connect(self.listWidget, SIGNAL("currentRowChanged(int)"), self.stack, SLOT("setCurrentIndex(int)"))
        self.connect(closeBtn, SIGNAL("clicked()"), self, SLOT("close()"))
        
        layout = QHBoxLayout(self)
        layout.addWidget(mainSplitter)
        self.setLayout(layout)
        
        self.faderWidget = None
        self.connect(self.listWidget, SIGNAL("currentItemChanged(QListWidgetItem, QListWidgetItem)"), self.changePage)
        self.connect(self.stack, SIGNAL("currentChanged(int)"), self.fadeInWidget)
        
        self.resize(1200, 400)
        
    def changePage(self, current,previous):
        if not current:
            current = previous
            
        self.stack.setCurrentWidget(current)
    
    def fadeInWidget(self, index):
        
        self.faderWidget = FaderWidget(self.stack.widget(index))
        self.faderWidget.start()



if __name__ == "__main__" : 
    app=QApplication(sys.argv) 
    demo=MainDialog()  
    demo.show()  
    sys.exit(app.exec_()) 







