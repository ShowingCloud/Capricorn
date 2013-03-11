from PySide import QtCore
from matplotlib.figure import Figure
from PySide.phonon import Phonon
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.ticker as ticker

class fig(Figure):
    def __init__(self):
        super(fig,self).__init__()
#        self.visionSeconds = 0
        
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
        if not hasattr(self, 'vline'):
            return
        currentFrame = self.getPlayerTime() * self.framerate * 1.0 / 1000
        zoomWidth = self.framerate * self.visionSeconds
        zoomLeft = currentFrame - zoomWidth/2.0
        zoomRigt = currentFrame + zoomWidth/2.0
        self.ax.set_xlim(zoomLeft, zoomRigt)
        self.vline.set_xdata(zoomLeft+zoomWidth/2.0)
        self.canvas.draw()
        
        self.signal.freshLowerPlotPanLeftAndWidth.emit(zoomLeft, zoomWidth)
        self.signal.freshTimeNowLabel.emit('%d:%02d'%(divmod(currentFrame/self.framerate,60)))
        self.signal.freshVisionTimeLengthLabel.emit(str('%d'%(zoomWidth/self.framerate))+'s')
        
#    def freshFromLowerPlot(self,left,width):
#        pass
##        self.x = left
##        self.zoomWidth = width
##        self.ax.set_xlim(self.x,self.x+self.zoomWidth)
##        self.vline.set_xdata(self.x+self.zoomWidth/2.0)
##        self.canvas.draw()
    

    def drawImage(self,dataDict):
        self.media = dataDict['media']
        if self.media.state() == Phonon.PausedState:
            return
#        sourcePath = dataDict['path']
#        if self.media.currentSource().url().path() == unicode(sourcePath):
#            print 'self.media.currentSource().url().path() == unicode(sourcePath):'
#            return
#        print 'self.media.currentSource().url().path() == ',self.media.currentSource().url().path()
#        print 'sourcePath == ',sourcePath
#        print 'sourcePath == self.media.currentSource().url().path():',sourcePath == self.media.currentSource().url().path()
        if hasattr(self,'oldMediaPath') and self.oldMediaPath==self.media.currentSource():
            return
        
        self.oldMediaPath = self.media.currentSource()
        
        self.waveData = dataDict['data']
        self.framerate = dataDict['framerate']
        interval = self.media.tickInterval ()
        self.getPlayerTime = self.media.currentTime
        self.visionSeconds = 20
        
        self.ax = self.add_axes([0.1,0.1,0.8,0.8])
#        print dir(self.ax)
        if isinstance(self.waveData, list):
            self.draw_2channel(zipRate=self.visionSeconds_2_ziprate(self.visionSeconds))
            self.signal.freshMusicTotalTimeLabel.emit(str('%d'%(len(self.waveData[0])/self.framerate))+'s')
        else:
            self.draw_1channel(zipRate=self.visionSeconds_2_ziprate(self.visionSeconds))
            self.signal.freshMusicTotalTimeLabel.emit(str('%d'%(len(self.waveData)/self.framerate))+'s')
        
#        self.connectMoveAction()
        self.ax.axhline(y=0,color='0.8')
        self.vline = self.ax.axvline(x=0,color='red')
        
        self.fresh()
        self.timer.start(interval)
        
    def visionSeconds_2_ziprate(self, visionSeconds):
        ziprate = 50 * visionSeconds + 100
        return ziprate
    
    def draw_1channel(self,zipRate=1000):
            dataOne = self.waveData
            dataLength = len(dataOne)
            chunksize = zipRate
            numchunks = dataLength // chunksize
             
            team_1 = dataOne[:chunksize*numchunks].reshape((-1, chunksize)) 
            max_1 = team_1.max(axis=1)
            min_1 = team_1.min(axis=1)
            mean_1 = team_1.mean(axis=1)
            xcenters = np.linspace(0, dataLength, numchunks)
            self.ax.clear()
            ax = self.ax
            ax.fill_between(xcenters, max_1, y2=min_1,color='0.6')
            ax.plot(xcenters,mean_1,'b')
            
            majorLocator   = MultipleLocator(self.framerate*self.visionSeconds/6)
            def format_date(x, pos=None):
                return '%d:%02d'%(divmod(x/self.framerate,60))
            ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
            ax.xaxis.set_major_locator(majorLocator)
            
            interval = self.media.tickInterval ()
            self.timer.start(interval)
            
    def draw_2channel(self,zipRate=1000):
            dataOne = self.waveData[0]
            dataTwo = self.waveData[1]
            dataLength = len(dataOne)
            chunksize = zipRate
            numchunks = dataLength // chunksize
            print 'dotsInScreen=',self.framerate*self.visionSeconds/chunksize
            
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
            
            xcenters = np.linspace(0, dataLength, numchunks)
#            self.ax.clear()
            ax = self.ax
            ax.fill_between(xcenters, max_1_2, y2=min_1_2,color='0.6')
            ax.plot(xcenters,mean_1,'b',xcenters,mean_2,'y')
            print 'plot2'
            
            majorLocator   = MultipleLocator(self.framerate*self.visionSeconds/6)
            def format_date(x, pos=None):
                return '%d:%02d'%(divmod(x/self.framerate,60))
            ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
            ax.xaxis.set_major_locator(majorLocator)
            
            interval = self.media.tickInterval()
            self.timer.start(interval)
            
    def zoomIn(self):
        self.visionSeconds = self.visionSeconds/2.0
        if isinstance(self.waveData, list):
            self.draw_2channel(zipRate=self.visionSeconds_2_ziprate(self.visionSeconds))
        else:
            self.draw_1channel(zipRate=self.visionSeconds_2_ziprate(self.visionSeconds))
        self.fresh()
        
    def zoomOut(self):
        self.visionSeconds = self.visionSeconds*2.0
        if isinstance(self.waveData, list):
            self.draw_2channel(zipRate=self.visionSeconds_2_ziprate(self.visionSeconds))
        else:
            self.draw_1channel(zipRate=self.visionSeconds_2_ziprate(self.visionSeconds))
        self.fresh()
        
#    def speedUp(self):
#        pass
##        self.lengthPerMove = self.lengthPerMove*2.0
#    
#    def speedDown(self):
#        pass
##        self.lengthPerMove = self.lengthPerMove/2.0
#            
#    def connectMoveAction(self):
#        self.pressX = None
#        self.connect()
#    def connect(self):
#        'connect to all the events we need'
#        self.cidpress = self.canvas.mpl_connect(
#        'button_press_event', self.on_press)
#        self.cidrelease = self.canvas.mpl_connect(
#        'button_release_event', self.on_release)
#        self.cidmotion = self.canvas.mpl_connect(
#        'motion_notify_event', self.on_motion)
#    def on_press(self, event):
#        'on button press we will see if the mouse is over us and store some data'
#        if event.inaxes != self.ax: return
#        self.pressX =event.xdata
#    def on_motion(self, event):
#        'on motion we will move the rect if the mouse is over us'
#        if self.pressX is None: return
#        if event.inaxes != self.ax: return
#        dx = event.xdata - self.pressX
#        self.x -= dx
#        self.fresh()
#    def on_release(self, event):
#        'on release we reset the press data'
#        self.pressX = None
#        self.fresh()
#
#        

class freshSignal(QtCore.QObject):
    freshLowerPlotPanLeftAndWidth = QtCore.Signal(int, int)
    freshTimeNowLabel = QtCore.Signal(str)
    freshMusicTotalTimeLabel = QtCore.Signal(str)
    freshVisionTimeLengthLabel = QtCore.Signal(str)
    
if __name__ == "__main__":
    import plotAndPlay
    from PySide import QtGui
    import sys
    app = QtGui.QApplication(sys.argv)
    playAndPlot = plotAndPlay.playAndPlotWidget()
    playAndPlot.show()
    sys.exit(app.exec_())
