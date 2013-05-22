#from Migrate.DBScript import upgrade
from PySide import QtGui
from UI.FirePositionShow import FirePositionShow
from UI.ImportProjectShow import ImportProjectShow
from UI.LoginShow import loginShow
from UI.WinShow import MainShow
from UI.newProjectShow import newProjectShow
import sys

class UiControl():
    def __init__(self):
        #Upgrading the database call function, Calls must be upgraded
#        upgrade()
        self.loginWin = loginShow()
        self.loginWin.show()
        self.loginWin.ui.pushButtonImport.clicked.connect(self.importProject)
        self.loginWin.ui.pushButtonSave.clicked.connect(self.fieldEdit)
        
    def importProject(self): 
        if self.loginWin.loginFlag == "Success" :
            self.sess = self.loginWin.sess
            self.importProjectWin = ImportProjectShow(self.sess)
            self.importProjectWin.ui.pushButtonSave.clicked.connect(self.mainWindow)
            self.importProjectWin.show()
            self.loginWin.close()
        else:
            QtGui.QMessageBox.question(None,'message','Please login first',QtGui.QMessageBox.Ok)
            
            
    def fieldEdit(self):
        self.loginWin.save()
        if self.loginWin.loginFlag != "Success" or self.loginWin.nameFlag == 'used':
            return
        self.sess = self.loginWin.sess
        self.fieldWin = FirePositionShow(self.sess, self.loginWin.UUID,self.loginWin.path)
        self.fieldWin.ui.pushButtonDone.clicked.connect(self.fieldToMainWin)
        self.fieldWin.show()
        self.loginWin.close()
        
    def fieldToMainWin(self):
        self.fieldWin.next()
        if self.fieldWin.confirmFlag == False:
            return
        self.mainWin = MainShow(self.sess, self.fieldWin.session, self.fieldWin.fieldUUID,self.fieldWin.musicPath)
        self.fieldWin.close()
        self.mainWin.show()
        self.mainWin.ui.actionNewOrOpen.triggered.connect(self.newOrOpenProject)
        
    def mainWindow(self):
        self.importProjectWin.save()
        if self.importProjectWin.ui.lineEditMusic.text() == '':
            return
        self.session = self.importProjectWin.session
        self.mainWin = MainShow(self.sess, self.session, self.importProjectWin.fieldUUID,self.importProjectWin.musicPath)
        self.mainWin.ui.actionNewOrOpen.triggered.connect(self.newOrOpenProject)
        self.mainWin.show()
        self.importProjectWin.close()
        
    def newOrOpenProject(self):
        self.newOrOpenWin = newProjectShow(self.sess)
        self.newOrOpenWin.ui.pushButtonSave.clicked.connect(self.createProject)
        self.newOrOpenWin.ui.pushButtonImport.clicked.connect(self.openExistedPorject)
        self.newOrOpenWin.show()
    
    def openExistedPorject(self):
        self.newOrOpenWin.close()
        self.openExistProjectWin = ImportProjectShow(self.sess)
        self.openExistProjectWin.show()
        self.openExistProjectWin.ui.pushButtonSave.clicked.connect(self.reDisplayMainWin)
        
    def reDisplayMainWin(self):
        self.openExistProjectWin.save()
        self.mainWin.close()
        self.openExistProjectWin.close()
        self.session = self.openExistProjectWin.session
        self.mainWin = MainShow(self.sess, self.session, self.openExistProjectWin.fieldUUID,self.openExistProjectWin.musicPath)
        self.mainWin.show()
        self.mainWin.ui.actionNewOrOpen.triggered.connect(self.newOrOpenProject)
        
    def createProject(self):
        self.newOrOpenWin.save()
        if self.newOrOpenWin.nameFlag == 'used' or self.newOrOpenWin.selectFlag == False:
            return
        self.fieldEditWin = FirePositionShow(self.sess, self.newOrOpenWin.UUID,self.newOrOpenWin.path)
        self.fieldEditWin.ui.pushButtonDone.clicked.connect(self.reShowMainWin)
        self.fieldEditWin.show()
        self.newOrOpenWin.close()
        
    def reShowMainWin(self):
        self.fieldEditWin.next()
        if self.fieldEditWin.confirmFlag == False:
            return
        self.mainWin.close()
        self.mainWin = MainShow(self.sess, self.fieldEditWin.session, self.fieldEditWin.fieldUUID,self.fieldEditWin.musicPath)
        self.fieldEditWin.close()
        self.mainWin.show()
        self.mainWin.ui.actionNewOrOpen.triggered.connect(self.newOrOpenProject)
        
def main():
    app = QtGui.QApplication(sys.argv)
    control = UiControl()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
