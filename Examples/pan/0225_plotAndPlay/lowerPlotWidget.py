# coding=utf-8
import numpy as np
from PySide import QtGui,QtCore
import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.collections import PatchCollection
import matplotlib.patches as mpatches
from matplotlib import mpl
import waveForm
import sys

class plotWidget(FigureCanvas):
    def __init__(self, parent=None):
        self.figure = fig()
        super(plotWidget,self).__init__(self.figure)
        self.setParent(parent)
        self.setWindowTitle("pyside test_plot fig FigureCanvas")
        
#        
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
#        
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
#
#        timeNowLabel = QtGui.QLabel('time now:',self)
#        timeNowLabel.setAlignment(QtCore.Qt.AlignHCenter)
#        timeNOwLineEdit = QtGui.QLineEdit(self)
#       
#        totalTimeLabel = QtGui.QLabel('total time:',self)
#        totalTimeLengthLabel = QtGui.QLabel('',self)
#        
#        visionTimeLabel = QtGui.QLabel('vision time:',self)
#        visionTimeLineEdit = QtGui.QLineEdit(self)
#        
#        controlLayout2=QtGui.QGridLayout ()
#        controlLayout2.addWidget(timeNowLabel,0,0,1,1)
#        controlLayout2.addWidget(timeNOwLineEdit,0,1,1,2)
#        controlLayout2.addWidget(totalTimeLabel,0,3,1,1)
#        controlLayout2.addWidget(totalTimeLengthLabel,0,4,1,2)
#        controlLayout2.addWidget(visionTimeLabel,0,6,1,1)
#        controlLayout2.addWidget(visionTimeLineEdit,0,8,1,2)
#        
#        layout=QtGui.QVBoxLayout()
#        layout.addWidget(self.plotWidget)
#        layout.addLayout(controlLayout)
#        layout.addLayout(controlLayout2)
#        self.setLayout(layout)
#        
        
        
class fig(Figure):
    def __init__(self):
        super(fig,self).__init__()
#        self.x = 1000
#        self.spanWidth = 300
#        self.timeInterval = 10
#        self.lengthPerMove = 3
#        self.direction = 1
        self.signal = freshSignal()
        
#        self.timer = QtCore.QTimer()
#        self.timer.timeout.connect(self.timerFunction)
#        
#    def setSpanWidth(self,width):
#        self.spanWidth = width
#        self.span.set_xy(self.x, self.x+self.spanWidth)
#    def move(self,dx):
#        self.x = self.x + dx
#        self.span.set_xy(self.x, self.x+self.spanWidth)
#    def timerFunction(self):
#        self.x = self.x + self.lengthPerMove*self.direction
#        self.setX()

#    @QtCore.Slot(int, int)
    def freshFromUpperPlot(self,left, width):
        self.left = left
        self.width = width
        if self.left<0:
            self.ax.set_xlim(self.left,self.dataLength)
        elif self.left+self.width<self.dataLength:
            self.ax.set_xlim(0,self.dataLength)
        else:
            self.ax.set_xlim(0,self.left+self.width)
            
        right = self.left + self.width
        xy = np.array([[self.left,0.],[self.left,1.],[right,1.],[right,0.],[self.left,0.]])
        self.span.set_xy(xy)
        self.vline.set_xdata(self.left+self.width/2.0)
        self.canvas.draw()
    def fresh2(self):
        self.freshFromUpperPlot(self.left, self.width)
    def drawImage(self,wave):
        self.clf()
        self.ax = self.add_axes([0.1,0.1,0.8,0.8])
        ax = self.ax
#        
        if isinstance(wave, list):
#            print 'wave=',wave
            dataOne = wave[0]
            dataTwo = wave[1]
#            len = len(dataOne)
            ax.plot(dataOne,'b',dataTwo,'y')
        else:
#            print 'wave=',wave
            dataOne = wave
            ax.plot(dataOne,'b')
        self.dataLength = len(dataOne)
#        print 'length=',self.length
        self.span = ax.axvspan(0, 0, facecolor='g', alpha=0.5,zorder=3)
        self.vline = ax.axvline(x=0,color='red')
        self.canvas.draw()
        self.connectMoveAction()
        
    def connectMoveAction(self):
        self.pressX = None
        self.connect()
    def connect(self):
        'connect to all the events we need'
        self.cidpress = self.canvas.mpl_connect(
        'button_press_event', self.on_press)
        self.cidrelease = self.canvas.mpl_connect(
        'button_release_event', self.on_release)
    def on_press(self, event):
        if event.inaxes != self.ax: return
        contains, attrd = self.span.contains(event)
        if not contains: return
        self.pressX =event.xdata
        
    def on_release(self, event):
        if self.pressX is None: return
        if event.inaxes != self.ax: return
        dx = event.xdata - self.pressX
        self.left += dx
        self.fresh2()
        self.signal.freshFunction.emit(self.left, self.width)        
        self.pressX = None
        
class freshSignal(QtCore.QObject):
    freshFunction = QtCore.Signal(int, int)
    
if __name__ == '__main__':
#    import time
    app = QtGui.QApplication(sys.argv)
    dialog = QtGui.QFileDialog()
    dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
    path = 0
    if dialog.exec_() == QtGui.QDialog.Accepted:
        path = dialog.selectedFiles()[0]
#        print path
    dialog.deleteLater()
    print path
    form = waveForm.waveform(path)
    plot_Widget = plotWidget()
#    time.sleep(2)
    plot_Widget.figure.drawImage(form.getWaveData())
#    plot_Widget.figure.drawImage((1,8,3))
    plot_Widget.show()
 
    sys.exit(app.exec_())
    