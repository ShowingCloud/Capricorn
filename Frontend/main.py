#coding=utf-8
'''
Created on 2013-10-17

@author: YuJin
'''
from PySide import QtGui
from UI.ui_main import Ui_Form
import sys
from Frontend.firework import Fireworks

class Main(QtGui.QWidget):
    
    def __init__(self, parent = None):
        super(Main, self).__init__()
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.pushButtonProject.clicked.connect(self.editProject)
        self.ui.pushButtonConnect.clicked.connect(self.connectTest)
        self.ui.pushButtonFire.clicked.connect(self.handFire)
        self.ui.pushButtonExit.clicked.connect(self.cancel)
    #连接测试系统
    def connectTest(self):
        pass
    #手动点火系统
    def handFire(self):
        pass
    #工程编辑系统
    def editProject(self):
        self.fireworks = Fireworks()
        self.fireworks.show()
        self.hide()
    #退出
    def cancel(self):
        self.close()
        
def main():
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()

