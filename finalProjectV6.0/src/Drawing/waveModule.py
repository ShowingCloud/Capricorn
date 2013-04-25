from Models.EngineeringDB import ScriptData
from PySide import QtCore, QtGui
from PySide.QtCore import Slot
from Ui_waveModule import Ui_widget_waveModule
from musicPlayer import Player
from upAndDownWaveWidget import UpAndDownWaveWidget
import sys



class WaveWidget(QtGui.QWidget):

    def __init__(self, session, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_widget_waveModule()
        self.ui.setupUi(self)
        self.session = session
        
        self.igniteTimes = []
        player = Player(self)
        self.ui.horizontalLayout_musicToolBox.addWidget(player)
        
        upAndDownWaveWidget = UpAndDownWaveWidget(self)
        self.upAndDownWaveWidget = upAndDownWaveWidget
        self.ui.horizontalLayout_plots.addWidget(upAndDownWaveWidget)
        
        upAndDownWaveWidget.setMedia(player.getPlayerMedia())
        
        player.signal.fileChoosedSignal.connect(upAndDownWaveWidget.analyzeWaveAndDrawInit)
        player.signal.TimeNowChanged.connect\
                (upAndDownWaveWidget.upperPlotWidget.plotWidget.figure.mediaTimeChanged)
        self.getData()
#    def getScreenTime(self):
#        '''return tuple ,such as (4003, 4300) , the unit is ms ,
#        this means the current screen scope spreads between 4003ms t0 4300ms.
#        ''' 
##        print self.upAndDownWaveWidget.upperPlotWidget.plotWidget.figure.getScreenTime()
#        return self.upAndDownWaveWidget.upperPlotWidget.plotWidget.figure.getScreenTime()

    @Slot()
    def getData(self):
#        print 'aaaaaiii'
        with self.session.begin():
            data = self.session.query(ScriptData).all()
            
        self.igniteTimes = []
        for row in data:
            itime = row.IgnitionTime
#            print itime
#            print repr(itime),type(itime),dir(itime)
#            print itime.microseconds,itime.seconds,itime.total_seconds()
#            print 'getData seconds',itime.total_seconds()
            self.igniteTimes.append(itime.total_seconds())
        self.upAndDownWaveWidget.upperPlotWidget.plotWidget.figure.drawIgniteLines(self.igniteTimes)
            
#def main():
#     app = QtGui.QApplication(sys.argv)
#     waveWidget = WaveWidget()
#     waveWidget.show()
#     sys.exit(app.exec_())
#     
if __name__ == "__main__":
     from Frontend.LoginShow import main
     main()
    
