#coding=utf-8
'''
Created on 2013-3-6

@author: pyroshow
'''
from Frontend.FaderWidget import FaderWidget
from Models.EngineeringDB import FieldsData
from PySide.QtCore import *
from PySide.QtGui import *
from UI import rc_picture
from UI.ui_combinationFireworks import Combination
from UI.ui_customFireworks import Custom
from UI.ui_fieldDirector import FieldDirectory
from UI.ui_fireworks import Fireworks
from UI.ui_script import Script
from UI.ui_typeList import TypeListWidget
#import sys

class MainWidget(QWidget):
    musicSignal = Signal()
    
    def __init__(self, sess, session, fieldUUID, parent = None):
        QWidget.__init__(self, parent)
        
        self.setWindowTitle(u"综合显示")
        self.setWindowIcon(QIcon(":/images/title.png"))
        
        self.fireworksGroup = QGroupBox("Database")
        self.fireworksGroup.setContentsMargins(-10,0,-10,-10)
        
        self.sess = sess
        self.session = session
        self.fieldUUID = fieldUUID
        
        self.typeList = TypeListWidget()
        
        self.fireworksStack = QStackedWidget()
        
        self.fireworksStack.setContentsMargins(0, 0, 0, 0)
        
        #设置栈窗口的格式为内嵌凸起的
#        self.fireworksStack.setFrameStyle(QFrame.Panel | QFrame.Raised)
        
        
        self.fireworksA = Fireworks("A", self.sess, self.session, self.musicSignal)
        self.fireworksB = Fireworks("B", self.sess, self.session, self.musicSignal)
        self.fireworksC = Fireworks("C", self.sess, self.session, self.musicSignal)
        self.fireworksD = Fireworks("D", self.sess, self.session, self.musicSignal)
        self.combinationFireworks = Combination(self.sess, self.session, self.musicSignal)
        self.customFireworks = Custom(self.sess, self.session, self.musicSignal)
        
        self.fireworksStack.addWidget(self.fireworksA)
        self.fireworksStack.addWidget(self.fireworksB)
        self.fireworksStack.addWidget(self.fireworksC)
        self.fireworksStack.addWidget(self.fireworksD)
        self.fireworksStack.addWidget(self.combinationFireworks)
        self.fireworksStack.addWidget(self.customFireworks)
        
        hbox1 = QHBoxLayout()
        hbox1.setSpacing(0)
        hbox1.addWidget(self.typeList)
        hbox1.addWidget(self.fireworksStack, 1)
        
        self.fireworksGroup.setLayout(hbox1)
        
        self.scriptGroup = QGroupBox("Project")
        self.scriptGroup.setContentsMargins(-10,0,-10,-10)
        
        self.fieldList = FieldDirectory(self.session, self.fieldUUID)
        
        self.script = Script(self.sess, self.session,self.musicSignal)
        with self.session.begin():
            data = self.session.query(FieldsData).filter_by(UUID = self.fieldUUID).first()
        self.script.query(data.FieldID)
        
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.fieldList)
        hbox2.addWidget(self.script, 1)
        hbox2.setSpacing(0)
        self.scriptGroup.setLayout(hbox2)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.fireworksGroup)
        mainLayout.addWidget(self.scriptGroup)
        self.setLayout(mainLayout)
        self.resize(1680, 800)
        
        self.faderWidget = None
        
        self.connect(self.fireworksStack, SIGNAL("currentChanged(int)"), self.fadeInFireworks)
        
        self.typeList.listWidget.currentItemChanged.connect(self.changeTypePage)
        
        self.fieldList.view.clicked.connect(self.showScript)
        
        

        
    #实现标签的变换
    def changeTypePage(self, current, previous):
        if not current:
            current = previous

        self.fireworksStack.setCurrentIndex(self.typeList.listWidget.row(current))
        
        self.combinationFireworks.model.clear()
        self.combinationFireworks.model.setHorizontalHeaderLabels(["UUID", "ID", "Contents", "Total Time (sec)"])
        self.combinationFireworks.query()
        self.combinationFireworks.view.hideColumn(0)
        
        
        self.customFireworks.model.clear()
        self.customFireworks.model.setHorizontalHeaderLabels(["UUID","Size (mm)", "Supplier", "Name", "Alias", "Rising Time", "Stock", "Weight Net", "Weight Gross", "Application", "Safety Distance Horizontal", "Safety Distance Vertical", "Information", "Price", "Notes"])
        self.customFireworks.query()
        self.customFireworks.proxyView.hideColumn(0)
        
        
    #实现明暗的变换
    def fadeInFireworks(self, index):
        
        self.faderWidget = FaderWidget(self.fireworksStack.widget(index))
        self.faderWidget.start()
        
        
    def showScript(self, index):
        #阵地号的UUID
        self.FieldID = self.fieldList.model.item(index.row(), 1).text()
        self.requery()
#        self.timer = QTimer()
#        self.connect(self.timer, SIGNAL("timeout()"), self.requery)
#        self.timer.start(5000)
        
    def requery(self):
        self.script.model.clear()
        self.script.model.setHorizontalHeaderLabels(["UUID", "FieldID", "Ignition Time", "Rising Time(s)", "Effect Time", "Name", "Size (mm)",  "Ignition ID",  "Tilt Angle", "Information", "Notes"])
        self.script.query(self.FieldID)
        self.script.view.hideColumn(0)
        self.script.view.hideColumn(1)
        
#if __name__ == "__main__" : 
#    app=QApplication(sys.argv) 
#    demo=MainWidget()  
#    demo.show()  
#    sys.exit(app.exec_())
        
        
    