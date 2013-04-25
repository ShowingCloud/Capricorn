from PySide import QtCore
from matplotlib.figure import Figure
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.ticker as ticker
from PySide.phonon import Phonon
import matplotlib.text as mtext
import matplotlib.lines as lines

class fig(Figure):
    
    def __init__(self):
        super(fig,self).__init__()
        self.signal = freshSignal()
        self.dotsInScreen = 2000
        self.secondsInScreen = 20
        
        self.lineDataList = []
        self.lineDataList2 = []
        self.igniteDataList = []
        self.ingiteLines = []
        self.mo = mediaObject()
        self.bombMedia = self.mo.media2
        
    def mediaTimeChanged(self,time):
        self.currentTime_ms = int(time)
#        print 'mediaTimeChanged time =',time
        self.fresh()
        self.signal.freshScreenTime.emit(time)
        
    def fresh(self):
        
        if not hasattr(self, 'ax'):
            return
            
        frameNow = self.currentTime_ms*self.framerate/1000
                
        dotNow = frameNow/self.zipRate  
        self.signal.freshLowerPlotCurrentTime.emit(frameNow)
        
        if dotNow >= self.leftDot + self.dotsInScreen*3/2 or dotNow <= self.leftDot - self.dotsInScreen/2:
            numberOfScreens = (dotNow-self.dotsInScreen/2) // self.dotsInScreen
            self.leftDot = numberOfScreens * self.dotsInScreen
            npSlice = np.arange(self.leftDot, self.leftDot+self.dotsInScreen)
            self.clearAxes()
            self.plotFunc(npSlice)
            
        if self.leftDot + self.dotsInScreen*3/2 > dotNow > self.leftDot + self.dotsInScreen/2:
            npSlice = np.arange(self.leftDot + self.dotsInScreen, self.leftDot+2*self.dotsInScreen)
            self.clearAxes()
            self.plotFunc(npSlice)
            self.leftDot += self.dotsInScreen
        
        for index in xrange(len(self.igniteTimes)):
            doti = self.igniteTimes[index]*self.framerate/self.zipRate
            if dotNow <= doti:
                self.bombOrNotList[index] = 0
            elif self.bombOrNotList[index] == 0:
                self.bombOrNotList[index] = 1
                self.bombMedia.stop()
                self.bombMedia.play()
                break
            
#         print '--------------'
#         print 'dotNow',dotNow
#         print 'self.dotsInScreen',self.dotsInScreen
#         print 'dotNow-self.dotsInScreen/2',dotNow-self.dotsInScreen/2
#         print 'dotNow+self.dotsInScreen/2',dotNow+self.dotsInScreen/2
#         print '--------------'
        
        self.ax.set_xlim(dotNow-self.dotsInScreen/2,dotNow+self.dotsInScreen/2) 
        self.vline.set_xdata(dotNow)
        framesInScreen = self.secondsInScreen*self.framerate
        self.signal.freshLowerPlotPanLeftAndWidth.emit(frameNow-framesInScreen/2,frameNow+framesInScreen/2)
        self.canvas.draw()
    
    def setIgniteList(self,lista):
        self.igniteDataList = lista
        self.igniteTimes = [igniteObject.itime for igniteObject in self.igniteDataList]
        self.bombOrNotList = [1]*len(self.igniteTimes)
##(itime=itime.total_seconds(), fireName=fireName,\
##                                        fire=fire, boxID=boxID, fireWork=firework,boxUUID=boxUUID )
#        print 'igniteTimes=',self.igniteTimes
#        print 'fireName=',[igniteObject.fireName for igniteObject in self.igniteDataList]
#        print 'fire=',[igniteObject.fire for igniteObject in self.igniteDataList]
#        print 'boxID=',[igniteObject.boxID for igniteObject in self.igniteDataList]
#        print 'fireWork=',[igniteObject.fireWork for igniteObject in self.igniteDataList]
#        print 'boxUUID=',[igniteObject.boxUUID for igniteObject in self.igniteDataList]
        
    def drawIgniteLines(self):
        length = len(self.ingiteLines)
        for i in xrange(length):
            line = self.ingiteLines.pop()
            line.remove()
        for line in self.igniteDataList:
            xDot = line.itime*self.framerate/self.zipRate
#            print '------------'
#            print 'line.itime',line.itime
#            print 'self.framerate',self.framerate
#            print 'self.zipRate=',self.zipRate
#            print 'xDot',xDot
#            print '------------'
            
            igiteLine = IgniteLine(ax=self.ax,\
                                    x=xDot,color='#0249ee',zorder=5,\
                                    textX=xDot,\
                                    textY=self.uplimit*5/6,\
                                    label=line.fireName+'--'+str(line.boxID))
            self.ingiteLines.append(igiteLine)
        self.canvas.draw()
        
    def drawInit(self,dataDict):
        self.clf()
        self.media = dataDict['media']
        self.waveData = dataDict['data']
        self.framerate = dataDict['framerate']
        self.zipRate = int(self.secondsInScreen*self.framerate/self.dotsInScreen)
        self.lineDataList = []
        self.lineDataList2 = []
        self.igniteTimes = []
        self.getAllPlotData(self.zipRate)
        
        if hasattr(self, 'ax'):
            self.ax.clear()
        
        self.ax = self.add_axes([0.038,0.048,0.95,0.94])
        self.ax.axhline(y=0,color='0.8',zorder=2)
        self.vline = self.ax.axvline(x=0,color='red',zorder=3)
        self.ax.set_ylim(self.downlimit,self.uplimit)
                
        self.leftDot = 0
        self.npSlice = [0]
        npSlice = np.arange(self.leftDot, self.leftDot+self.dotsInScreen)
        self.plotFunc(npSlice)
        self.mediaTimeChanged(0)
        self.drawIgniteLines()
        self.ax.xaxis.set_tick_params(which='both', top=False, labeltop=False,
                                 bottom=True, labelbottom=True)
        self.ax.yaxis.set_tick_params(which='both', right=False, labeltop=False,
                                 left=True, labelbottom=True)
        
    def plotFunc(self,npSlice):
        print 'pltoFunc'
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
            line,  = self.ax.plot(npSlice,ymean,'pink',zorder=1)
            self.lineDataList.append(line)
            
        self.drawIgniteLines()
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
            
            uplimit = max(max(mean_1),max(mean_2))
            downlimit = min(min(mean_1),min(mean_2))
            if uplimit+downlimit>0:
                self.uplimit = uplimit
                self.downlimit = -uplimit
            else:
                self.uplimit = -downlimit
                self.downlimit = downlimit
                
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
            
            uplimit = max(mean_1)
            downlimit = min(mean_1)
            if uplimit+downlimit>0:
                self.uplimit = uplimit
                self.downlimit = -uplimit
            else:
                self.uplimit = -downlimit
                self.downlimit = downlimit
                
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
#        length = len(self.ingiteLines)
#        for i in xrange(length):
#            line = self.ingiteLines.pop()
#            line.remove()
#        self.canvas.draw()
        secondsInScreen =  self.secondsInScreen / 2
        zipRate = self.zipRate / 2
        if zipRate == 0:
            return
        else:
            self.secondsInScreen = secondsInScreen
            self.zipRate = zipRate
        self.getAllPlotData(self.zipRate)
        self.currentTime_ms = self.media.currentTime ()
        dotNow = self.currentTime_ms*self.framerate/1000/self.zipRate        
        numberOfScreens = (dotNow-self.dotsInScreen/2) // self.dotsInScreen
        self.leftDot = numberOfScreens * self.dotsInScreen
        self.fresh()
        
    def zoomOut(self): 
        secondsInScreen =  self.secondsInScreen * 2
        if secondsInScreen > 60*60*2:
            return
        else:
            self.secondsInScreen = secondsInScreen
            
        self.zipRate = self.zipRate * 2
        self.getAllPlotData(self.zipRate)
        self.currentTime_ms = self.media.currentTime ()
        dotNow = self.currentTime_ms*self.framerate/1000/self.zipRate        
        numberOfScreens = (dotNow-self.dotsInScreen/2) // self.dotsInScreen
        self.leftDot = numberOfScreens * self.dotsInScreen
        self.fresh()

    def toNextScreen(self):
#         print repr(self.bombMedia.state())
#         self.bombMedia.stop()
#         self.bombMedia.play()
#         print repr(self.bombMedia.state())
        self.currentTime_ms += self.secondsInScreen*1000
        if self.currentTime_ms > self.media.totalTime():
            self.currentTime_ms = self.media.totalTime()
        self.mediaTimeChanged(self.currentTime_ms)
        
    def toPreviousScreen(self):
#         print repr(self.bombMedia.state())
#         self.bombMedia.stop()
#         self.bombMedia.play()
#         print repr(self.bombMedia.state())
        
        self.currentTime_ms -= self.secondsInScreen*1000
        if self.currentTime_ms<0:
            self.currentTime_ms = 0
        self.mediaTimeChanged(self.currentTime_ms)
            
class mediaObject(QtCore.QObject):
    def __init__(self):
        super(mediaObject,self).__init__()
        import os
        import sys
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        path2 = ''
        for index in xrange(len(path)):
            if path[index]=='\\':
                path2 += '/'
            else:
                path2 += path[index]

        path = path2+'/Fire.wav'
        print 'path22222=',path
        self.media2 = Phonon.MediaObject(self)
        self.media2.setCurrentSource(Phonon.MediaSource())
        output = Phonon.AudioOutput(Phonon.MusicCategory,self)
        Phonon.createPath(self.media2, output)
        self.media2.setCurrentSource(Phonon.MediaSource(path))
       
class IgniteLine():
    def __init__(self,ax=None,x=None,color=None,zorder=None, textX=None,textY=None,label=None):
        self.ax = ax
        self.line = self.ax.axvline(x=x,color=color,zorder=zorder)
        self.text = None
        if not label.endswith('None'):
            self.text = self.ax.text(textX, textY, label,horizontalalignment='center',fontsize=10)
    def remove(self):
        self.line.remove()
        if not self.text==None:
            self.text.remove()
        
class freshSignal(QtCore.QObject):
    freshLowerPlotPanLeftAndWidth = QtCore.Signal(int, int)
    freshLowerPlotCurrentTime = QtCore.Signal(int)
    freshScreenTime = QtCore.Signal(int)
        
# def main():
#     import plotAndPlay
#     from PySide import QtGui
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     playAndPlot = plotAndPlay.playAndPlotWidget()
#     playAndPlot.show()
#     sys.exit(app.exec_())
#     
# if __name__ == "__main__":
#     from waveModule import main
#     main()
    
#    from Frontend.LoginShow import main
#    main()
