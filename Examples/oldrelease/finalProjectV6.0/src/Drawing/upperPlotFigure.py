from PySide import QtCore
from matplotlib.figure import Figure
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.ticker as ticker
import thread
import threading

class fig(Figure):
    
    def __init__(self):
        super(fig,self).__init__()
        self.signal = freshSignal()
        self.dotsInScreen = 2000
        self.secondsInScreen = 20
        
    def mediaTimeChanged(self,time):
        self.currentTime_ms = int(time)
        self.fresh()
        self.signal.freshScreenTime.emit(time)
#         pass
    
    def fresh(self):
        
#        print 'fresh'
        if not hasattr(self, 'ax'):
            return
        if hasattr(self, 'pressX') and not self.pressX==None:
            self.currentTime_ms = self.media.currentTime ()
#        
        frameNow = self.currentTime_ms*self.framerate/1000
        framesInScreen = self.secondsInScreen*self.framerate
#        totalFrame = self.media.totalTime()*self.framerate/1000
        
#         print 'zipRate=', self.zipRate
        
        dotNow = frameNow/self.zipRate
        self.signal.freshLowerPlotCurrentTime.emit(frameNow)
         
        if dotNow >= self.leftDot + self.dotsInScreen*3/2 or dotNow <= self.leftDot - self.dotsInScreen/2:
            print 'or'
            print 'self.leftdot=',self.leftDot
            print 'dotNow=',dotNow
            numberOfScreens = (dotNow-self.dotsInScreen/2) // self.dotsInScreen
            self.leftDot = numberOfScreens * self.dotsInScreen
            npSlice = np.arange(self.leftDot, self.leftDot+self.dotsInScreen)
            self.plotFunc(npSlice)
            self.clearAxes()
            
        if self.leftDot + self.dotsInScreen*3/2 > dotNow > self.leftDot + self.dotsInScreen/2:
            print 'draw > > '
            npSlice = np.arange(self.leftDot + self.dotsInScreen, self.leftDot+2*self.dotsInScreen)
            self.plotFunc(npSlice)
            self.clearAxes()
            self.leftDot += self.dotsInScreen
            
            
        self.ax.set_xlim(dotNow-self.dotsInScreen/2,dotNow+self.dotsInScreen/2)  
        self.vline.set_xdata(dotNow)
        
        self.signal.freshLowerPlotPanLeftAndWidth.emit(frameNow-framesInScreen/2,frameNow+framesInScreen/2)
                
        self.canvas.draw()
        
    def drawIgniteLines(self, igniteTimeList):
        print 'drawIgniteLines'
        if not hasattr(self, 'ax'):
            return
        for i in xrange(2,len(self.ax.lines)):
            del self.ax.lines[i]
        for igniteTime in  igniteTimeList:
            if self.currentTime_ms/1000-self.secondsInScreen/2<igniteTime and \
                    igniteTime<self.currentTime_ms/1000+self.secondsInScreen/2:
                currentDot = igniteTime*self.framerate/self.zipRate
                self.ax.axvline(x=currentDot,color='#0249ee',zorder=4)
        self.canvas.draw()
        
    def drawInit(self,dataDict):
        self.clf()
        self.media = dataDict['media']
        self.waveData = dataDict['data']
        self.framerate = dataDict['framerate']
        self.zipRate = int(self.secondsInScreen*self.framerate/self.dotsInScreen)
        self.plotDataList = []
        self.getAllPlotData(self.zipRate)
        if hasattr(self, 'ax'):
            self.ax.clear()
        
        self.ax = self.add_axes([0.1,0.1,0.8,0.8])
        self.ax.axhline(y=0,color='0.8',zorder=2)
        self.vline = self.ax.axvline(x=0,color='red',zorder=3)
        
        self.leftDot = 0
        self.npSlice = [0]
        npSlice = np.arange(self.leftDot, self.leftDot+self.dotsInScreen)
        self.plotFunc(npSlice)
        self.mediaTimeChanged(0)
        
    def plotFunc(self,npSlice):
        
        if npSlice[0] < 0:
            return
        if npSlice[0] > self.waveDataLength:
            return
        elif npSlice[-1] > self.waveDataLength:
            npSlice = npSlice[0:self.waveDataLength-npSlice[0]]
            
        plotDataSliceDict = self.getSlicePlotData(npSlice)
        ymax = plotDataSliceDict['y_max']
        ymin = plotDataSliceDict['y_min']
                    
        fillPlot = self.ax.fill_between(npSlice, ymax, y2=ymin , color='c', zorder=0)
        self.plotDataList.append(fillPlot)
        
    def clearAxes(self):
        length = len(self.plotDataList)
        if length > 2:
            for i in xrange(length-3):
                self.plotDataList[i].remove()
                self.plotDataList.pop(i)
    
    def getAllPlotData(self, zipRate):
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
            self.waveDataLength = numchunks
        else:
            dataLength = len(waveData)
            chunksize = zipRate
            numchunks = dataLength // chunksize  
            team_1 = waveData[:chunksize*numchunks].reshape((-1, chunksize)) 
            max_1 = team_1.max(axis=1)
            min_1 = team_1.min(axis=1)
            mean_1 = team_1.mean(axis=1)
            plotDataDict = dict(y_max=max_1, y_min=min_1, y_mean=mean_1)
            self.waveDataLength = numchunks
        self.plotDataAllDict = plotDataDict
    
    def getSlicePlotData(self,npSlice):
        ymaxSlice = self.plotDataAllDict['y_max'][npSlice]
        yminSlice = self.plotDataAllDict['y_min'][npSlice]
        ymeanSlice = self.plotDataAllDict['y_mean'][npSlice]
        if self.plotDataAllDict.has_key('y_mean_2'):
            ymean2Slice = self.plotDataAllDict['y_mean_2'][npSlice]
            plotDataSliceDict = dict(y_max=ymaxSlice, y_min=yminSlice, y_mean=ymeanSlice, y_mean_2=ymean2Slice)
        else:
            plotDataSliceDict = dict(y_max=ymaxSlice, y_min=yminSlice, y_mean=ymeanSlice)
            
        return plotDataSliceDict
    
    def zoomIn(self):
        self.secondsInScreen /= 2
        self.zipRate = int(self.secondsInScreen*self.framerate/self.dotsInScreen)
        if self.zipRate == 0:
            return
        self.plotDataList = []
        self.getAllPlotData(self.zipRate)
        self.currentTime_ms = self.media.currentTime ()
        self.fresh()
        
    def zoomOut(self):
        self.secondsInScreen *= 2
        self.zipRate = int(self.secondsInScreen*self.framerate/self.dotsInScreen)
        self.plotDataList = []
        self.getAllPlotData(self.zipRate)
        self.currentTime_ms = self.media.currentTime ()
        self.fresh()
        
        
        
    def freshFromLowerPlot(self,dx):
#        self.currentTime_ms += dx*1000/self.framerate
#        self.fresh()
        pass 
    
    def getScreenTime(self):
        leftBorderTime = self.currentTime_ms-self.secondsInScreen*1000/2
        rightBorderTime = self.currentTime_ms+self.secondsInScreen*1000/2
        return (leftBorderTime, rightBorderTime)

class freshSignal(QtCore.QObject):
    freshLowerPlotPanLeftAndWidth = QtCore.Signal(int, int)
    freshLowerPlotCurrentTime = QtCore.Signal(int)
    freshTimeNowLabel = QtCore.Signal(str)
    freshMusicTotalTimeLabel = QtCore.Signal(str)
    freshVisionTimeLengthLabel = QtCore.Signal(str)
    freshScreenTime = QtCore.Signal(int)
    
def main():
    import plotAndPlay
    from PySide import QtGui
    import sys
    app = QtGui.QApplication(sys.argv)
    playAndPlot = plotAndPlay.playAndPlotWidget()
    playAndPlot.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    from waveModule import main
    main()
