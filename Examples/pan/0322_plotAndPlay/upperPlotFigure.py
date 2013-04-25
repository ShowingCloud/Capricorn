from PySide import QtCore
from matplotlib.figure import Figure
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.ticker as ticker

class fig(Figure):
    
    def __init__(self):
        super(fig,self).__init__()
        self.signal = freshSignal()
        self.dotsInScreen = 2000
        self.secondsInScreen = 20
                
    def mediaTimeChanged(self,time):
        self.currentTime_ms = int(time)
        self.fresh()
        pass
    
    def fresh(self):
        if not hasattr(self, 'ax'):
            return
        if hasattr(self, 'pressX') and not self.pressX==None:
            self.currentTime_ms = self.media.currentTime ()
#        
        frameNow = self.currentTime_ms*self.framerate/1000
        framesInScreen = self.secondsInScreen*self.framerate
        totalFrame = self.media.totalTime ()*self.framerate/1000
        
        dotNow = frameNow/self.zipRate
        self.signal.freshLowerPlotCurrentTime.emit(frameNow)
        print '------------'
        print 'frameNow=',frameNow
        totalDots = self.plotDataDict['y_max'].size
        
        if dotNow < self.dotsInScreen/2:
            sliceList = range(0, dotNow+self.dotsInScreen/2)
            self.plotFunc(sliceList)
            self.ax.set_xlim(dotNow-self.dotsInScreen/2,dotNow+self.dotsInScreen/2)
            self.vline.set_xdata(dotNow)
            self.signal.freshLowerPlotPanLeftAndWidth.emit\
                (0,frameNow+framesInScreen/2)
                
        elif dotNow < totalDots - self.dotsInScreen/2:
            sliceList = range(dotNow-self.dotsInScreen/2, dotNow+self.dotsInScreen/2)
            self.plotFunc(sliceList)
            self.ax.set_xlim(0,self.dotsInScreen)
            self.vline.set_xdata(self.dotsInScreen/2)
            self.signal.freshLowerPlotPanLeftAndWidth.emit\
                (frameNow-framesInScreen/2,frameNow+framesInScreen/2)
                
        else:
            sliceList = range(dotNow-self.dotsInScreen/2, totalDots)
            self.plotFunc(sliceList)
            self.ax.set_xlim(0,self.dotsInScreen)
            self.vline.set_xdata(self.dotsInScreen/2)
            self.signal.freshLowerPlotPanLeftAndWidth.emit\
                (frameNow-framesInScreen/2,totalFrame)
                
        self.canvas.draw()
        
    def drawInit(self,dataDict):
        print 'drawInit'
        self.clf()
        self.media = dataDict['media']
        self.waveData = dataDict['data']
        self.framerate = dataDict['framerate']
        self.zipRate = int(self.secondsInScreen*self.framerate/self.dotsInScreen)
        
        self.plotDataDict = self.plotDataProcess(self.zipRate)
        if hasattr(self, 'ax'):
            self.ax.clear()
        self.ax = self.add_axes([0.1,0.1,0.8,0.8])
        self.ax.axhline(y=0,color='0.8',zorder=2)
        self.vline = self.ax.axvline(x=0,color='red',zorder=3)
        self.mediaTimeChanged(0)
        
    def plotFunc(self,sliceList):
        plotDataDict = self.plotDataDict
        if hasattr(self, 'linePlot'):
            if isinstance(self.linePlot, list):
                for line in self.linePlot: line.remove()
            else:
                self.linePlot.remove()
        if hasattr(self, 'fillPlot'):
            self.fillPlot.remove()
        xarray = np.arange(len(sliceList))
        if isinstance(self.waveData, list):
            ymax = plotDataDict['y_max'][np.array(sliceList)]
            ymin = plotDataDict['y_min'][np.array(sliceList)]
            ymean = plotDataDict['y_mean'][np.array(sliceList)]
            ymean2 = plotDataDict['y_mean_2'][np.array(sliceList)]
            self.fillPlot = self.ax.fill_between(xarray, ymax, y2=ymin , color='c', zorder=0)
            self.linePlot = self.ax.plot(xarray,ymean,'pink',xarray,ymean2,'y',zorder=1)
        else:
            ymax = plotDataDict['y_max'][np.array(sliceList)]
            ymin = plotDataDict['y_min'][np.array(sliceList)]
            ymean = plotDataDict['y_mean'][np.array(sliceList)]
            self.fillPlot = self.ax.fill_between(xarray, ymax, y2=ymin , color='.6',zorder=0)
            self.linePlot, = self.ax.plot(xarray,ymean,'pink',zorder=1)
                
    def plotDataProcess(self, zipRate):
        waveData = self.waveData
        if isinstance(waveData, list):
            dataOne = waveData[0]
            dataTwo = waveData[1]
            dataLength = len(dataOne)
            chunksize = zipRate
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
            plotDataDict = dict(y_max=max_1_2, y_min=min_1_2, y_mean=mean_1, y_mean_2=mean_2)
        else:
            dataLength = len(waveData)
            chunksize = zipRate
            numchunks = dataLength // chunksize            
            team_1 = waveData[:chunksize*numchunks].reshape((-1, chunksize)) 
            max_1 = team_1.max(axis=1)
            min_1 = team_1.min(axis=1)
            mean_1 = team_1.mean(axis=1)
            plotDataDict = dict(y_max=max_1, y_min=min_1, y_mean=mean_1)
        return plotDataDict
        
    def freshFromLowerPlot(self,dx):
#        self.currentTime_ms += dx*1000/self.framerate
#        self.fresh()
        pass 

class freshSignal(QtCore.QObject):
    freshLowerPlotPanLeftAndWidth = QtCore.Signal(int, int)
    freshLowerPlotCurrentTime = QtCore.Signal(int)
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
