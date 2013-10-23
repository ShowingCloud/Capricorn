#coding=utf-8
from PySide import QtCore,QtGui
from UI.ui_fireworks import Ui_widgetWaveModule
from PySide.phonon import Phonon
from Resource import images_rc
# import sys
from PySide.QtCore import QPoint, Slot
from Models.LocalDB import session, engine, meta, FireworksData
from Models.ProjectDB import proSession, proEngine, proMeta, ProFireworksData
from Frontend.setTime import SetDelayTime
from Frontend.editFireworks import EditFireworks
from Frontend.timeTick import TimeTickShow
from Frontend.progressBar import ProgressBarShow
from Frontend.control import ControlWinShow
from Delegate.localDelegate import LocalDelegate
from Delegate.scriptDelegate import ScriptDelegate
import json
import uuid
from datetime import datetime
from Delegate.timeDelegate import TimeDelegate
from Delegate.spinBoxDelegate import SpinBoxDelegate
from Device.Communication import HardwareCommunicate
from Device.protocol import dataPack
import Queue
import time
import os
from config import appdata
from sqlalchemy.sql.expression import func, distinct
import tarfile
import shutil

try:
    from Device import ftdi2 as ft
except:
    pass


class Fireworks(QtGui.QWidget):

    def __init__(self, signal, parent=None):
        QtGui.QWidget.__init__(self,parent)
        
        self.showSignal = signal
        self.ui=Ui_widgetWaveModule()
        self.ui.setupUi(self)
        self.ui.lcdNumber.display('00:00')
        self.ui.pushButtonDelay.hide()
        self.ui.pushButtonUpLoad.hide()
        self.ui.pushButtonOpenMusic.clicked.connect(self.openMusic)
        self.ui.pushButtonPlayOrPause.clicked.connect(self.playOrPauseMusic)
        self.ui.pushButtonStop.clicked.connect(self.stopMusic)
        self.ui.pushButtonDelay.clicked.connect(self.delayFire)
        self.ui.pushButtonUpLoad.clicked.connect(self.upLoadToDevice)

        #create local database
        self.localSession = session()
        meta.create_all(engine)
        
        #create project database
        self.proSession = proSession()
        proMeta.create_all(proEngine)
        #create media player 
        self.media = Phonon.MediaObject(self)
        self.output = Phonon.AudioOutput(Phonon.MusicCategory, self)
        Phonon.createPath(self.media, self.output)
        self.media.setTickInterval(10)
        
        self.ui.volumeSlider.setAudioOutput(self.output)
        self.ui.seekSlider.setMediaObject(self.media)
        
        self.media.tick.connect(self.tick)
        self.media.stateChanged.connect(self.musicStatusChanged)
        self.media.finished.connect(self.mediaFinish)
        self.musicTime = 0
        
        self.ui.comboBoxMode.currentIndexChanged.connect(self.modeChanged)
        
        #set fireworks type
        self.setTypeData()
        
        self.model = QtGui.QStandardItemModel(0, 3, self)
        self.ui.tableViewLocal.setModel(self.model)
        self.ui.tableViewLocal.setColumnWidth(1, 116)
        self.ui.tableViewLocal.setItemDelegate(LocalDelegate(self))
        
        self.ui.tableViewLocal.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.tableViewLocal.customContextMenuRequested.connect(self.rightContextMenu)
        
        self.proModel = QtGui.QStandardItemModel(0, 11, self)
        self.ui.scriptTableView.setModel(self.proModel)
        self.ui.scriptTableView.setSortingEnabled(True)
        self.ui.scriptTableView.setItemDelegateForColumn(1, TimeDelegate(self.proSession, self))
        self.ui.scriptTableView.setItemDelegateForColumn(2, ScriptDelegate(self.proSession, self))
        self.ui.scriptTableView.setItemDelegateForColumn(3, ScriptDelegate(self.proSession, self))
        self.ui.scriptTableView.setItemDelegateForColumn(4, ScriptDelegate(self.proSession, self))
        self.ui.scriptTableView.setItemDelegateForColumn(5, ScriptDelegate(self.proSession, self))
        self.ui.scriptTableView.setItemDelegateForColumn(6, TimeDelegate(self.proSession,self))
        self.ui.scriptTableView.setItemDelegateForColumn(7, TimeDelegate(self.proSession,self))
        self.ui.scriptTableView.setItemDelegateForColumn(8, TimeDelegate(self.proSession,self))
        self.ui.scriptTableView.setItemDelegateForColumn(9, TimeDelegate(self.proSession,self))
        self.ui.scriptTableView.setItemDelegateForColumn(10, SpinBoxDelegate(self.proSession, self))
        self.ui.scriptTableView.setItemDelegateForColumn(11, ScriptDelegate(self.proSession, self))
        
        #add right menu
        self.ui.scriptTableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.scriptTableView.customContextMenuRequested.connect(self.scriptRightContextMenu)
        
        
        self.type = u'椰树'
        self.query(self.type)
        
        #show the script fireworks
        self.scriptTable = self.refreshScript()
        
        #change the local database fireworks
        self.ui.listWidgetLocal.itemClicked.connect(self.refreshQuery)
        
        self.ui.tableViewLocal.doubleClicked.connect(self.addScriptFireworks)
        self.musicPath = None
    
        self.ui.pushButtonSavePro.clicked.connect(self.saveProject)
        self.ui.pushButtonOpenPro.clicked.connect(self.openProject)
        
        self.projectPath = None
        
    def upLoadToDevice(self):
#         try:
#             dev = ft.list_devices()
#         except:
#             dev = []
#         if len(dev) == 0:
#             return
        
        with self.proSession.begin():
            tableFire = self.proSession.query(ProFireworksData).all()
        node = {'head':0xAAF0,'length':0x14,'function':0x01,'ID':0xAABBCCDD,'fireBox':None,
                'firePoint':None,'seconds':None,'offsetSec':None,'crc':0,'tail':0xDD}
        
        self.progressBar = ProgressBarShow(len(tableFire))
        print len(tableFire)
        self.progressBar.show()
        i = 0
        for row in tableFire:
            node['fireBox'] = row.IgnitorID
            node['firePoint'] = row.ConnectorID
            node['seconds'] = int(row.IgnitionTime/1000)
            node['offsetSec'] = int(row.IgnitionTime%1000) #ms
            package = dataPack(node)
            package.pack()
            self.myQueue.put (package.package)
            i += 1
            self.progressBar.ui.progressBar.setValue(i)
            for a in range(1000000):
                pass
        self.progressBar.close()
        self.ui.pushButtonUpLoad.setEnabled(False)
        self.ui.pushButtonDelay.setEnabled(True)
    def delayFire(self):
        self.delayTimeWin = SetDelayTime()
        if self.delayTimeWin.exec_():
            self.delaySeconds = int(self.delayTimeWin.ui.lineEditDelayTime.text())
            self.startTick()
            
    def startTick(self):
        self.timeCountWin = TimeTickShow(self.delaySeconds)
        if self.timeCountWin.exec_():
            if self.musicPath != None :
                self.media.play()
                self.controlWin = ControlWinShow(self.ui.pushButtonPlayOrPause.clicked,self.ui.pushButtonStop.clicked,self.media.finished)
                if self.controlWin.exec_():
                    self.media.stop()
                
    
            
        
    def setTypeData(self):
        coco = QtGui.QListWidgetItem(self.ui.listWidgetLocal)
        cocoIcon = QtGui.QIcon()
        cocoIcon.addPixmap(QtGui.QPixmap(":/Images/coco.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        coco.setIcon(cocoIcon)
        coco.setToolTip(u'椰树')
        coco.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        
        brocadeHat = QtGui.QListWidgetItem(self.ui.listWidgetLocal)
        brocadeHatIcon = QtGui.QIcon()
        brocadeHatIcon.addPixmap(QtGui.QPixmap(":/Images/brocade hat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        brocadeHat.setIcon(brocadeHatIcon)
        brocadeHat.setToolTip(u'锦冠')
        brocadeHat.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        
        gorgeous = QtGui.QListWidgetItem(self.ui.listWidgetLocal)
        gorgeousIcon = QtGui.QIcon()
        gorgeousIcon.addPixmap(QtGui.QPixmap(":/Images/gorgeous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        gorgeous.setIcon(gorgeousIcon)
        gorgeous.setToolTip(u'大丽')
        gorgeous.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
         
        peony = QtGui.QListWidgetItem(self.ui.listWidgetLocal)
        peonyIcon = QtGui.QIcon()
        peonyIcon.addPixmap(QtGui.QPixmap(":/Images/peony.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        peony.setIcon(peonyIcon)
        peony.setToolTip(u'牡丹')
        peony.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
         
        candle = QtGui.QListWidgetItem(self.ui.listWidgetLocal)
        candleIcon = QtGui.QIcon()
        candleIcon.addPixmap(QtGui.QPixmap(":/Images/candle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        candle.setIcon(candleIcon)
        candle.setToolTip(u'喷泉')
        candle.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
         
        potFlower = QtGui.QListWidgetItem(self.ui.listWidgetLocal)
        potFlowerIcon = QtGui.QIcon()
        potFlowerIcon.addPixmap(QtGui.QPixmap(":/Images/pot flower.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        potFlower.setIcon(potFlowerIcon)
        potFlower.setToolTip(u'盆花')
        potFlower.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
         
        willow = QtGui.QListWidgetItem(self.ui.listWidgetLocal)
        willowIcon = QtGui.QIcon()
        willowIcon.addPixmap(QtGui.QPixmap(":/Images/willow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        willow.setIcon(willowIcon)
        willow.setToolTip(u'柳树')
        willow.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
         
        mum = QtGui.QListWidgetItem(self.ui.listWidgetLocal)
        mumIcon = QtGui.QIcon()
        mumIcon.addPixmap(QtGui.QPixmap(":/Images/mum.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mum.setIcon(mumIcon)
        mum.setToolTip(u'菊花')
        mum.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
         
        glint = QtGui.QListWidgetItem(self.ui.listWidgetLocal)
        glintIcon = QtGui.QIcon()
        glintIcon.addPixmap(QtGui.QPixmap(":/Images/glint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        glint.setIcon(glintIcon)
        glint.setToolTip(u'银闪')
        glint.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
    
    def query(self, Type):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["UUID",u"烟花信息", u'上升时间', u'烟花效果'])
        self.ui.tableViewLocal.hideColumn(0)
        self.ui.tableViewLocal.hideColumn(2)
        self.ui.tableViewLocal.hideColumn(3)
        with self.localSession.begin():
            record = self.localSession.query (FireworksData).filter_by(Type = Type).all()
        for i in xrange(len(record)):
            self.model.insertRow(i)
            self.model.setData(self.model.index(i, 0), record[i].UUID)
            self.model.setData(self.model.index(i, 1), record[i].Name)
            self.model.setData(self.model.index(i, 2), record[i].RisingTime)
            self.model.setData(self.model.index(i, 3), record[i].EffectsInfo)
     
    @Slot(QPoint)  
    def rightContextMenu(self, point):
        self.row = self.ui.tableViewLocal.rowAt(point.y())
        rightMenu = QtGui.QMenu(self)
        addFireworksAction = QtGui.QAction("Add Fireworks", self)
        addFireworksAction.setStatusTip("Insert the fireworks info into  database")
        addFireworksAction.connect(QtCore.SIGNAL("triggered()"), self.addFireworks)
        rightMenu.addAction(addFireworksAction)
        if self.row >= 0:
            editFireworksAction = QtGui.QAction("Edit Fireworks", self)
            editFireworksAction.setStatusTip("Edit  the fireworks  information")
            editFireworksAction.connect(QtCore.SIGNAL("triggered()"), self.editFireworks)
            rightMenu.addAction(editFireworksAction)
            
        rightMenu.exec_(QtGui.QCursor.pos())
        
    def addFireworks(self):
        dialogAddFireworks = EditFireworks(self.localSession, parent = self)
        accept = dialogAddFireworks.exec_()
        if accept == 1:
            self.query(self.type)
            
    @Slot(QPoint)  
    def scriptRightContextMenu(self, point):
        self.scriptRow = self.ui.scriptTableView.rowAt(point.y())
        scriptRightMenu = QtGui.QMenu(self)
        if self.scriptRow >= 0:
            deleteScriptAction = QtGui.QAction("Delete", self)
            deleteScriptAction.setStatusTip("Delete  the script fireworks  information")
            deleteScriptAction.connect(QtCore.SIGNAL("triggered()"), self.deleteScript)
            scriptRightMenu.addAction(deleteScriptAction)
            
        scriptRightMenu.exec_(QtGui.QCursor.pos()) 
        
    def deleteScript(self):
        deleteUUID = self.proModel.item(self.scriptRow).text()
        with self.proSession.begin():
            deleteRecord = self.proSession.query (ProFireworksData).filter_by(UUID = deleteUUID).first()
            self.proSession.delete(deleteRecord)
        self.proModel.takeRow(self.scriptRow)
    
    def editFireworks(self):
        fireworksUUID = self.model.item(self.row, 0).text()
        
        dialogEditFireworks = EditFireworks(self.localSession, fireworksUUID, self)
        accept = dialogEditFireworks.exec_()
        if accept == 1:
            self.query(self.type)
        pass
    
    @Slot(QtGui.QListWidgetItem)
    def refreshQuery(self, item):
        self.type = item.toolTip()
        self.query(self.type)
    
    def modeChanged(self):
        if self.ui.comboBoxMode.currentIndex() == 0:
            self.ui.pushButtonDelay.hide()
            self.ui.pushButtonUpLoad.hide()
            self.ui.pushButtonOpenPro.show()
            self.ui.pushButtonSavePro.show()
            self.ui.seekSlider.setDisabled(False)
            self.ui.tableViewLocal.setEnabled(True)
            self.ui.scriptTableView.setEnabled(True)
        else:
            if self.checkCondition(): #if not self.checkCondition():
                self.ui.comboBoxMode.setCurrentIndex(0)
                return
            self.ui.tableViewLocal.setEnabled(False)
            self.ui.scriptTableView.setEnabled(False)
            self.ui.pushButtonDelay.show()
            self.ui.pushButtonUpLoad.show()
            self.ui.pushButtonOpenPro.hide()
            self.ui.pushButtonSavePro.hide()
            self.ui.seekSlider.setDisabled(True)
            self.ui.pushButtonDelay.setEnabled(False)
            self.stopMusic()
            
            self.myQueue = Queue.Queue()
            self.comminute = HardwareCommunicate(self.myQueue)
            self.threadCommunicate = QtCore.QThread()
            self.comminute.moveToThread(self.threadCommunicate)
            self.threadCommunicate.start()
            time.sleep(0.1)
            self.comminute.signalCommunicate.emit()
            
    def checkCondition(self):
        if self.musicPath == None:
            QtGui.QMessageBox.question(None,'message','Please choose music',QtGui.QMessageBox.Ok)
            return False
        #TODO:Check Fireworks and Ignitors 
#         try:
#             dev = ft.list_devices()
#         except:
#             dev = []
#         if len(dev) == 0:
#             QtGui.QMessageBox.question(None,'message','No device connect',QtGui.QMessageBox.Ok)
#             return False
#         return True
    
    def musicStatusChanged(self, newstate, oldState):
        if newstate == Phonon.PlayingState:
            self.ui.pushButtonPlayOrPause.setIcon(QtGui.QIcon(':/Images/pause.png'))
            
        elif (newstate != Phonon.LoadingState and newstate != Phonon.BufferingState):
            self.ui.pushButtonPlayOrPause.setIcon(QtGui.QIcon(':/Images/play.png'))
            if newstate == Phonon.ErrorState:
                source = self.media.currentSource().fileName()
                print ('ERROR: could not play: %s' % source)
                print ('  %s' % self.media.errorString())
    
    def openMusic(self):
        if self.media.state() == Phonon.PlayingState:
            self.media.stop()
        dialog = QtGui.QFileDialog(self)
        dialog.setFilter("*.wav | *.mp3")
        dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.musicPath = dialog.selectedFiles()[0]
            self.media.setCurrentSource(Phonon.MediaSource(self.musicPath))
        dialog.deleteLater()
        
    def playOrPauseMusic(self):
        if self.musicPath == None:
            msgBox = QtGui.QMessageBox(self)
            msgBox.setText("please choose a music file first.")
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.exec_()
            return
        if self.media.state() == Phonon.PlayingState:
            self.media.pause()
        else:
            self.media.play()
            
    def stopMusic(self):
        #self.ui.lcdNumber.display('00:00')
        self.media.seek(0)
        self.media.pause()
    
    def tick(self, time):
        self.musicTime = time
        displayTime = QtCore.QTime(0, (time / 60000) % 60, (time / 1000) % 60)
        self.ui.lcdNumber.display(displayTime.toString('mm:ss'))
        
    #double click add script fireworks
    @Slot(QtCore.QModelIndex) 
    def addScriptFireworks(self, index):
        
        effectTime = self.musicTime
        info = json.loads(self.model.item(index.row(), 3).text())
#         print int(float(info["EffectsInfo"][0][2])*1000)
#         print self.model.item(index.row(), 2).text()
        with self.proSession.begin():
            record = ProFireworksData()
            record.UUID = str(uuid.uuid1())
            record.CTime = datetime.utcnow()
            record.MTime = datetime.utcnow()
            record.FireworkID = self.model.item(index.row(), 0).text()
            if effectTime == 0:
                record.IgnitionTime = 0
            else:
                record.IgnitionTime = effectTime - int(self.model.item(index.row(), 2).text())
            
            record.IgnitorID = 0
            record.ConnectorID = 0
            record.Notes = self.model.item(index.row(), 2).text() + ',' +str(int(float(info["EffectsInfo"][0][2])*1000))
            self.proSession.add(record)
             
        self.scriptTable = self.refreshScript()
        
    def refreshScript(self):
        self.proModel.clear()
        self.proModel.setHorizontalHeaderLabels(['UUID',  u'开爆时刻', u'烟花名称', u'尺寸', u'颜色', u'燃放方向', u'点火时刻', u'上升时间', u'效果时间', u'结束时刻', u'点火盒', u'点火点'])
        self.ui.scriptTableView.hideColumn(0)
        
        with self.proSession.begin():
            scriptTable = self.proSession.query (ProFireworksData).all()
            
        for i in xrange(len(scriptTable)):
            #Get Rising time and Effect time from Notes
            effectAndRisingtimes = scriptTable[i].Notes.split(',')
            
            self.proModel.insertRow(i)
            
            with self.localSession.begin():
                data = self.localSession.query(FireworksData).filter_by(UUID = scriptTable[i].FireworkID).first()
            info = json.loads(data.EffectsInfo)
            effectTime = int(effectAndRisingtimes[0]) + scriptTable[i].IgnitionTime
            
            self.proModel.setData(self.proModel.index(i, 0), scriptTable[i].UUID)#uuid
            self.proModel.setData(self.proModel.index(i, 1), effectTime)#开爆时刻
            
            self.proModel.setData(self.proModel.index(i, 2), data.Name)#烟火名称
            self.proModel.setData(self.proModel.index(i, 3), data.Size)#尺寸
            self.proModel.setData(self.proModel.index(i, 4), info["EffectsInfo"][0][1])#颜色
            self.proModel.setData(self.proModel.index(i, 5), 90)#燃放方向,设置默认值为正对主席台90度
            self.proModel.setData(self.proModel.index(i, 6), scriptTable[i].IgnitionTime)#点火时刻
            self.proModel.setData(self.proModel.index(i, 7), int(effectAndRisingtimes[0]))#上升时间
            self.proModel.setData(self.proModel.index(i, 8),  int(effectAndRisingtimes[1]))#效果时间
            
            self.proModel.setData(self.proModel.index(i, 9), effectTime + int(effectAndRisingtimes[1]))#结束时刻
            self.proModel.setData(self.proModel.index(i, 10), scriptTable[i].IgnitorID)#点火盒,设置默认为0
            self.proModel.setData(self.proModel.index(i, 11), scriptTable[i].ConnectorID)#点火点,设置默认为0
        return scriptTable 
     
    def mediaFinish(self):
        self.stopMusic()
        
    def closeEvent(self, event):
        
        if not os.path.exists(os.path.join (appdata, 'proj', 'project.db')):
            return
        if os.path.getmtime(os.path.join (appdata, 'proj', 'project.db')) - os.path.getctime(os.path.join (appdata, 'proj', 'project.db')) > 1:
                
            #create custom message box 
            customMsgBox = QtGui.QMessageBox(self)
            customMsgBox.setWindowTitle(self.tr ("Message"))
            customMsgBox.setText(self.tr ("Do you want to save?"))
            buttonYes = customMsgBox.addButton(self.tr ("Yes"), QtGui.QMessageBox.ActionRole)
            buttonNO = customMsgBox.addButton(self.tr ("No"), QtGui.QMessageBox.ActionRole)
            buttonCancel = customMsgBox.addButton(self.tr("Cancel"), QtGui.QMessageBox.ActionRole)
            customMsgBox.exec_()    
            button = customMsgBox.clickedButton()
            
            if button == buttonYes:
                
                self.media.stop()
#         self.threadCommunicate.terminate()
                self.showSignal.emit()
                
                if self.projectPath == None:
                    self.projectPathAndSave()
                else:
                    self.save()
                os.remove(os.path.join (appdata, 'proj', 'project.db'))
                event.accept()
            elif button == buttonNO:
                
                self.media.stop()
    #             self.threadCommunicate.terminate()
                self.showSignal.emit()
                os.remove(os.path.join (appdata, 'proj', 'project.db'))
                event.accept()
                pass
            elif button == buttonCancel:
    #             print time.ctime(os.path.getctime(os.path.join (appdata, 'proj', 'project.db')))
                print os.path.getctime(os.path.join (appdata, 'proj', 'project.db'))
                print os.path.getatime(os.path.join (appdata, 'proj', 'project.db'))
                print os.path.getmtime(os.path.join (appdata, 'proj', 'project.db'))
                event.ignore()
           
        else:
            self.media.stop()
#             self.threadCommunicate.terminate()
            self.showSignal.emit()
            os.remove(os.path.join (appdata, 'proj', 'project.db'))
            event.accept()
                
        
    def checkIgnitorBox(self):
        flag = True
        #check Ignitor box
        with self.proSession.begin():
            records = self.proSession.query(ProFireworksData).all()
        for row in records:
            if row.IgnitorID == 0:
                flag = False
        #check   ConnectorID
        with self.proSession.begin():
            repeatCount = self.proSession.query(ProFireworksData.IgnitorID, func.count(ProFireworksData.ConnectorID)).group_by(ProFireworksData.IgnitorID).all()
            distinctCount = self.proSession.query(ProFireworksData.IgnitorID, func.count(distinct(ProFireworksData.ConnectorID))).group_by(ProFireworksData.IgnitorID).all()
        for i in xrange(len(repeatCount)):
            if repeatCount[i][0] == distinctCount[i][0]  and repeatCount[i][1] != distinctCount[i][1]:
                flag = False
        return flag
    
    def saveProject(self):
        
        if self.projectPath == None:
            self.projectPathAndSave()
        else:
            self.save()
        
    def save(self):
        
        tmpdir = os.path.join (appdata, 'tmp')
        if os.path.exists (tmpdir):
            if not os.path.isdir (tmpdir):
                os.remove (tmpdir)
                os.mkdir (tmpdir)
        else:
            os.mkdir (tmpdir)
              
        tar = tarfile.open (os.path.join (tmpdir, "export.tgz"), "w:gz")
        
        files = [(os.path.join (appdata, self.proSession.bind.url.database), os.path.basename (self.proSession.bind.url.database))]
#         TODO: add Music 
#         if self.musicPath != None:
#             shutil.copy2(self.musicPath, os.path.join (appdata, "music"))
#             files.append ((os.path.join (appdata, 'music', self.musicPath[(self.musicPath).rfind('/') + 1 :]), self.musicPath[(self.musicPath).rfind('/') + 1 :]))
        
        for f, name in files:
            tar.add(f, arcname = name)
        
        tar.close()
        
        shutil.copy2 (os.path.join (tmpdir, "export.tgz"), self.projectPath)
        
#         os.remove(os.path.join (appdata, 'music', self.musicPath[(self.musicPath).rfind('/') + 1 :]))
    def projectPathAndSave(self):
        
        filename = QtGui.QFileDialog.getSaveFileName (self,
                self.tr ("Save Project As..."),
                "output.tgz",
                self.tr ("Compressed Archives (*.tgz, *.tar.gz)"))
        self.projectPath = filename[0]
        self.save()

    def openProject(self):
        dialog = QtGui.QFileDialog(self)
        dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.projectPath = dialog.selectedFiles()[0]
            with tarfile.open (self.projectPath, "r") as tar:
                for f in tar:
                    if os.path.splitext (f.name)[1] == ".db":
                        break

                tar.extract (member = f.name, path = os.path.join (appdata, "proj"))
                
        self.refreshScript()
    
def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    window = Fireworks(None)
    window.show()
    sys.exit(app.exec_())
     
if __name__ == "__main__":
    main()
