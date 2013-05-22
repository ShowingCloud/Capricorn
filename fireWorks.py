#coding=utf-8
from PySide import QtCore, QtGui
from UI.FirePositionShow import FirePositionShow
from UI.ImportProjectShow import ImportProjectShow
from UI.ui_loginWin import Ui_Dialog
from Models.LocalDB import *
from datetime import datetime, timedelta, date
import sys, uuid
from Toolkit import SingleInstance
 
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
        self.path = None
        self.ui.pushButtonLogin.clicked.connect(self.login)
        self.ui.pushButtonImport.clicked.connect(self.importProject)
        self.ui.pushButtonSave.clicked.connect(self.save)
        self.ui.pushButtonSoundTrack.clicked.connect(self.handleButtonChoose)
        self.ui.checkBoxMusic.clicked.connect(self.setMusicTime)
        self.ui.lineEditDurationMin.setText('5')
        self.ui.lineEditDurationSec.setText('0')

    def addComboData(self):
        with self.sess.begin():
            data = self.sess.query(L_ScenesData).all()
            
        for row in data:
            self.ui.comboBoxShootSite.addItem(row.Name, row.UUID)
            
    def handleButtonChoose(self):
        dialog = QtGui.QFileDialog(self)
        dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.path = dialog.selectedFiles()[0]
            self.ui.lineEditSoundTrack.setText(self.path)
            if self.ui.checkBoxMusic.isChecked():
                self.getMusicTime()
        dialog.deleteLater()
        
        
    def getMusicTime(self):
        from PySide.phonon import Phonon
        self.media2 = Phonon.MediaObject(self)
        self.media2.setCurrentSource(Phonon.MediaSource())
        self.media2.setCurrentSource(Phonon.MediaSource(self.path))
        output = Phonon.AudioOutput(Phonon.MusicCategory, self)
        Phonon.createPath(self.media2, output)
        self.media2.stateChanged.connect(self.stateChanged2)
        
    def stateChanged2(self):
        print 'stateChanged2 media.totalTime()=',self.media2.totalTime()
        if self.ui.checkBoxMusic.isChecked():
            musicTime = self.media2.totalTime()/1000
            musicSeconds = musicTime%60
            musicMinutes = musicTime/60
            self.ui.lineEditDurationMin.setText(str(musicMinutes))
            self.ui.lineEditDurationSec.setText(str(musicSeconds))
            
    def setMusicTime(self):
        if self.ui.checkBoxMusic.isChecked():
            if self.path == None:
                return
            else:
                self.getMusicTime()
        else:
            self.ui.lineEditDurationMin.setText('5')
            self.ui.lineEditDurationSec.setText('0')
        
    def login(self):
        print self.ui.lineEditUsername.text()
        print self.ui.lineEditPassword.text()
        if self.ui.lineEditUsername.text() == "admin" and self.ui.lineEditPassword.text() == "admin":
            self.loginFlag = "Success"
            self.ui.label_progress.setText('Login Success')
        else:
            self.ui.label_progress.setText('Wrong password or username')
            
    def importProject(self):
        if self.loginFlag == "Success":
            self.project = ImportProjectShow(self.sess)
            self.project.show()
            self.close()
        else:
            QtGui.QMessageBox.question(None,'message','Please login first ',
                                           QtGui.QMessageBox.Ok)
    def save(self):
        #通过ComboBox获取场景的UUID
        with self.sess.begin():
            row = self.sess.query(ProjectsData).filter_by(Name = self.ui.lineEditShowName.text()).first()
        if row != None:
            QtGui.QMessageBox.question(None,'message','Show name has been used',
                                           QtGui.QMessageBox.Ok)
            return
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
                record.Scenes = item
                record.Duration = timedelta(minutes = int(self.ui.lineEditDurationMin.text()), seconds = int(self.ui.lineEditDurationSec.text()))
                record.Notes = self.ui.textEditNotes.toPlainText()
                record.MusicID = self.path
                self.sess.add(record)
                
            self.fire = FirePositionShow(self.sess, self.UUID, self.ui.lineEditUsername.text(),self.path)
            self.fire.show()
            self.close()
        else:
            QtGui.QMessageBox.information(self, "Information", " Username or password error, please login again!")
            
def main():
    me = SingleInstance()
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
