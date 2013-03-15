from PySide import QtCore
from matplotlib.figure import Figure
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.ticker as ticker

class fig(Figure):
    
    def __init__(self):
        super(fig,self).__init__()

        self.signal = freshSignal()
#        self. = self.bbox.bounds[2]
#        print 'a=',a
        
    def mediaTimeChanged(self,time):
        self.currentTime_ms = time
        self.fresh()
#    
#    def freshZoomwidth(self):
#        currentFrame = self.currentTime_ms * self.framerate * 1.0 / 1000
#        zoomWidth = self.framerate * self.visionSeconds
#        self.zoomLeftAndRight[1]= self.zoomLeftAndRight[0] + zoomWidth
        
    def fresh(self):
        if not hasattr(self, 'ax'):
            return
        if not hasattr(self, 'vline'):
            return
        if hasattr(self, 'pressX') and not self.pressX==None:
            self.currentTime_ms = self.media.currentTime ()
        currentFrame = self.currentTime_ms * self.framerate * 1.0 / 1000
        zoomWidth = self.framerate * self.visionSeconds
        self.zoomLeftAndRight[1] = self.zoomLeftAndRight[0] + zoomWidth
        if self.zoomLeftAndRight[1] < currentFrame:
            while 1:
                self.zoomLeftAndRight[0] += zoomWidth
                self.zoomLeftAndRight[1] += zoomWidth
                if self.zoomLeftAndRight[1] > currentFrame:
                    break
            self.ax.set_xlim(self.zoomLeftAndRight[0], self.zoomLeftAndRight[1])
        elif self.zoomLeftAndRight[0] > currentFrame:
            while 1:
                self.zoomLeftAndRight[0] -= zoomWidth
                self.zoomLeftAndRight[1] -= zoomWidth
                if self.zoomLeftAndRight[1] < currentFrame:
                    break
            self.ax.set_xlim(self.zoomLeftAndRight[0], self.zoomLeftAndRight[1])
            
        self.vline.set_xdata(currentFrame)
        self.canvas.draw()
        
        self.signal.freshLowerPlotPanLeftAndWidth.emit\
            (self.currentTime_ms*self.framerate*1.0/1000, self.visionSeconds*self.framerate)
#        print 'self.currentTime_ms=',self.currentTime_ms
        self.signal.freshTimeNowLabel.emit('%d:%06.3f'%(self.currentTime_ms/60000,self.currentTime_ms%60000*1.0/1000))
        self.signal.freshVisionTimeLengthLabel.emit(str(self.visionSeconds)+'s')
        
    def drawImage(self,dataDict):
        self.media = dataDict['media']     
        self.clf()
        self.waveData = dataDict['data']
        self.framerate = dataDict['framerate']
        self.visionSeconds = 20
        
        self.ax = self.add_axes([0.1,0.1,0.8,0.8])
        if isinstance(self.waveData, list):
            self.draw_2channel(zipRate=self.visionSeconds_2_ziprate(self.visionSeconds))
            self.signal.freshMusicTotalTimeLabel.emit(str('%d'%(self.media.totalTime()/1000)+'s'))
        else:
            self.draw_1channel(zipRate=self.visionSeconds_2_ziprate(self.visionSeconds))
            self.signal.freshMusicTotalTimeLabel.emit(str('%d'%(self.media.totalTime()/1000)+'s'))
        
        self.connectMoveAction()
        self.ax.axhline(y=0,color='0.8')
        self.vline = self.ax.axvline(x=0,color='red')
        self.currentTime_ms = 0
        self.zoomLeftAndRight = [0, 0]
        self.fresh()
        
    def visionSeconds_2_ziprate(self, visionSeconds):
        ziprate = int(visionSeconds*self.framerate/self.bbox.bounds[2])
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
            
#            ax.fill_between(xcenters, max_1, y2=min_1,color='0.6')
            
            ax.plot(xcenters,mean_1,'b')
            
#            print '-----------------'
#            print 'dataLength=',dataLength
#            print 'framerate=',self.framerate
#            print 'visionSeconds=',self.visionSeconds
#            print 'chunksize=',chunksize
#            print 'numchunks=',numchunks
#            print 'chunksize*numchunks=',chunksize*numchunks
#            print 'totalDots=',dataLength/2000
#            print '-----------------'

            majorLocator   = MultipleLocator(self.framerate*self.visionSeconds/6)
            def format_date(x, pos=None):
#                print 'format_date,x=',x
                y = x*1.0/self.framerate
                tupleTime = divmod(y, 60)
#                print 'tupleTime[0]=',tupleTime[0]
#                print 'tupleTime[1]=',tupleTime[1]
                return '%d:%06.3f'%(tupleTime[0],tupleTime[1])
            ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
            ax.xaxis.set_major_locator(majorLocator)
            
    def draw_2channel(self,zipRate=1000):
            dataOne = self.waveData[0]
            dataTwo = self.waveData[1]
            dataLength = len(dataOne)
            chunksize = int(zipRate)
            numchunks = dataLength // chunksize
#            print '-----------------'
#            print 'dotsInScreen=',self.framerate*self.visionSeconds/chunksize
#            print 'chunksize=',chunksize
#            print 'numchunks=',numchunks
#            print 'chunksize*numchunks=',chunksize*numchunks
#            print 'dataLength=',dataLength
#            print '-----------------'
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
#            ax.plot(xcenters,mean_1,'b',xcenters,mean_2,'y')
            print 'plot2'
            
            self.visionSeconds/6
#            majorLocator   = MultipleLocator(self.framerate*self.visionSeconds/6)
##            majorLocator   = MultipleLocator(1)
##            def format_date(x, pos=None):
##                tupleTime = divmod(x, self.framerate)
##                return '%d:%02d'%(tupleTime[0],tupleTime[1])
##            ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
#            ax.xaxis.set_major_locator(majorLocator)
            
#            interval = self.media.tickInterval()
#            self.timer.start(interval)
            
    def zoomIn(self):
        self.visionSeconds = self.visionSeconds/2.0
        if isinstance(self.waveData, list):
            self.draw_2channel(zipRate=self.visionSeconds_2_ziprate(self.visionSeconds))
        else:
            self.draw_1channel(zipRate=self.visionSeconds_2_ziprate(self.visionSeconds))
#        self.freshZoomwidth()
        self.fresh()
        
    def zoomOut(self):
        self.visionSeconds = self.visionSeconds*2.0
        if isinstance(self.waveData, list):
            self.draw_2channel(zipRate=self.visionSeconds_2_ziprate(self.visionSeconds))
        else:
            self.draw_1channel(zipRate=self.visionSeconds_2_ziprate(self.visionSeconds))
#        self.freshZoomwidth()
        self.fresh()
        
#    def speedUp(self):
#        pass
##        self.lengthPerMove = self.lengthPerMove*2.0
#    
#    def speedDown(self):
#        pass
##        self.lengthPerMove = self.lengthPerMove/2.0

        
    def connectMoveAction(self):
        self.pressX = None
        self.connect()
    def connect(self):
        self.cidpress = self.canvas.mpl_connect(
        'button_press_event', self.on_press)
        self.cidrelease = self.canvas.mpl_connect(
        'button_release_event', self.on_release)
        self.cidmotion = self.canvas.mpl_connect(
        'motion_notify_event', self.on_motion)
    def on_press(self, event):
        if event.inaxes != self.ax: return
        self.pressX = event.xdata
        self.currentTime2_ms = 0
        if  abs(self.vline.get_xdata()-self.pressX) < self.framerate*self.visionSeconds/5:
            self.currentTime2_ms = self.media.currentTime()
        else:
            self.pressX = None
    def on_motion(self, event):
        if self.pressX is None: return
        if event.inaxes != self.ax: return
        dx = event.xdata - self.pressX
        print 'dx=',dx
        self.currentTime2_ms += dx*1000/self.framerate
#        print 'self.currentTime2_ms=',self.currentTime2_ms
        if self.currentTime2_ms < 0:
            return
        self.media.seek(self.currentTime2_ms)
        self.fresh()
        
    def on_release(self, event):
        self.pressX = None
#        self.fresh()

        

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
