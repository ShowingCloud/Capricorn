from PySide import QtCore,QtGui
from ui_projectImport import Ui_ProjectDialog
import tarfile, os
from datetime import datetime
from config import appdata
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from Models.EngineeringDB import *#ParametersData,FieldsData,base1
from Models.LocalDB import ProjectsData
from UI.WinShow import MainShow
import json

class ImportProjectShow(QtGui.QDialog):

    def __init__(self,sess,parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui=Ui_ProjectDialog()
        self.ui.setupUi(self)
        self.sess = sess
        self.showList()
        self.ui.pushButtonImport.clicked.connect(self.importProject)
        self.ui.pushButtonDelete.clicked.connect(self.deleteProject)
        self.ui.pushButtonSave.clicked.connect(self.save)
        self.ui.pushButtonClose.clicked.connect(self.cancel)
        self.ui.listWidgetProject.itemClicked.connect(self.showDetail)
    
    def showList(self):
        self.ui.listWidgetProject.clear()
        with self.sess.begin():
            projectTable = self.sess.query(ProjectsData).all()
        for row in projectTable:
            if row.Authorized != 'Deleted': 
                self.ui.listWidgetProject.addItem(row.Name)
        self.ui.lineEditDesigner.setText('')
        self.ui.lineEditDuration.setText('')
        self.ui.lineEditMusic.setText('')
        self.ui.lineEditShellCount.setText('')
        self.ui.lineEditModuleCount.setText('')
        
        
    def showDetail(self):
        name = self.ui.listWidgetProject.currentItem().text()
        
        self.ui.labelTitle.setText(name)
        with self.sess.begin():
            row = self.sess.query(ProjectsData).filter_by(Name = name).first()
        self.ui.lineEditDesigner.setText(row.Designer)
        self.ui.lineEditDuration.setText(str(row.Duration))
        self.ui.lineEditMusic.setText(row.MusicID)
        self.ui.lineEditShellCount.setText(str(row.ShellCount))
        self.ui.lineEditModuleCount.setText(str(row.ModuleCount))
        self.ui.textEditDescription.setText(str(row.Notes))
    
    def importProject(self):
        dialog = QtGui.QFileDialog(self)
        dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.path = dialog.selectedFiles()[0]
            with tarfile.open (self.path, "r") as tar:
                for f in tar:
                    if os.path.splitext (f.name)[1] == ".db":
                        break

                tar.extract (member = f.name, path = os.path.join (appdata, "proj"))

            print os.path.join (appdata, "proj", f.name)
            engine = create_engine("sqlite:///" + os.path.join (appdata, "proj", f.name))
            self.session = scoped_session(sessionmaker(bind = engine, autocommit= True))
            with self.session.begin():
                parameter = self.session.query (ParametersData).first()

            with self.sess.begin():
                project = self.sess.query(ProjectsData).filter_by(UUID = parameter.ProjectID).first()
            if project != None:
                project.MTime = datetime.utcnow()
                project.FieldList = parameter.FieldList
                project.Name = parameter.Name
                project.Description = parameter.Description
                project.Animation = parameter.Animation
                project.Time = parameter.Time
                project.Location = parameter.Location
                project.MusicID = parameter.MusicID
                project.ProjectFile = parameter.ProjectFile
                project.Designer = parameter.Designer
                project.Worker = parameter.Worker
                project.ShellCount = parameter.ShellCount
                project.Scenes = parameter.Scenes
                project.Duration = parameter.Duration
                project.Authorized = parameter.Authorized
                project.ModuleCount = parameter.ModuleCount
                project.Information = parameter.Information
                project.Notes = parameter.Notes
            else: 
                with self.session.begin():
                    parameter = self.session.query (ParametersData).first()
                with self.sess.begin():
                    project = ProjectsData()
                    project.UUID = parameter.ProjectID
                    project.CTime = datetime.utcnow()
                    project.MTime = datetime.utcnow()
                    project.FieldList = parameter.FieldList
                    project.Name = parameter.Name
                    project.Description = parameter.Description
                    project.Animation = parameter.Animation
                    project.Time = parameter.Time
                    project.Location = parameter.Location
                    project.MusicID = parameter.MusicID
                    project.ProjectFile = parameter.ProjectFile
                    project.Designer = parameter.Designer
                    project.Worker = parameter.Worker
                    project.ShellCount = parameter.ShellCount
                    project.Scenes = parameter.Scenes
                    project.Duration = parameter.Duration
                    project.Authorized = parameter.Authorized
                    project.ModuleCount = parameter.ModuleCount
                    project.Information = parameter.Information
                    project.Notes = parameter.Notes
                    self.sess.add(project)
            self.showList()

    
    def deleteProject(self):
        replay = QtGui.QMessageBox.question(None,'message','Are you sure to delete',
                                           QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
        if replay == QtGui.QMessageBox.No:
            return
        name = self.ui.listWidgetProject.currentItem().text()
        with self.sess.begin():
            row = self.sess.query(ProjectsData).filter_by(Name = name).first()
            row.Authorized = 'Deleted'
        i = self.ui.listWidgetProject.currentItem()
        self.ui.listWidgetProject.takeItem(int(self.ui.listWidgetProject.row(i)))
    
    def save(self):
        if self.ui.lineEditMusic.text() == '':
            QtGui.QMessageBox.question(None,'message','Please choose project first ',
                                           QtGui.QMessageBox.Ok)
            return
        name = self.ui.listWidgetProject.currentItem().text()
        with self.sess.begin():
            row = self.sess.query(ProjectsData).filter_by(Name = name).first()
            print 'project name is = ',row.Name
        file1 = row.UUID
        self.fieldUUID = json.loads(row.FieldList)[0]
        self.musicPath = row.MusicID
        engine = create_engine("sqlite:///" + os.path.join (appdata, "proj", file1+ '.db'))
        self.session = scoped_session(sessionmaker(bind = engine, autocommit= True))
     
        self.winShow = MainShow(self.sess, self.session, self.fieldUUID,self.musicPath)
        self.winShow.show()
        self.close()
        self.close()
        
    
    def cancel(self):
        self.close()