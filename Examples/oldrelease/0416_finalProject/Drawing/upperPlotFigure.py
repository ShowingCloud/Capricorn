from PySide import QtCore
from matplotlib.figure import Figure
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.ticker as ticker
import thread
import threading
import matplotlib.ticker as ticker
from PySide.phonon import Phonon


class fig(Figure):
    
    def __init__(self):
        super(fig,self).__init__()
        self.signal = freshSignal()
        self.dotsInScreen = 2000
        self.secondsInScreen = 20
        
        self.lineDataList = []
        self.lineDataList2 = []
        self.igniteTimeLines = []
        
        self.bombMedia = Phonon.MediaObject()
        self.bombMedia.setCurrentSource(Phonon.MediaSource())
        output = Phonon.AudioOutput(Phonon.MusicCategory)
        Phonon.createPath(self.bombMedia, output)
        path = 'C:/Users/pyroshow/Documents/GitHub/Capricorn/src/WaveModule/0416_finalProject/2633_0.3s.wav'
#        self.bombMedia.stateChanged.connect(self.stateChanged)
        self.bombMedia.setCurrentSource(Phonon.MediaSource(path))
        
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
        print 'dotNow=',dotNow
         
        
#        print 'screenTime',self.getScreenTime()
        if dotNow >= self.leftDot + self.dotsInScreen*3/2 or dotNow <= self.leftDot - self.dotsInScreen/2:
            print 'or'
            print 'self.leftdot=',self.leftDot
            print 'dotNow=',dotNow
            numberOfScreens = (dotNow-self.dotsInScreen/2) // self.dotsInScreen
            self.leftDot = numberOfScreens * self.dotsInScreen
            npSlice = np.arange(self.leftDot, self.leftDot+self.dotsInScreen)
            self.clearAxes()
            self.plotFunc(npSlice)

            
        if self.leftDot + self.dotsInScreen*3/2 > dotNow > self.leftDot + self.dotsInScreen/2:
            print 'draw > > '
            npSlice = np.arange(self.leftDot + self.dotsInScreen, self.leftDot+2*self.dotsInScreen)
            self.clearAxes()
            self.plotFunc(npSlice)
            self.leftDot += self.dotsInScreen
            
        for timeOne in self.igniteTimes:
            doti = timeOne*self.framerate/self.zipRate
            if dotNow <= doti and dotNow + 10 >= doti:
                self.bombMedia.play()
                
       
        self.ax.set_xlim(dotNow-self.dotsInScreen/2,dotNow+self.dotsInScreen/2) 
        self.vline.set_xdata(dotNow)
        
        self.signal.freshLowerPlotPanLeftAndWidth.emit(frameNow-framesInScreen/2,frameNow+framesInScreen/2)
        self.drawIgniteLines()
#        self.canvas.draw()
        
    def setIgniteTimes(self,times):
        self.igniteTimes = times
        
    def drawIgniteLines(self):

        
        igniteTimes = self.igniteTimes
        if not hasattr(self, 'ax'):
            return
        for line in self.igniteTimeLines:
#            print 'line=',repr(line),dir(line)
            self.ax.lines.remove(line)
        self.igniteTimeLines = []
#        print '-------------------'
#        print 'self.igniteTimes =',self.igniteTimes
#        print 'self.igniteTimeLines =',self.igniteTimeLines
        
        for igniteTime in  igniteTimes:
            igniteDot = igniteTime*self.framerate/self.zipRate
            if self.leftDot - self.dotsInScreen <= igniteDot < self.leftDot + self.dotsInScreen:
                print 'igniteDot=',igniteDot
                line = self.ax.axvline(x=igniteDot,color='#0249ee',zorder=5)
                self.igniteTimeLines.append(line)
        self.canvas.draw()
        
        
        frameNow = self.currentTime_ms*self.framerate/1000
        dotNow = frameNow/self.zipRate
        
#        print '------'
#        print 'dotNow=',dotNow
#        print 'dotNow-self.dotsInScreen/2=',dotNow-self.dotsInScreen/2
#        print 'dotNow+self.dotsInScreen/2=',dotNow+self.dotsInScreen/2
#        print 'self.igniteTimes =',self.igniteTimes
#        print 'self.igniteTimeLines =',self.igniteTimeLines
#        print '-------------------'
        
        
    def drawInit(self,dataDict):
        self.clf()
        self.media = dataDict['media']
        self.waveData = dataDict['data']
        self.framerate = dataDict['framerate']
        self.zipRate = int(self.secondsInScreen*self.framerate/self.dotsInScreen)
        self.lineDataList = []
        self.lineDataList2 = []
        self.igniteTimeLines = []
        self.getAllPlotData(self.zipRate)
        if hasattr(self, 'ax'):
            self.ax.clear()
        
        self.ax = self.add_axes([0.0,0.1,1,0.9])
        self.ax.axhline(y=0,color='0.8',zorder=2)
        self.vline = self.ax.axvline(x=0,color='red',zorder=3)
        
        self.leftDot = 0
        self.npSlice = [0]
        npSlice = np.arange(self.leftDot, self.leftDot+self.dotsInScreen)
        self.plotFunc(npSlice)
        self.mediaTimeChanged(0)
        self.drawIgniteLines()
        
    def plotFunc(self,npSlice):
        if npSlice[0] < 0:
            return
        if npSlice[0] > self.waveDataLength:
            return
        elif npSlice[-1] > self.waveDataLength:
            npSlice = npSlice[0:self.waveDataLength-npSlice[0]]
            
        plotDataSliceDict = self.getSlicePlotData(npSlice)
        ymean = plotDataSliceDict['y_mean']
        if isinstance(self.waveData, list):
            ymean2 = plotDataSliceDict['y_mean_2']
            b = zip(npSlice,npSlice)
            npSlice = np.array([i[j] for i in b  for j in xrange(2)])
            line1, line2 = self.ax.plot(npSlice,ymean,'pink',npSlice,ymean2,'y',zorder=1)
            self.lineDataList.append(line1)
            self.lineDataList2.append(line2)
            
        else:
            b = zip(npSlice,npSlice)
            npSlice = np.array([i[j] for i in b  for j in xrange(2)])
#            print 'npSlice.size=',npSlice.size
#            print 'yean.size=',ymean.size
            line,  = self.ax.plot(npSlice,ymean,'pink',zorder=1)
            self.lineDataList.append(line)
            
        
        majorLocator   = MultipleLocator(self.dotsInScreen/20)
        def format_time(x, pos=None):
            if x < 0:
                return ''
            y = x*self.zipRate/self.framerate
            tupleTime = divmod(y, 60)
            return '%d:%04.1f'%(tupleTime[0],tupleTime[1])
        self.ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_time))
        self.ax.xaxis.set_major_locator(majorLocator)
        
                
    def clearAxes(self):
        length = len(self.lineDataList)
        if length > 1:
            for i in xrange(length-1):
                self.lineDataList[i].remove()
                self.lineDataList.pop(i)
            if isinstance(self.waveData, list):
                for i in xrange(length-1):
                    self.lineDataList2[i].remove()
                    self.lineDataList2.pop(i)
                    
                    
                        
    def getAllPlotData(self, zipRate):
        waveData = self.waveData
        if isinstance(waveData, list):
            dataOne = waveData[0]
            dataTwo = waveData[1]
            dataLength = len(dataOne)
            chunksize = zipRate
            numchunks = dataLength // chunksize
            team_1 = dataOne[:chunksize*numchunks].reshape((-1, chunksize))
            a1 = team_1.take([0],axis=1)
            b1 = []
            for i in xrange(len(a1)):
                b1.append(a1[i][0])
                b1.append(a1[i][0]*-1)
            mean_1 = np.array(b1)
            
            team_2 = dataTwo[:chunksize*numchunks].reshape((-1, chunksize))  
            a2 = team_2.take([0],axis=1)
            b2 = []
            for i in xrange(len(a2)):
                b2.append(a2[i][0])
                b2.append(a2[i][0]*-1)
            mean_2 = np.array(b2)
            plotDataDict = dict(y_mean=mean_1, y_mean_2=mean_2)
            
        else:
            dataLength = len(waveData)
            chunksize = zipRate
            numchunks = dataLength // chunksize  
            team_1 = waveData[:chunksize*numchunks].reshape((-1, chunksize)) 
            
            a = team_1.take([0],axis=1)
            b = []
            for i in xrange(len(a)):
                b.append(a[i][0])
                b.append(a[i][0]*-1)
            mean_1 = np.array(b)
            plotDataDict = dict(y_mean=mean_1)
            
        self.waveDataLength = numchunks
        self.plotDataAllDict = plotDataDict
    
    def getSlicePlotData(self,npSlice):
        
        ymeanSlice = self.plotDataAllDict['y_mean'][npSlice[0]*2:npSlice[-1]*2+2]
        if isinstance(self.waveData, list):
            ymeanSlice2 = self.plotDataAllDict['y_mean_2'][npSlice[0]*2:npSlice[-1]*2+2]
            plotDataSliceDict = dict(y_mean=ymeanSlice, y_mean_2=ymeanSlice2)
        else:
            plotDataSliceDict = dict(y_mean=ymeanSlice)
        return plotDataSliceDict
    
    def zoomIn(self):
        secondsInScreen =  self.secondsInScreen / 2
        zipRate = int(secondsInScreen*self.framerate/self.dotsInScreen)
        if zipRate == 0:
            return
        else:
            self.secondsInScreen = secondsInScreen
            self.zipRate = zipRate
        self.getAllPlotData(self.zipRate)
        self.currentTime_ms = self.media.currentTime ()
        self.fresh()
        
    def zoomOut(self):
        secondsInScreen =  self.secondsInScreen * 2
        if secondsInScreen > 60*60*2:
            return
        else:
            self.secondsInScreen = secondsInScreen
            
        self.zipRate = int(self.secondsInScreen*self.framerate/self.dotsInScreen)
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
    

            

class freshSignal(QtCore.QObject):
    freshLowerPlotPanLeftAndWidth = QtCore.Signal(int, int)
    freshLowerPlotCurrentTime = QtCore.Signal(int)
    freshTimeNowLabel = QtCore.Signal(str)
    freshMusicTotalTimeLabel = QtCore.Signal(str)
    freshVisionTimeLengthLabel = QtCore.Signal(str)
    freshScreenTime = QtCore.Signal(int)
    
    bomb = QtCore.Signal()
    
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
    
#    from Frontend.LoginShow import main
#    main()
