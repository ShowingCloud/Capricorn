from PySide import QtGui,QtCore
from plotWidget import plotWidget
class plotControlWidget(QtGui.QWidget):
    def __init__(self,parent=None):
        super(plotControlWidget,self).__init__(parent)
        
        self.plotWidget = plotWidget()
          
#        self.buttonPlay = QtGui.QPushButton('go', self) 
#        self.buttonReverse = QtGui.QPushButton('reverse', self)       
#        self.buttonStop = QtGui.QPushButton('Stop', self)
#        
#        self.buttonGoRight = QtGui.QPushButton('goRight', self)
#        self.buttonGoLeft = QtGui.QPushButton('goLeft', self)
#        
#        self.buttonZoomIn = QtGui.QPushButton('ZoomIn', self)
#        self.buttonZoomOut = QtGui.QPushButton('ZoomOut', self)
#        
#        self.buttonSpeedUp = QtGui.QPushButton('quicker', self)
#        self.buttonSpeedDown = QtGui.QPushButton('slower', self)
        
#        self.buttonPlay.clicked.connect(self.plotWidget.figure.startMove)
#        self.buttonReverse.clicked.connect(self.plotWidget.figure.reverseMove)
#        self.buttonStop.clicked.connect(self.plotWidget.figure.pauseMove)
#        self.buttonGoRight.clicked.connect(self.plotWidget.figure.goRight)
#        self.buttonGoLeft.clicked.connect(self.plotWidget.figure.goLeft)
#        self.buttonZoomIn.clicked.connect(self.plotWidget.figure.zoomIn)
#        self.buttonZoomOut.clicked.connect(self.plotWidget.figure.zoomOut)
#        self.buttonSpeedUp.clicked.connect(self.plotWidget.figure.speedUp)
#        self.buttonSpeedDown.clicked.connect(self.plotWidget.figure.speedDown)
#        
#        controlLayout=QtGui.QHBoxLayout()
#        controlLayout.addWidget(self.buttonPlay)
#        controlLayout.addWidget(self.buttonReverse)
#        controlLayout.addWidget(self.buttonStop)
#        controlLayout.addWidget(self.buttonGoRight)
#        controlLayout.addWidget(self.buttonGoLeft) 
#        controlLayout.addWidget(self.buttonZoomIn)
#        controlLayout.addWidget(self.buttonZoomOut)
#        controlLayout.addWidget(self.buttonSpeedUp)
#        controlLayout.addWidget(self.buttonSpeedDown)

        timeNowLabel = QtGui.QLabel('time now:',self)
        timeNowLabel.setAlignment(QtCore.Qt.AlignHCenter)
        timeNowLineEdit = QtGui.QLineEdit(self)
        
        totalTimeLabel = QtGui.QLabel('total time:',self)
        totalTimeLengthLabel = QtGui.QLabel('',self)
        
        visionTimeLabel = QtGui.QLabel('vision time:',self)
        visionTimeLineEdit = QtGui.QLineEdit(self)
        
        controlLayout2=QtGui.QGridLayout ()
        controlLayout2.addWidget(timeNowLabel,0,0,1,1)
        controlLayout2.addWidget(timeNowLineEdit,0,1,1,2)
        controlLayout2.addWidget(totalTimeLabel,0,3,1,1)
        controlLayout2.addWidget(totalTimeLengthLabel,0,4,1,2)
        controlLayout2.addWidget(visionTimeLabel,0,6,1,1)
        controlLayout2.addWidget(visionTimeLineEdit,0,8,1,2)
        
        layout=QtGui.QVBoxLayout()
        layout.addWidget(self.plotWidget)
#        layout.addLayout(controlLayout)
        layout.addLayout(controlLayout2)
        self.setLayout(layout)
        
    
        self.plotWidget.figure.signal.freshTimeNowLabel.connect(timeNowLineEdit.setText)
        self.plotWidget.figure.signal.freshMusicTotalTimeLabel.connect(totalTimeLengthLabel.setText)
        self.plotWidget.figure.signal.freshVisionTimeLengthLabel.connect(visionTimeLineEdit.setText)
         
    def lineGo(self):
        pass