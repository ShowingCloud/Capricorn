#coding=utf-8
'''
Created on 2013-10-17

@author: YuJin
'''
from PySide import QtGui, QtCore
from UI.ui_main import Ui_Form
from Frontend.fireNow import UiShow as FireNowWin
from Frontend.connectTest import UiShow as ConnectTestWin
import sys
from Frontend.firework import Fireworks

class Main(QtGui.QWidget):
    showSignal = QtCore.Signal()
    def __init__(self, parent = None):
        super(Main, self).__init__()
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.pushButtonProject.clicked.connect(self.editProject)
        self.ui.pushButtonConnect.clicked.connect(self.connectTest)
        self.ui.pushButtonFire.clicked.connect(self.handFire)
        self.ui.pushButtonExit.clicked.connect(self.cancel)
        
        self.showSignal.connect(self.showAgain)
        
    #连接测试系统
    def connectTest(self):
        self.connectTestForm = ConnectTestWin(self.showSignal)
        self.connectTestForm.show()
        self.hide()
    #手动点火系统
    def handFire(self):
        self.fireNowWin = FireNowWin(self.showSignal)
        self.fireNowWin.show()
        self.hide()
    #工程编辑系统
    def editProject(self):
        self.fireworks = Fireworks(self.showSignal)
        self.fireworks.show()
        self.hide()
        
    #退出
    def cancel(self):
        self.close()
        
    def showAgain(self):
        self.show()
        
def main():
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()

