#coding=utf-8
from Models.EngineeringDB import *
from Models.LocalDB import ProjectsData, L_ScenesData
from PySide import QtGui
from UI.WinShow import MainShow
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from ui_firePosition import Ui_FirePositionDialog
import json
import uuid
import os
from config import appdata



class FirePositionShow(QtGui.QDialog):

    def __init__(self, sess, UUID, owner,musicFilePath, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui=Ui_FirePositionDialog()
        self.ui.setupUi(self)
        
        self.ui.pushButtonDone.clicked.connect(self.next)
        self.ui.pushButtonCancel.clicked.connect(self.cancel)
        self.ui.pushButtonAdd.clicked.connect(self.add)
        self.ui.pushButtonDelete.clicked.connect(self.deleteField)
        self.ui.listWidgetPosition.itemClicked.connect(self.showDetail)
        self.musicPath = musicFilePath
        self.sess = sess
        self.UUID = UUID
        self.owner = owner
        with self.sess.begin():
            self.record = self.sess.query (ProjectsData).filter_by(UUID = self.UUID).first()
        self.engine = create_engine("sqlite:///" + os.path.join (appdata, 'proj', self.record.Name + '.db'))
        self.session = scoped_session(sessionmaker(bind = self.engine, autocommit= True))
        base1.metadata.create_all(self.engine)
        
    def next(self):
        with self.sess.begin():
            other = self.sess.query (L_ScenesData).filter_by(UUID = self.record.Scenes).first()
        with self.session.begin():
            fieldList = self.session.query (FieldsData).filter_by(Parent = other.Name).first()

        if fieldList == None:
            reply = QtGui.QMessageBox.question(None,'message','Please add field first',
                                           QtGui.QMessageBox.Ok)
        else:
            self.winShow = MainShow(self.sess, self.session, self.fieldUUID,self.musicPath)
            self.winShow.show()
            self.close()
        
    def add(self):
        d = {'X':self.ui.lineEditPositionX.text(), 'Y':self.ui.lineEditPositionY.text(), 'Z':self.ui.lineEditPositionZ.text()}
        loca = json.dumps(d)
#         #生成自定义数据库
        with self.sess.begin():
            other = self.sess.query (L_ScenesData).filter_by(UUID = self.record.Scenes).first()
#         #添加到工程库阵地表中
        with self.session.begin():
            self.fieldUUID = str(uuid.uuid1())
            data = FieldsData()
            data.UUID = self.fieldUUID
            data.CTime = datetime.utcnow()
            data.MTime = datetime.utcnow()
            data.FieldID = self.ui.lineEditName.text()
            data.Location = loca
            data.Parent = other.Name
            self.session.add(data)
#         
        with self.session.begin():
            ignitor = IgnitorsData()
            ignitor.UUID = str(uuid.uuid1())
            ignitor.CTime = datetime.utcnow()
            ignitor.MTime = datetime.utcnow()
            ignitor.FieldID = data.UUID
#            ignitor.IgnitorID = 
            ignitor.BoxID = self.ui.comboBoxIgnitionBoxID.currentText()
            ignitor.TotalHeads = int(self.ui.comboBoxIgnitionBoxPoints.currentText())
            ignitor.SurplusHeads = int(self.ui.comboBoxIgnitionBoxPoints.currentText())
            self.session.add(ignitor)

        self.ui.listWidgetPosition.addItem(self.ui.lineEditName.text())
        
        
    def showDetail(self):
        itemSelect = self.ui.listWidgetPosition.currentItem().text()
        with self.session.begin():
            rowField = self.session.query (FieldsData).filter_by(FieldID = itemSelect).first()
        self.ui.lineEditName.setText( rowField.FieldID )
        self.ui.lineEditPositionX.setText(json.loads(rowField.Location)['X'])
        self.ui.lineEditPositionY.setText(json.loads(rowField.Location)['Y'])
        self.ui.lineEditPositionZ.setText(json.loads(rowField.Location)['Z'])
        
        with self.session.begin():
            rowIgnitor = self.session.query (IgnitorsData).filter_by(FieldID = rowField.UUID).first()
        if rowIgnitor == None:
            print 'rowIgnitor == None'
        i =int( rowIgnitor.BoxID)
        self.ui.comboBoxIgnitionBoxID.setCurrentIndex(i-1)
        if rowIgnitor.TotalHeads == 10:
            self.ui.comboBoxIgnitionBoxPoints.setCurrentIndex(0)
        if rowIgnitor.TotalHeads == 50:
            self.ui.comboBoxIgnitionBoxPoints.setCurrentIndex(1)
    def deleteField(self):
        
        pass
    def cancel(self):
        self.close()
        
        
        
        

