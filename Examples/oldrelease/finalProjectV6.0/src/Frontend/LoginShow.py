#coding=utf-8
from PySide import QtCore, QtGui
from UI.FirePositionShow import FirePositionShow
from UI.ImportProjectShow import ImportProjectShow
from UI.ui_loginWin import Ui_Dialog
from Models.LocalDB import *
from datetime import datetime, timedelta, date
import sys, uuid
#from Translations.tr_rc import *


class uiShow(QtGui.QDialog):

    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        
        self.sess = session()
        base.metadata.create_all(engine)
        
        self.UUID = str(uuid.uuid1())
        self.loginFlag = None
        self.addComboData()
        
        self.ui.pushButtonLogin.clicked.connect(self.login)
        self.ui.pushButtonImport.clicked.connect(self.importProject)
        self.ui.pushButtonSave.clicked.connect(self.save)
        
    def addComboData(self):
        with self.sess.begin():
            data = self.sess.query(L_ScenesData).all()
            
        for row in data:
            self.ui.comboBoxShootSite.addItem(row.Name, row.UUID)
           
    def login(self):
        print self.ui.lineEditUsername.text()
        print self.ui.lineEditPassword.text()
        if self.ui.lineEditUsername.text() == "admin" and self.ui.lineEditPassword.text() == "admin":
            self.loginFlag = "Success"
            self.ui.label_progress.setText('Login Success')
        else:
            self.ui.label_progress.setText('Wrong password or username')
    def importProject(self):
        project = ImportProjectShow(self)
        project.show()
    
    def save(self):
        #通过ComboBox获取场景的UUID
        item = self.ui.comboBoxShootSite.itemData(self.ui.comboBoxShootSite.currentIndex())
        if self.loginFlag == "Success" :
            with self.sess.begin():
                record = ProjectsData()
                record.UUID = self.UUID
                record.CTime = datetime.utcnow()
                record.MTime = datetime.utcnow()
                record.Name = self.ui.lineEditShowName.text()
                record.Time = date(self.ui.lineEditShowDate.date().year(), self.ui.lineEditShowDate.date().month(), self.ui.lineEditShowDate.date().day())
                record.Designer = self.ui.lineEditDesigner.text()
                record.Worker = self.ui.lineEditFiredBy.text()
                record.Cues = self.ui.lineEditCues.text()
                record.Scenes = item
                record.Duration = timedelta(minutes = int(self.ui.lineEditDurationMin.text()), seconds = int(self.ui.lineEditDurationSec.text()))
                record.Notes = self.ui.textEditNotes.toPlainText()
                self.sess.add(record)
                
            self.fire = FirePositionShow(self.sess, self.UUID, self.ui.lineEditUsername.text())
            self.fire.show()
            self.close()
        else:
            QtGui.QMessageBox.information(self, "Information", " Username or password error, please login again!")
            
def main():
    app = QtGui.QApplication(sys.argv)
    locale = QtCore.QLocale.system().name()
##    appTranslator = QtCore.QTranslator()
##    if appTranslator.load (":/loginWin_" + locale):
##        app.installTranslator (appTranslator)
    window = uiShow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
