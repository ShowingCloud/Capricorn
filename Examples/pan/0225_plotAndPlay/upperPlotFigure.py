from PySide import QtCore
from matplotlib.figure import Figure
from PySide.phonon import Phonon
import numpy as np

class fig(Figure):
    def __init__(self):
        super(fig,self).__init__()
        self.zoomWidth = 0
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.freshOrNot)
        self.signal = freshSignal()
        
    def freshOrNot(self):
        if self.media.state() == Phonon.PlayingState:
            self.fresh()
        else:
            return
        
    def fresh(self):
        if not hasattr(self, 'ax'):
            return
        timeNow = self.getPlayerTime() * self.framerate * 1.0 / 1000
        
        zoomLeft = timeNow - self.zoomWidth/2.0
        zoomRigt = timeNow + self.zoomWidth/2.0
        self.ax.set_xlim(zoomLeft, zoomRigt)
        self.vline.set_xdata(timeNow)
        self.canvas.draw()
        
        self.signal.freshFunction.emit(zoomLeft, self.zoomWidth)
        self.signal.freshTimeNow.emit('%d'%timeNow)
        self.signal.visionTimeLength.emit('%d'%self.zoomWidth)
        
    def freshFromLowerPlot(self,left,width):
        pass
#        self.x = left
#        self.zoomWidth = width
#        self.ax.set_xlim(self.x,self.x+self.zoomWidth)
#        self.vline.set_xdata(self.x+self.zoomWidth/2.0)
#        self.canvas.draw()
        
    def drawImage(self,dataDict):
        print 'drawImage'
        waveData = dataDict['data']
        self.framerate = dataDict['framerate']
        
#        interval = dataDict['interval'].tickInterval ()
#        self.timeNow = dataDict['currentTimeFuntion']

        self.media = dataDict['media']
        interval = self.media.tickInterval ()
        self.getPlayerTime = self.media.currentTime
        
        self.clf()
        self.ax = self.add_axes([0.1,0.1,0.8,0.8])
        ax = self.ax  
        dataOne = 0
        dataTwo = 0
        if isinstance(waveData, list):
            
            dataOne = waveData[0]
            dataTwo = waveData[1]
            dataLength = len(dataOne)
            chunksize = 1000
            numchunks = dataLength // chunksize
             
            team_1 = dataOne[:chunksize*numchunks].reshape((-1, chunksize))
            team_2 = dataTwo[:chunksize*numchunks].reshape((-1, chunksize))
            
            max_1 = team_1.max(axis=1)
            max_2 = team_2.max(axis=1)
            max_1_2 = np.maximum(max_1,max_2)

            min_1 = team_1.min(axis=1)
            min_2 = team_2.min(axis=1)
            min_1_2 = np.minimum(min_1,min_2)
            
            mean_1 = team_1.mean(axis=1)
            mean_2 = team_2.mean(axis=1)
            
            xchunks = np.linspace(0, dataLength, numchunks)
#            xcenters = xchunks.mean(axis=0)
            xcenters = xchunks

            ax.fill_between(xcenters, max_1_2, y2=min_1_2,color='0.6')
            ax.plot(xcenters,mean_1,'b',xcenters,mean_2,'y')
        else:
            dataOne = waveData
            ax.plot(dataOne,'b')
#        dataLength = len(dataOne)
##        del dataOne,dataTwo
#        print dataLength
        
#        self.connectMoveAction()
        ax.axhline(y=0,color='0.8')
        self.vline = ax.axvline(x=0,color='red')
        
#        self.signal.freshTotalTime.emit('%d'%dataLength)
        self.zoomWidth = self.framerate * 20
        
        self.fresh()
        self.timer.start(interval)
#        

        
    def zoomIn(self):
        self.zoomWidth = self.zoomWidth/2.0
        self.fresh()
        
    def zoomOut(self):
        self.zoomWidth = self.zoomWidth*2.0
        self.fresh()
        
    def speedUp(self):
        pass
#        self.lengthPerMove = self.lengthPerMove*2.0
    
    def speedDown(self):
        pass
#        self.lengthPerMove = self.lengthPerMove/2.0
            
    def connectMoveAction(self):
        self.pressX = None
        self.connect()
    def connect(self):
        'connect to all the events we need'
        self.cidpress = self.canvas.mpl_connect(
        'button_press_event', self.on_press)
        self.cidrelease = self.canvas.mpl_connect(
        'button_release_event', self.on_release)
        self.cidmotion = self.canvas.mpl_connect(
        'motion_notify_event', self.on_motion)
    def on_press(self, event):
        'on button press we will see if the mouse is over us and store some data'
        if event.inaxes != self.ax: return
        self.pressX =event.xdata
    def on_motion(self, event):
        'on motion we will move the rect if the mouse is over us'
        if self.pressX is None: return
        if event.inaxes != self.ax: return
        dx = event.xdata - self.pressX
        self.x -= dx
        self.fresh()
    def on_release(self, event):
        'on release we reset the press data'
        self.pressX = None
        self.fresh()

        
class freshSignal(QtCore.QObject):
    freshFunction = QtCore.Signal(int, int)
    freshTimeNow = QtCore.Signal(str)
    freshTotalTime = QtCore.Signal(str)
    visionTimeLength = QtCore.Signal(str)
    
if __name__ == "__main__":
    fig2 = fig()
