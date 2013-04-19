import sys
from PySide import QtCore,QtGui

from Ui_waveModule import Ui_widget_waveModule

from musicPlayer import Player
from upAndDownWaveWidget import UpAndDownWaveWidget

class WaveWidget(QtGui.QWidget):

    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_widget_waveModule()
        self.ui.setupUi(self)
        
        player = Player(self)
        self.ui.horizontalLayout_musicToolBox.addWidget(player)
        
        upAndDownWaveWidget = UpAndDownWaveWidget(self)
        self.upAndDownWaveWidget = upAndDownWaveWidget
        self.ui.horizontalLayout_plots.addWidget(upAndDownWaveWidget)
        
        upAndDownWaveWidget.setMedia(player.getPlayerMedia())
        
        player.signal.fileChoosedSignal.connect(upAndDownWaveWidget.analyzeWaveAndDrawInit)
        player.signal.TimeNowChanged.connect\
                (upAndDownWaveWidget.plotWidget.figure.mediaTimeChanged)
                

def main():
    app = QtGui.QApplication(sys.argv)
    waveWidget = WaveWidget()
    waveWidget.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
#    import cProfile
#    cProfile.run ('main()')
