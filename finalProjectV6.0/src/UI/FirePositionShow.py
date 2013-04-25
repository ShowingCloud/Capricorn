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



class FirePositionShow(QtGui.QDialog):

    def __init__(self, sess, UUID, owner, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui=Ui_FirePositionDialog()
        self.ui.setupUi(self)
        
        self.ui.pushButtonDone.clicked.connect(self.next)
        self.ui.pushButtonCancel.clicked.connect(self.cancel)
        
        self.sess = sess
        self.UUID = UUID
        self.owner = owner
        self.fieldUUID = str(uuid.uuid1())
        
    def next(self):
        d = {'X':self.ui.lineEditPositionX.text(), 'Y':self.ui.lineEditPositionY.text(), 'Z':self.ui.lineEditPositionZ.text()}
        loca = json.dumps(d)
        with self.sess.begin():
            record = self.sess.query (ProjectsData).filter_by(UUID = self.UUID).first()
        
        #生成自定义数据库
        self.engine = create_engine("sqlite:///" + record.Name)
        self.session = scoped_session(sessionmaker(bind = self.engine, autocommit= True))
        base1.metadata.create_all(self.engine)
        with self.sess.begin():
            other = self.sess.query (L_ScenesData).filter_by(UUID = record.Scenes).first()
        #添加到工程库阵地表中
        with self.session.begin():
            data = FieldsData()
            data.UUID = self.fieldUUID
            data.CTime = datetime.utcnow()
            data.MTime = datetime.utcnow()
            data.FieldID = self.ui.lineEditName.text()
            data.Location = loca
            data.Parent = other.Name
            self.session.add(data)
        
        with self.session.begin():
            ignitor = IgnitorsData()
            ignitor.UUID = str(uuid.uuid1())
            ignitor.CTime = datetime.utcnow()
            ignitor.MTime = datetime.utcnow()
#            ignitor.IgnitorID = 
            ignitor.BoxID = self.ui.comboBoxIgnitionBoxID.currentText()
            ignitor.TotalHeads = int(self.ui.comboBoxIgnitionBoxPoints.currentText())
            ignitor.SurplusHeads = int(self.ui.comboBoxIgnitionBoxPoints.currentText())
            self.session.add(ignitor)
            
        self.winShow = MainShow(self.sess, self.session, self.fieldUUID)
        self.winShow.show()
        self.close()
        
    def cancel(self):
        self.close()
        
        
        
        

