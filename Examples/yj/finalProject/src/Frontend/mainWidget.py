#coding=utf-8
'''
Created on 2013-3-6

@author: pyroshow
'''

from Frontend.FaderWidget import FaderWidget
from PySide.QtCore import *
from PySide.QtGui import *
from UI import rc_picture
#from UI.ui_chooseSize import ChooseSizeWidget
from UI.ui_combinationFireworks import Combination
from UI.ui_customFireworks import Custom
from UI.ui_fieldList import FieldListWidget
from UI.ui_fireworks import Fireworks
#from UI.ui_screening import ScreeningWidget
from UI.ui_script import Script
from UI.ui_typeList import TypeListWidget
import sys

class MainWidget(QWidget):
    
    def __init__(self, parent = None):
        QWidget.__init__(self,parent)
        
        self.setWindowTitle(u"综合显示")
        self.setWindowIcon(QIcon(":/images/title.png"))
        
        self.fireworksGroup = QGroupBox("Database")
        
        self.typeList = TypeListWidget()
#        self.screening = ScreeningWidget()
#        self.chooseSize = ChooseSizeWidget()
        
#        vbox1 = QVBoxLayout()
#        vbox1.addWidget(self.typeList)
#        vbox1.addWidget(self.chooseSize)
#        vbox1.addWidget(self.screening)
        
        self.fireworksStack = QStackedWidget()
        
        #设置栈窗口的格式为内嵌凸起的
        self.fireworksStack.setFrameStyle(QFrame.Panel | QFrame.Raised)
        
        
        self.fireworksA = Fireworks("A")
        self.fireworksB = Fireworks("B")
        self.fireworksC = Fireworks("C")
        self.fireworksD = Fireworks("D")
        self.combinationFireworks = Combination()
        self.customFireworks = Custom()
        
        self.fireworksStack.addWidget(self.fireworksA)
        self.fireworksStack.addWidget(self.fireworksB)
        self.fireworksStack.addWidget(self.fireworksC)
        self.fireworksStack.addWidget(self.fireworksD)
        self.fireworksStack.addWidget(self.combinationFireworks)
        self.fireworksStack.addWidget(self.customFireworks)
        
        hbox1 = QHBoxLayout()
#        hbox1.addLayout(vbox1)
        hbox1.addWidget(self.typeList)
        hbox1.addWidget(self.fireworksStack, 1)
        
        self.fireworksGroup.setLayout(hbox1)
        
        self.scriptGroup = QGroupBox("Script")
        
        self.fieldList = FieldListWidget()
        self.scriptStack = QStackedWidget()
        
        self.scriptStack.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.fieldFirst = Script("1")
        self.fieldSecond = Script("2")
        self.fieldThird = Script("3")
        self.fieldFour = Script("4")
        self.fieldFive = Script("5")
        self.fieldSix = Script("6")
        self.scriptStack.addWidget(self.fieldFirst)
        self.scriptStack.addWidget(self.fieldSecond)
        self.scriptStack.addWidget(self.fieldThird)
        self.scriptStack.addWidget(self.fieldFour)
        self.scriptStack.addWidget(self.fieldFive)
        self.scriptStack.addWidget(self.fieldSix)
        
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.fieldList)
        hbox2.addWidget(self.scriptStack, 1)
        self.scriptGroup.setLayout(hbox2)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.fireworksGroup)
        mainLayout.addWidget(self.scriptGroup)
        self.setLayout(mainLayout)
        self.resize(1680, 800)
        
        self.faderWidget = None
        
        self.connect(self.fireworksStack, SIGNAL("currentChanged(int)"), self.fadeInFireworks)
        self.connect(self.scriptStack, SIGNAL("currentChanged(int)"), self.fadeInScript)
        
        self.typeList.listWidget.currentItemChanged.connect(self.changeTypePage)
        self.fieldList.listWidget.currentItemChanged.connect(self.changeFieldPage)
        
#        self.screening.filterPatternLineEdit.textChanged.connect(self.filterRegExpChanged)
#        self.chooseSize.sizeGroup.buttonClicked.connect(self.getSize)

#        self.refreshScript()
        
    #实现标签的变换
    def changeTypePage(self, current, previous):
        if not current:
            current = previous

        self.fireworksStack.setCurrentIndex(self.typeList.listWidget.row(current))
        
        self.combinationFireworks.model.clear()
        self.combinationFireworks.model.setHorizontalHeaderLabels(["UUID", "ID", "Combination Info(Item/Time)"])
        self.combinationFireworks.query()
        self.combinationFireworks.view.hideColumn(0)
        
        
    def changeFieldPage(self, current, previous):
        if not current:
            current = previous

        self.scriptStack.setCurrentIndex(self.fieldList.listWidget.row(current))
        
        self.requeryScript()
        
        
    #实现明暗的变换
    def fadeInFireworks(self, index):
        
        self.faderWidget = FaderWidget(self.fireworksStack.widget(index))
        self.faderWidget.start()
        
    def fadeInScript(self, index):
        
        self.faderWidget = FaderWidget(self.scriptStack.widget(index))
        self.faderWidget.start()
        
    def requeryScript(self):
        self.fieldFirst.model.clear()
        self.fieldFirst.model.setHorizontalHeaderLabels(["UUID", "Name", "Alias", "Size", "Ignition Time", "Rising Time(s)", "Effect Time", "Ignition ID", "Connector ID", "Information", "Notes"])
        self.fieldFirst.query(self.fieldFirst.Type)
        self.fieldFirst.view.hideColumn(0)
        
        self.fieldSecond.model.clear()
        self.fieldSecond.model.setHorizontalHeaderLabels(["UUID", "Name", "Alias", "Size", "Ignition Time", "Rising Time(s)", "Effect Time", "Ignition ID", "Connector ID", "Information", "Notes"])
        self.fieldSecond.query(self.fieldSecond.Type)
        self.fieldSecond.view.hideColumn(0)
        
        self.fieldThird.model.clear()
        self.fieldThird.model.setHorizontalHeaderLabels(["UUID", "Name", "Alias", "Size", "Ignition Time", "Rising Time(s)", "Effect Time", "Ignition ID", "Connector ID", "Information", "Notes"])
        self.fieldThird.query(self.fieldThird.Type)
        self.fieldThird.view.hideColumn(0)
        
        self.fieldFour.model.clear()
        self.fieldFour.model.setHorizontalHeaderLabels(["UUID", "Name", "Alias", "Size", "Ignition Time", "Rising Time(s)", "Effect Time", "Ignition ID", "Connector ID", "Information", "Notes"])
        self.fieldFour.query(self.fieldFour.Type)
        self.fieldFour.view.hideColumn(0)
        
        self.fieldFive.model.clear()
        self.fieldFive.model.setHorizontalHeaderLabels(["UUID", "Name", "Alias", "Size", "Ignition Time", "Rising Time(s)", "Effect Time", "Ignition ID", "Connector ID", "Information", "Notes"])
        self.fieldFive.query(self.fieldFive.Type)
        self.fieldFive.view.hideColumn(0)
        
        self.fieldSix.model.clear()
        self.fieldSix.model.setHorizontalHeaderLabels(["UUID", "Name", "Alias", "Size", "Ignition Time", "Rising Time(s)", "Effect Time", "Ignition ID", "Connector ID", "Information", "Notes"])
        self.fieldSix.query(self.fieldSix.Type)
        self.fieldSix.view.hideColumn(0)
        
#    def refreshScript(self):
#        
#        if self.fireworksA.acc == 1 or self.fireworksB.acc == 1 or self.fireworksC.acc == 1 or self.fireworksD.acc == 1:
#            self.requeryScript()
#            print "**********"
        
            
        
        
if __name__ == "__main__" : 
    app=QApplication(sys.argv) 
    demo=MainWidget()  
    demo.show()  
    sys.exit(app.exec_())
        
        
    