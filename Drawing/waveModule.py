from Models.EngineeringDB import ScriptData ,IgnitorsData
from PySide import QtCore, QtGui
from PySide.QtCore import Slot
from Ui_waveModule import Ui_widget_waveModule
from musicPlayer import Player
from upAndDownWaveWidget import UpAndDownWaveWidget
from Models.LocalDB import FireworksData
import sys

class WaveWidget(QtGui.QWidget):

    def __init__(self, session=None ,musicPath=None, sess=None, parent=None):
        self.show = False
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_widget_waveModule()
        self.ui.setupUi(self)
        self.sess = sess
        self.session = session
        self.musicPath = musicPath
#         print self.musicPath
        self.igniteList = []
        player = Player(self)
        self.player = player
        self.ui.horizontalLayout_musicToolBox.addWidget(player)
        
        upAndDownWaveWidget = UpAndDownWaveWidget(self)
        self.upAndDownWaveWidget = upAndDownWaveWidget
        self.ui.horizontalLayout_plots.addWidget(upAndDownWaveWidget)
        
        
        upAndDownWaveWidget.setMedia(player.getPlayerMedia())
        
#        player.signal.fileChoosedSignal.connect(upAndDownWaveWidget.analyzeWaveAndDrawInit)
        self.draw = upAndDownWaveWidget.analyzeWaveAndDrawInit
        player.setMusicFilePath(self.musicPath)
        
        player.signal.TimeNowChanged.connect\
                (upAndDownWaveWidget.plotWidget.figure.mediaTimeChanged)
        
        player.ui.pushButton_zoomIn.clicked.connect(upAndDownWaveWidget.plotWidget.figure.zoomIn)
        player.ui.pushButton_zoomOut.clicked.connect(upAndDownWaveWidget.plotWidget.figure.zoomOut)
        
        player.ui.pushButton_goLeft.clicked.connect(upAndDownWaveWidget.plotWidget.figure.toNextScreen)
        player.ui.pushButton_goRight.clicked.connect(upAndDownWaveWidget.plotWidget.figure.toPreviousScreen)
        player.ui.pushButton_musicPlay.clicked.connect(self.getData)
        
#        self.getData()
    @Slot()
    def getData(self):
        with self.session.begin():
            data = self.session.query(ScriptData).all()
            
        self.igniteList = []
        for row in data:
            itime = row.IgnitionTime
            firework = row.FireworkID
            boxUUID = row.IgnitorID
            scriptUUID = row.UUID
            with self.session.begin():
                rowBox = self.session.query(IgnitorsData).filter_by(UUID = boxUUID).first()
                if rowBox != None:
                    boxID = rowBox.BoxID
                else:
                    boxID = None
            with self.sess.begin():
                fire = self.sess.query(FireworksData).filter_by(UUID = firework).first()
                fireName = fire.Name
            dtime = fire.RisingTime
            itime = itime + dtime
            igniteObject = igniteClass(itime=itime.total_seconds(), fireName=fireName,\
                                        fire=fire, boxID=boxID, fireWork=firework, boxUUID=boxUUID, scriptUUID=scriptUUID )
            self.igniteList.append(igniteObject)
        self.upAndDownWaveWidget.plotWidget.figure.setIgniteList(self.igniteList)
        self.upAndDownWaveWidget.plotWidget.figure.drawIgniteLines()
       
    def enterEvent(self, e):
        if not self.show:
            self.show = True
            self.draw()
        
class igniteClass(QtCore.QObject):
    def __init__(self,itime=None,fireName=None, fire=None, boxID= None, fireWork= None, boxUUID= None,scriptUUID=None):
        super(igniteClass,self).__init__()
        self.itime = itime
        self.fireName = fireName
        self.boxID = boxID
#        self.rowBox = rowBox
        self.fire = fire
        self.fireWork = fireWork
        self.boxUUID = boxUUID
        self.scriptUUID = scriptUUID

#     @Slot()
#     def getData(self):
#         with self.session.begin():
#             data = self.session.query(ScriptData).all()
#             
#         self.igniteList = []
#         for row in data:
#             itime = row.IgnitionTime
#             firework = row.FireworkID
#             boxUUID = row.IgnitorID
#             with self.session.begin():
#                 rowBox = self.session.query(IgnitorsData).filter_by(UUID = boxUUID).first()
#                 if rowBox != None:
#                     boxID = rowBox.BoxID
#                 else:
#                     boxID = None
#             with self.sess.begin():
#                 fire = self.sess.query(FireworksData).filter_by(UUID = firework).first()
#                 fireName = fire.Name
#             dtime = fire.RisingTime
#             itime = itime + dtime
#             igniteObject = igniteClass(itime=itime.total_seconds(), fireName=fireName,\
#                                         fire=fire, boxID=boxID, fireWork=firework, boxUUID=boxUUID )
#             self.igniteList.append(igniteObject)
#         self.upAndDownWaveWidget.plotWidget.figure.setIgniteList(self.igniteList)
#         self.upAndDownWaveWidget.plotWidget.figure.drawIgniteLines()
#        
#     def enterEvent(self, e):
#         if not self.show:
#             self.show = True
#             self.draw()
#         
# class igniteClass(QtCore.QObject):
#     def __init__(self,itime=None,fireName=None, fire=None, boxID= None, fireWork= None, boxUUID= None):
#         super(igniteClass,self).__init__()
#         self.itime = itime
#         self.fireName = fireName
#         self.boxID = boxID
# #        self.rowBox = rowBox
#         self.fire = fire
#         self.fireWork = fireWork
#         self.boxUUID = boxUUID
    
def main():
     app = QtGui.QApplication(sys.argv)
     waveWidget = WaveWidget()
     
     waveWidget.show()
     sys.exit(app.exec_())
#     
if __name__ == "__main__":
    main()
#     from Frontend.LoginShow import main
#     main()
    
