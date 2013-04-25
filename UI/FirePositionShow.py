#coding=utf-8
from Models.EngineeringDB import *
from Models.LocalDB import ProjectsData, L_ScenesData
from PySide import QtGui
from UI.WinShow import MainShow
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from ui_firePosition import Ui_FirePositionDialog
from Delegate.newFieldIgnitorBoxDelegate import ignitorBoxDelegate
#from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtCore import Qt,QPoint,Slot,SIGNAL
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
        self.ui.pushButtonAdd.clicked.connect(self.addField)
        self.ui.pushButtonDelete.clicked.connect(self.deleteField)
        self.ui.listWidgetPosition.itemClicked.connect(self.showDetail)
        self.ui.lineEditName.textChanged.connect(self.resetTable)
        self.ui.pushButtonAddBox.clicked.connect(self.addBox)
        self.musicPath = musicFilePath
        self.sess = sess
        self.UUID = UUID
        self.owner = owner
        self.addBoxFlag = False
        intVal = QtGui.QIntValidator()
        self.ui.lineEditPositionX.setValidator(intVal)
        self.ui.lineEditPositionY.setValidator(intVal)
        self.ui.lineEditPositionZ.setValidator(intVal)
        self.ui.lineEditIgnitionBox.setValidator(intVal)
        
        self.setIgnitorTable()
        self.ui.tableViewIgnitor.setItemDelegate(ignitorBoxDelegate())
        self.ui.tableViewIgnitor.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tableViewIgnitor.customContextMenuRequested.connect(self.deleteBoxAction)
        
        with self.sess.begin():
            self.record = self.sess.query (ProjectsData).filter_by(UUID = self.UUID).first()
        self.engine = create_engine("sqlite:///" + os.path.join (appdata, 'proj', self.record.UUID + '.db'))
        self.session = scoped_session(sessionmaker(bind = self.engine, autocommit= True))
        base1.metadata.create_all(self.engine)
        with self.session.begin():
            parameter = ParametersData()
            parameter.CTime = datetime.utcnow()
            parameter.MTime = datetime.utcnow()
            parameter.ProjectID = self.UUID
            parameter.Worker = self.record.Worker
            parameter.Designer = self.record.Designer
            parameter.Scenes = self.record.Scenes
            parameter.Time = self.record.Time
            parameter.Duration = self.record.Duration
            parameter.Notes = self.record.Notes
            parameter.MusicID = self.record.MusicID
            parameter.Name = self.record.Name
            self.session.add(parameter)
            
            
    def setIgnitorTable(self):
        self.ui.tableViewIgnitor.setAlternatingRowColors(True)
        self.model = QStandardItemModel(0, 1, self)
        self.model.setHorizontalHeaderLabels(["BoxID","Heads"])
        self.ui.tableViewIgnitor.setModel(self.model)
        self.ui.tableViewIgnitor.setColumnWidth(0,80)
        self.ui.tableViewIgnitor.setColumnWidth(1,80)
        self.boxList = []
        
        
    def next(self):
        with self.sess.begin():
            other = self.sess.query (L_ScenesData).filter_by(UUID = self.record.Scenes).first()
        with self.session.begin():
            fieldList = self.session.query (FieldsData).filter_by(Parent = other.Name).first()
        with self.session.begin():
            ignitorBox = self.session.query (IgnitorsData).first()
        if fieldList == None:
            QtGui.QMessageBox.question(None,'message','Please add field first',
                                           QtGui.QMessageBox.Ok)
            return
        if ignitorBox == None:
            QtGui.QMessageBox.question(None,'message','Please add ignitorBox first',
                                           QtGui.QMessageBox.Ok)    
            return
        else:
            FieldList = []
            with self.session.begin():
                fieldTable = self.session.query(FieldsData).all()
            for row in fieldTable:
                FieldList.append(row.UUID)
            FieldListPack = json.dumps(FieldList)
            with self.sess.begin():
                row = self.sess.query(ProjectsData).filter_by(UUID = self.UUID).first()
                row.FieldList = FieldListPack
            print 'add field ',row.FieldList
            self.fieldUUID = fieldList.UUID
            self.winShow = MainShow(self.sess, self.session, self.fieldUUID,self.musicPath)
            self.winShow.show()
            self.close()
            
            
    def checkIgnitor(self):
        if self.ui.lineEditIgnitionBox.text() == '':
                QtGui.QMessageBox.question(None,'message','Please input ignitorBox ID',
                                           QtGui.QMessageBox.Ok)
                self.ignitorUseFlag = True
                return
        with self.session.begin():
            ignitorTable = self.session.query (IgnitorsData).all()
        for row in ignitorTable:
            if row.BoxID == self.ui.lineEditIgnitionBox.text():
                reply = QtGui.QMessageBox.question(None,'message','Ignitor box ID has been used',
                                           QtGui.QMessageBox.Ok)
                self.ignitorUseFlag = True
                return 
            
    def resetTable(self):
        self.model.clear()
        self.setIgnitorTable()
        self.boxList = []
        self.addBoxFlag = False
        
    def checkFieldID(self):
        with self.session.begin():
            fieldTable = self.session.query(FieldsData).all()
        for row in fieldTable:
            if row.FieldID == self.ui.lineEditName.text():
                reply = QtGui.QMessageBox.question(None,'message','Field name has been used',
                                           QtGui.QMessageBox.Ok)
                self.fieldUseFlag = True
        
    def addBox(self):
        self.ignitorUseFlag = False
        if len(self.boxList) :
            for node in self.boxList:
                if node['BoxID'] == self.ui.lineEditIgnitionBox.text():
                    QtGui.QMessageBox.question(None,'message','Ignitor box ID has been used',
                                           QtGui.QMessageBox.Ok)
                    return
        
        self.checkIgnitor()
        if self.ignitorUseFlag == True:
            return
        
        boxDict = {'BoxID':None,'Heads':None}
        boxDict['BoxID'] = self.ui.lineEditIgnitionBox.text()
        boxDict['Heads'] = self.ui.comboBoxIgnitionBoxPoints.currentText()
        self.boxList.append(boxDict)
        newRow = []
        newRow.append (QStandardItem (boxDict['BoxID']))
        newRow.append (QStandardItem (boxDict['Heads']))      
        self.model.appendRow(newRow)
#         if self.addBoxFlag == True:
#             with self.session.begin():
                

    @Slot(QPoint)
    def deleteBoxAction(self,point):
        rightMenu = QMenu(self)
        addAction = QAction("Delete", self)
        self.row = self.ui.tableViewIgnitor.rowAt(point.y())
        addAction.connect(SIGNAL("triggered()"), self.deleteBox)
        rightMenu.addAction(addAction)
        
        rightMenu.exec_(QCursor.pos())
        
        pass
    def deleteBox(self):
        item = self.model.item(self.row)
        with self.session.begin():
            record = self.session.query (IgnitorsData).filter_by(BoxID = item.text()).first()
            #删除表格里面数据
            self.model.takeRow(self.row)
            if record:
                self.session.delete(record)
        
    def addField(self):
        if len(self.boxList) == 0:
            QtGui.QMessageBox.question(None,'message','Please add ignitorBox first',
                                           QtGui.QMessageBox.Ok)
            return

        self.fieldUseFlag = False
        self.checkFieldID()
        if  self.fieldUseFlag == True :
            return
        d = {'X':self.ui.lineEditPositionX.text(), 'Y':self.ui.lineEditPositionY.text(), 'Z':self.ui.lineEditPositionZ.text()}
        loca = json.dumps(d)
#             #生成自定义数据库
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
        print '1 ',data.UUID
        for node in self.boxList:
            print  'addField',node['BoxID'],' head',node['Heads']
            with self.session.begin():
                ignitor = IgnitorsData()
                ignitor.UUID = str(uuid.uuid1())
                ignitor.CTime = datetime.utcnow()
                ignitor.MTime = datetime.utcnow()
                ignitor.FieldID = data.UUID
#            ignitor.IgnitorID = 
                ignitor.BoxID = node['BoxID']
                ignitor.TotalHeads = int(node['Heads'])
                ignitor.SurplusHeads = int(node['Heads'])
                self.session.add(ignitor)
            
        self.ui.listWidgetPosition.addItem(self.ui.lineEditName.text())
        self.boxList = []
        self.model.clear()
        self.setIgnitorTable()

    def showDetail(self):
        itemSelect = self.ui.listWidgetPosition.currentItem().text()
        with self.session.begin():
            rowField = self.session.query (FieldsData).filter_by(FieldID = itemSelect).first()
        self.ui.lineEditName.setText( rowField.FieldID )
        self.ui.lineEditPositionX.setText(json.loads(rowField.Location)['X'])
        self.ui.lineEditPositionY.setText(json.loads(rowField.Location)['Y'])
        self.ui.lineEditPositionZ.setText(json.loads(rowField.Location)['Z'])
        self.model.clear()
        self.setIgnitorTable()
        with self.session.begin():
            IgnitorTable = self.session.query (IgnitorsData).filter_by(FieldID = rowField.UUID)
        for row in IgnitorTable:
            newRow = []
            newRow.append (QStandardItem (row.BoxID))
            newRow.append (QStandardItem (str(row.TotalHeads)))   
            self.model.appendRow(newRow)
            
        self.ui.lineEditIgnitionBox.setText('')
        self.ui.comboBoxIgnitionBoxPoints.setCurrentIndex(0)
        self.addBoxFlag = True
    
    def deleteField(self):
        itemSelect = self.ui.listWidgetPosition.currentItem().text()
       
        with self.session.begin():
            row = self.session.query (FieldsData).filter_by(FieldID = itemSelect).first()
            fieldID = row.UUID
            self.session.delete(row)
        with self.session.begin():
            boxTable = self.session.query(IgnitorsData).filter_by(FieldID = fieldID)
            for row1 in boxTable:
                self.session.delete(row1)
        i = self.ui.listWidgetPosition.currentItem()
        self.ui.listWidgetPosition.takeItem(int(self.ui.listWidgetPosition.row(i)))
        self.resetTable()
        
    def cancel(self):
        self.close()
        
        
        
        

