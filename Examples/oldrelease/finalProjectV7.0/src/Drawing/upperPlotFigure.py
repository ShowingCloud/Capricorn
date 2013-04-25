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
        self.signal.freshScreenTime.emit(time)
#        pass
    
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
        
#        print 'lines=', len(self.ax.lines)
        
        dotNow = frameNow/self.zipRate
        self.signal.freshLowerPlotCurrentTime.emit(frameNow)
         
#        print 'screenTime',self.getScreenTime()
        if dotNow >= self.leftDot + self.dotsInScreen*3/2 or dotNow <= self.leftDot - self.dotsInScreen/2:
            numberOfScreens = (dotNow-self.dotsInScreen/2) // self.dotsInScreen
            self.leftDot = numberOfScreens * self.dotsInScreen
            npSlice = np.arange(self.leftDot, self.leftDot+self.dotsInScreen)
            self.plotFunc(npSlice)            
        if self.leftDot + self.dotsInScreen*3/2 > dotNow > self.leftDot + self.dotsInScreen/2:
            npSlice = np.arange(self.leftDot + self.dotsInScreen, self.leftDot+2*self.dotsInScreen)
            self.plotFunc(npSlice)
            self.drawIgniteLines()
            self.leftDot += self.dotsInScreen
            
            
        self.ax.set_xlim(dotNow-self.dotsInScreen/2,dotNow+self.dotsInScreen/2)  
        self.vline.set_xdata(dotNow)
        
        self.signal.freshLowerPlotPanLeftAndWidth.emit(frameNow-framesInScreen/2,frameNow+framesInScreen/2)
                
        self.canvas.draw()


    def setIgniteTimes(self,times):
        self.igniteTimes = times
        
    def drawIgniteLines(self):
        print 'drawIgniteLines'
        igniteTimeList = self.igniteTimes
        if not hasattr(self, 'ax'):
            return
##        for i in xrange(2,len(self.ax.lines)):
##            del self.ax.lines[i]
#        print 'igniteTimeList=',igniteTimeList
#        length = len(self.igniteTimeLines)
        for line in self.igniteTimeLines:
            line.remove()
            self.igniteTimeLines.remove(line)
#            print 'igniteTimeLines=',self.igniteTimeLines
#            print 'i=',i
#            print self.igniteTimeLines[i]
#            self.igniteTimeLines.pop(i)
#for i in xrange(length-1):
#    self.lineDataList[i].remove()
#    self.lineDataList.pop(i)
                    
#        for line in self.igniteTimeLines:
#            self.igniteTimeLines.remove(line)
            
            
        for igniteTime in  igniteTimeList:
            igniteDot = igniteTime*self.framerate/self.zipRate
#            
#            print 'igniteTime=',igniteTime
#            print 'igniteDot=',igniteDot
#            print 'leftDot=',self.leftDot
#            print 'leftDot 2=',self.leftDot + 2*self.dotsInScreen
            if self.leftDot - self.dotsInScreen <= igniteDot < self.leftDot + self.dotsInScreen:
                line = self.ax.axvline(x=igniteDot,color='#0249ee',zorder=4)
                self.igniteTimeLines.append(line)
#                
        self.canvas.draw()
                
    def drawInit(self,dataDict):
        self.clf()
        self.media = dataDict['media']
        self.waveData = dataDict['data']
        self.framerate = dataDict['framerate']
        self.zipRate = int(self.secondsInScreen*self.framerate/self.dotsInScreen)
        self.plotDataList = []
        self.lineDataList = []
        self.igniteTimes = []
        self.igniteTimeLines = []
        self.getAllPlotData(self.zipRate)
        if hasattr(self, 'ax'):
            self.ax.clear()
        
        self.ax = self.add_axes([0.04,0.05,0.96,0.95])
        self.ax.axhline(y=0,color='0.8',zorder=2)
        self.vline = self.ax.axvline(x=0,color='red',zorder=3)
        self.ax.set_axis_on()
        self.set_facecolor("#ffffff")
        
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
            
        self.clearAxes() 
        plotDataSliceDict = self.getSlicePlotData(npSlice)
        ymax = plotDataSliceDict['y_max']
        ymin = plotDataSliceDict['y_min']
        ymean = plotDataSliceDict['y_mean']
        if isinstance(self.waveData, list):
            ymean2 = plotDataSliceDict['y_mean_2']
            line1, line2 = self.ax.plot(npSlice,ymean,'pink',npSlice,ymean2,'y',zorder=1)
            self.lineDataList.append((line1,line2))
        else:
            line,  = self.ax.plot(npSlice,ymean,'pink',zorder=1)
            self.lineDataList.append(line)
        fillPlot = self.ax.fill_between(npSlice, ymax, y2=ymin , color='c', zorder=0)
        self.plotDataList.append(fillPlot)
#        self.autofmt_xdate()
#        self.ax.xaxis.set_ticks_position('top')
        
        majorLocator   = MultipleLocator(self.dotsInScreen/20)
#        np.clip()
#autofmt_xdate()

        def format_time(x, pos=None):
#            print 'format_date,x=',x
            if x < 0:
                return ''
            y = x*self.zipRate/self.framerate
            tupleTime = divmod(y, 60)
#            print 'tupleTime[0]=',tupleTime[0]
#            print 'tupleTime[1]=',tupleTime[1]
            return '%d:%04.1f'%(tupleTime[0],tupleTime[1])
        self.ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_time))
        self.ax.xaxis.set_major_locator(majorLocator)
        
    def clearAxes(self):
        length = len(self.plotDataList)
        if length > 1:
            for i in xrange(length-1):
                self.plotDataList[i].remove()
                self.plotDataList.pop(i)
                
            if isinstance(self.waveData, list):
                for i in xrange(length-1):
                    self.lineDataList[i][0].remove()
                    self.lineDataList[i][1].remove()
                    self.lineDataList.pop(i)
            else:
                for i in xrange(length-1):
                    self.lineDataList[i].remove()
                    self.lineDataList.pop(i)
                    
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
        
    def toNextScreen(self):
        self.currentTime_ms += self.secondsInScreen*1000
        if self.currentTime_ms > self.media.totalTime():
            self.currentTime_ms = self.media.totalTime()
        self.mediaTimeChanged(self.currentTime_ms)
        
        
    def toPreviousScreen(self):
        self.currentTime_ms -= self.secondsInScreen*1000
        if self.currentTime_ms<0:
            self.currentTime_ms = 0
        self.mediaTimeChanged(self.currentTime_ms)
        
        
    def freshFromLowerPlot(self,dx):
#        self.currentTime_ms += dx*1000/self.framerate
#        self.fresh()
        pass 
    
#    def getScreenTime(self):
#        leftBorderTime = self.currentTime_ms-self.secondsInScreen*1000/2
#        rightBorderTime = self.currentTime_ms+self.secondsInScreen*1000/2
#        return (leftBorderTime, rightBorderTime)

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
