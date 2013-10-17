#coding=utf-8
from PySide import QtCore,QtGui
from UI.ui_fireworks import Ui_widgetWaveModule
from PySide.phonon import Phonon
from Resource import images_rc
import sys
from PySide.QtCore import QPoint, Slot
from Models.LocalDB import session, engine, meta, FireworksData
from Models.ProjectDB import proSession, proEngine, proMeta, ProFireworksData
from Frontend.setTime import SetDelayTime
from Frontend.editFireworks import EditFireworks
from Frontend.GlobalMessage import MessageDisplay
from Frontend.timeTick import TimeTickShow
from Frontend.progressBar import ProgressBarShow
from Delegate.localDelegate import LocalDelegate
from Delegate.scriptDelegate import ScriptDelegate
import json
import uuid
from datetime import datetime
from Delegate.timeDelegate import TimeDelegate
from Delegate.spinBoxDelegate import SpinBoxDelegate
from Device.Communication import HardwareCommunicate
import Queue
import time

class Fireworks(QtGui.QWidget):

    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_widgetWaveModule()
        self.ui.setupUi(self)
        self.ui.lcdNumber.display('00:00')
        self.ui.pushButtonDelay.hide()
        self.ui.pushButtonUpLoad.hide()
        self.ui.pushButtonOpen.clicked.connect(self.openMusic)
        self.ui.pushButtonPlayOrPause.clicked.connect(self.playOrPauseMusic)
        self.ui.pushButtonStop.clicked.connect(self.stopMusic)
        self.ui.pushButtonDelay.clicked.connect(self.delayFire)
        self.ui.pushButtonUpLoad.clicked.connect(self.upLoadToDevice)

        #生成本地库
        self.localSession = session()
        meta.create_all(engine)
        
        #生成工程库
        self.proSession = proSession()
        proMeta.create_all(proEngine)
        #添加音乐播放器
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
        
        #改变模式
        self.ui.comboBoxMode.currentIndexChanged.connect(self.modeChanged)
        
        #设置烟花类型数据
        self.setTypeData()
        
        #为本地烟火库tableview添加model
        self.model = QtGui.QStandardItemModel(0, 3, self)
        self.ui.tableViewLocal.setModel(self.model)
        self.ui.tableViewLocal.setColumnWidth(1, 116)
        self.ui.tableViewLocal.setItemDelegate(LocalDelegate(self))
        
        #为本地烟火库tableview添加右键菜单
        self.ui.tableViewLocal.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.tableViewLocal.customContextMenuRequested.connect(self.rightContextMenu)
        
        #为脚本烟火库tableview添加model
        self.proModel = QtGui.QStandardItemModel(0, 11, self)
        self.ui.scriptTableView.setModel(self.proModel)
        self.ui.scriptTableView.setSortingEnabled(True)
        self.ui.scriptTableView.setItemDelegateForColumn(1, TimeDelegate(self.proSession, self))
        self.ui.scriptTableView.setItemDelegateForColumn(2, ScriptDelegate(self))
        self.ui.scriptTableView.setItemDelegateForColumn(3, ScriptDelegate(self))
        self.ui.scriptTableView.setItemDelegateForColumn(4, ScriptDelegate(self))
        self.ui.scriptTableView.setItemDelegateForColumn(5, ScriptDelegate(self))
        self.ui.scriptTableView.setItemDelegateForColumn(6, TimeDelegate(self.proSession,self))
        self.ui.scriptTableView.setItemDelegateForColumn(7, TimeDelegate(self.proSession,self))
        self.ui.scriptTableView.setItemDelegateForColumn(8, TimeDelegate(self.proSession,self))
        self.ui.scriptTableView.setItemDelegateForColumn(9, TimeDelegate(self.proSession,self))
        self.ui.scriptTableView.setItemDelegateForColumn(10, SpinBoxDelegate(self.proSession, self))
        self.ui.scriptTableView.setItemDelegateForColumn(11, ScriptDelegate(self))
        
        #为工程脚本tableview添加右键菜单
        self.ui.scriptTableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.scriptTableView.customContextMenuRequested.connect(self.scriptRightContextMenu)
        
        #测试全局字符串
        print MessageDisplay.getMessage('a')
        
        #查询数据库显示本地烟火库
        self.type = 'coco'
        self.query(self.type)
        
        #显示脚本库信息
        self.scriptTable = self.refreshScript()
        
        #切换烟花种类刷新烟火库
        self.ui.listWidgetLocal.itemClicked.connect(self.refreshQuery)
        #双击添加脚本烟花
        self.ui.tableViewLocal.doubleClicked.connect(self.addScriptFireworks)
        self.path = None
    
    def upLoadToDevice(self):
        self.myQueue = Queue.Queue()
        self.comminute = HardwareCommunicate(self.myQueue)
        thread = QtCore.QThread()
        self.comminute.moveToThread(thread)
        thread.start()
        time.sleep(0.1)
        self.comminute.signalCommunicate.emit()
        self.progressBar = ProgressBarShow(12)
        self.progressBar.show()
        for i in range(12):
            for a in range(10000000):
                pass
            self.progressBar.ui.progressBar.setValue(i)
        self.progressBar.close()
    
    def delayFire(self):
        self.delayTime = SetDelayTime()
        self.delayTime.show()
        self.delayTime.ui.pushButtonStart.clicked.connect(self.startTick)
        
    def startTick(self):
        self.delaySeconds = int(self.delayTime.ui.lineEditDelayTime.text())
        self.delayTime.close()
        self.timeCount = TimeTickShow(self.delaySeconds)
        self.timeCount.show()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.setLcdDisplay)
        self.timer.start(1000)
        
    def setLcdDisplay(self):
        self.delaySeconds -= 1
        displayTime = QtCore.QTime(0, (self.delaySeconds / 60) % 60, (self.delaySeconds) % 60)
        self.timeCount.ui.lcdNumber.display(displayTime.toString('mm:ss'))
        if self.delaySeconds == 0 :
            self.timer.stop()
            self.timeCount.accept()
            if self.path != None :
                self.media.play()
        
    def setTypeData(self):
        coco = QtGui.QListWidgetItem(self.ui.listWidgetLocal)
        coco.setIcon(QtGui.QIcon(':/Images/coco.jpg'))
        coco.setToolTip('coco')
        coco.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        
        brocadeHat = QtGui.QListWidgetItem(self.ui.listWidgetLocal)
        brocadeHat.setIcon(QtGui.QIcon(':/Images/brocade hat.jpg'))
        brocadeHat.setToolTip('brocade hat')
        brocadeHat.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        
        gorgeous = QtGui.QListWidgetItem(self.ui.listWidgetLocal)
        gorgeous.setIcon(QtGui.QIcon(':/Images/gorgeous.jpg'))
        gorgeous.setToolTip('gorgeous')
        gorgeous.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        
        peony = QtGui.QListWidgetItem(self.ui.listWidgetLocal)
        peony.setIcon(QtGui.QIcon(':/Images/peony.jpg'))
        peony.setToolTip('peony')
        peony.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        
        candle = QtGui.QListWidgetItem(self.ui.listWidgetLocal)
        candle.setIcon(QtGui.QIcon(':/Images/candle.jpg'))
        candle.setToolTip('candle')
        candle.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        
        potFlower = QtGui.QListWidgetItem(self.ui.listWidgetLocal)
        potFlower.setIcon(QtGui.QIcon(':/Images/pot flower.jpg'))
        potFlower.setToolTip('pot flower')
        potFlower.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        
        willow = QtGui.QListWidgetItem(self.ui.listWidgetLocal)
        willow.setIcon(QtGui.QIcon(':/Images/willow.jpg'))
        willow.setToolTip('willow')
        willow.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        
        mum = QtGui.QListWidgetItem(self.ui.listWidgetLocal)
        mum.setIcon(QtGui.QIcon(':/Images/mum.jpg'))
        mum.setToolTip('mum')
        mum.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        
        glint = QtGui.QListWidgetItem(self.ui.listWidgetLocal)
        glint.setIcon(QtGui.QIcon(':/Images/glint.jpg'))
        glint.setToolTip('glint')
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
        dialogAddFireworks = EditFireworks(self.localSession, self)
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
        pass
    
    @Slot(QtGui.QListWidgetItem)
    def refreshQuery(self, item):
        self.type = item.toolTip()
        self.query(self.type)
    
    def modeChanged(self):
        if self.ui.comboBoxMode.currentIndex() == 0:
            self.ui.pushButtonDelay.hide()
            self.ui.pushButtonUpLoad.hide()
            self.ui.seekSlider.setDisabled(False)
        else:
            self.ui.pushButtonDelay.show()
            self.ui.pushButtonUpLoad.show()
            self.stopMusic()
            self.ui.seekSlider.setDisabled(True)
            
        
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
            self.path = dialog.selectedFiles()[0]
            self.media.setCurrentSource(Phonon.MediaSource(self.path))
        dialog.deleteLater()
        
    def playOrPauseMusic(self):
        if self.path == None:
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
        
    #双击添加到脚本
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
        
    #刷新显示脚本     
    def refreshScript(self):
        self.proModel.clear()
        self.proModel.setHorizontalHeaderLabels(['UUID',  u'开爆时刻', u'烟花名称', u'尺寸', u'颜色', u'燃放方向', u'点火时刻', u'上升时间', u'效果时间', u'结束时刻', u'点火盒', u'点火点'])
        self.ui.scriptTableView.hideColumn(0)
        
        with self.proSession.begin():
            scriptTable = self.proSession.query (ProFireworksData).all()
            
        for i in xrange(len(scriptTable)):
            #分解notes获得效果时间和上升时间
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
     
    #音乐播放结束的时候重新开始数据归零    
    def mediaFinish(self):
        self.stopMusic()
        
    
# def main():
#     app = QtGui.QApplication(sys.argv)
# #     locale = QtCore.QLocale.system().name()
# ##    appTranslator = QtCore.QTranslator()
# ##    if appTranslator.load (":/loginWin_" + locale):
# ##        app.installTranslator (appTranslator)
#     window = Fireworks()
#     window.show()
#     sys.exit(app.exec_())
#     
# if __name__ == "__main__":
#     main()
