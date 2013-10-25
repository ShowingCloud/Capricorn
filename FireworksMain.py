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
from Translations.tr_rc import *
from Frontend.firework import Firework
from config import basedir

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
        
    
    def connectTest(self):
        self.connectTestForm = ConnectTestWin(self.showSignal)
        self.connectTestForm.show()
        self.hide()
    
    def handFire(self):
        self.fireNowWin = FireNowWin(self.showSignal)
        self.fireNowWin.show()
        self.hide()
    
    def editProject(self):
        self.fireworks = Firework(self.showSignal)
        self.fireworks.show()
        self.hide()
        
    
    def cancel(self):
        self.close()
        
    def showAgain(self):
        self.show()
        
def main():
    app = QtGui.QApplication(sys.argv)
    locale = QtCore.QLocale.system().name()
    appTranslator = QtCore.QTranslator()
    if appTranslator.load (":/Fireworks_" + locale):
        app.installTranslator (appTranslator)
    app.addLibraryPath (basedir)
    window = Main()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()

