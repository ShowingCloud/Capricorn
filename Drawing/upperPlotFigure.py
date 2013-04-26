<<<<<<< HEAD
#coding=utf-8
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
        
        
    def getBombMediaAudioOutput(self):
        return self.mo.getBombMediaAudioOutput()
    
    def mediaTimeChanged(self,time):
        self.currentTime_ms = int(time)
#        print 'mediaTimeChanged time =',time
        self.fresh()
        self.signal.freshScreenTime.emit(time)
        
    def fresh(self):
        
        print 'fresh Start-----------'
        if not hasattr(self, 'ax'):
            return
            
        frameNow = self.currentTime_ms*self.framerate/1000
                
        dotNow = frameNow/self.zipRate  
        self.signal.freshLowerPlotCurrentTime.emit(frameNow)
        
        if dotNow >= self.leftDot + self.dotsInScreen*3/2 or dotNow <= self.leftDot - self.dotsInScreen/2:
            numberOfScreens = (dotNow-self.dotsInScreen/2) // self.dotsInScreen
            self.leftDot = numberOfScreens * self.dotsInScreen
            print 'leftDot=',self.leftDot
            print 'self.dotsInScreen=',self.dotsInScreen
            npSlice = np.arange(self.leftDot, self.leftDot+self.dotsInScreen)
            print 'npSlice[0]=',npSlice[0]
            print 'npSlice[-1]=',npSlice[-1]
            print 'npSlice.size=',npSlice.size
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
                self.signal.currentFireworks.emit(self.igniteDataList[index].scriptUUID)
                break
            
#        print '--------------'
#        print 'dotNow',dotNow
#        print 'self.dotsInScreen',self.dotsInScreen
#        print 'dotNow-self.dotsInScreen/2',dotNow-self.dotsInScreen/2
#        print 'dotNow+self.dotsInScreen/2',dotNow+self.dotsInScreen/2
#        print '--------------'
        
        self.ax.set_xlim(dotNow-self.dotsInScreen/2,dotNow+self.dotsInScreen/2) 
        self.vline.set_xdata(dotNow)
        framesInScreen = self.secondsInScreen*self.framerate
        self.signal.freshLowerPlotPanLeftAndWidth.emit(frameNow-framesInScreen/2,frameNow+framesInScreen/2)
        self.canvas.draw()
        print 'fresh over-----------'
        
    def setIgniteList(self,list):
        self.igniteDataList = list
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
        print 'length=',len(self.igniteDataList)
        for line in self.igniteDataList:
            xDot = line.itime*self.framerate/self.zipRate
#            print '------------'
#            print 'line.itime',line.itime
#            print 'self.framerate',self.framerate
#            print 'self.zipRate=',self.zipRate
#             print 'xDot',xDot
#             print 'xDot time',line.itime
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
        print 'plotFunc'
        if npSlice[0] > self.waveDataLength or npSlice[-1] < 0:
            return
        if npSlice[0] < 0:
            npSlice = np.array(range(0,npSlice[-1]))
#        print 'npSlice[0]=',npSlice[0]
#        print 'npSlice[-1]=',npSlice[-1]
#        print 'npSlice.size=',npSlice.size
        if npSlice[-1] > self.waveDataLength:
#            print 'self.waveDataLength=',self.waveDataLength
#            print '111 npSlice.size=',npSlice.size
#            print 'npSlice[0]=',npSlice[0]
#            print 'npSlice[-1]=',npSlice[-1]
#            print '-----'
            npSlice = np.arange(npSlice[0],self.waveDataLength)
#            print '111 npSlice.size=',npSlice.size
#            print 'npSlice[0]=',npSlice[0]
#            print 'npSlice[-1]=',npSlice[-1]
        if npSlice.size ==0:
            return
            
        plotDataSliceDict = self.getSlicePlotData(npSlice)
        ymean = plotDataSliceDict['y_mean']
        if isinstance(self.waveData, list):
            ymean2 = plotDataSliceDict['y_mean_2']
            b = zip(npSlice,npSlice)
            npSlice = np.array([i[j] for i in b  for j in xrange(2)])
            line1, line2 = self.ax.plot(npSlice,ymean,'#4F4F4F',npSlice,ymean2,'#4F4F4F',zorder=1)
            self.lineDataList.append(line1)
            self.lineDataList2.append(line2)
            
        else:
            b = zip(npSlice,npSlice)
            npSlice = np.array([i[j] for i in b  for j in xrange(2)])
#            ymean = ymean[npSlice[]]
            print 'npSlice size',npSlice.size
            print 'ymean size',ymean.size
            line,  = self.ax.plot(npSlice,ymean,'#4F4F4F',zorder=1)
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
        print 'self.waveDataLength',self.waveDataLength
        self.plotDataAllDict = plotDataDict
    
    def getSlicePlotData(self,npSlice):
#        print '------------'
#        print 'npSlice[0]=',npSlice[0]
#        print 'npSlice[0]*2=',npSlice[0]*2
#        print 'npSlice[-1]=',npSlice[-1]
#        print 'npSlice[-1]*2+2=',npSlice[-1]*2+2
#        print 'npSlice[-1]*2+2-npSlice[0]*2=',npSlice[-1]*2+2-npSlice[0]*2
#        print '------------'
        ymeanSlice = self.plotDataAllDict['y_mean'][npSlice[0]*2:npSlice[-1]*2+2]
        print self.plotDataAllDict['y_mean'].size
        print self.plotDataAllDict['y_mean'][npSlice[0]*2]
        print self.plotDataAllDict['y_mean'][npSlice[-1]*2+1]
#        print '---'
#        print 'getSlicePlotData npSlice.size',npSlice.size
#        print 'getSlicePlotData npSlice.size',ymeanSlice.size
        if isinstance(self.waveData, list):
            ymeanSlice2 = self.plotDataAllDict['y_mean_2'][npSlice[0]*2:npSlice[-1]*2+2]
            plotDataSliceDict = dict(y_mean=ymeanSlice, y_mean_2=ymeanSlice2)
        else:
            plotDataSliceDict = dict(y_mean=ymeanSlice)
#            print 'getSlicePlotData npSlice.size',npSlice.size
#            print 'getSlicePlotData npSlice.size',ymeanSlice.size
        return plotDataSliceDict
    
    #放大
    def zoomIn(self):
        print '-----------------'
        print 'zoomIn'
        secondsInScreen =  self.secondsInScreen / 2
        zipRate = self.zipRate / 2
        if zipRate == 0:
            return
        else:
            self.secondsInScreen = secondsInScreen
            self.zipRate = zipRate
            
        self.getAllPlotData(self.zipRate)
        self.currentTime_ms = self.media.currentTime()
        print 'self.currentTime_ms',self.currentTime_ms
        dotNow = self.currentTime_ms*self.framerate/1000/self.zipRate
        numberOfScreens = (dotNow-self.dotsInScreen/2) // self.dotsInScreen
        self.leftDot = numberOfScreens * self.dotsInScreen
        npSlice = np.arange(self.leftDot, self.leftDot+2*self.dotsInScreen+1)
#        print 'self.leftDot',self.leftDot
#        print 'dotsInScreen',self.dotsInScreen
#        print 'dotNow',dotNow
#        print 'dotNow time',self.currentTime_ms/1000
#        print 'dotNow-self.dotsInScreen/2',dotNow-self.dotsInScreen/2
#        print 'dotNow+self.dotsInScreen/2',dotNow+self.dotsInScreen/2
        self.clearAxes()
        self.plotFunc(npSlice)
        self.ax.set_xlim(dotNow-self.dotsInScreen/2,dotNow+self.dotsInScreen/2)
        self.vline.set_xdata(dotNow)
        self.canvas.draw()
        frameNow = self.currentTime_ms*self.framerate/1000
        framesInScreen = self.secondsInScreen*self.framerate
        self.signal.freshLowerPlotPanLeftAndWidth.emit(frameNow-framesInScreen/2,frameNow+framesInScreen/2)
        
    #缩小
    def zoomOut(self): 
        print '-----------------'
        print 'zoomOut'
        secondsInScreen =  self.secondsInScreen * 2
        if secondsInScreen > 60*60*2:
            return
        self.secondsInScreen = secondsInScreen
        self.zipRate = self.zipRate * 2
        self.getAllPlotData(self.zipRate)
        self.currentTime_ms = self.media.currentTime ()
        dotNow = self.currentTime_ms*self.framerate/1000/self.zipRate    
        numberOfScreens = (dotNow-self.dotsInScreen/2) // self.dotsInScreen
        self.leftDot = numberOfScreens * self.dotsInScreen
        print 'self.leftDot',self.leftDot
        print 'dotsInScreen',self.dotsInScreen
        print 'dotNow',dotNow
        print 'dotNow time',self.currentTime_ms/1000
        npSlice = np.arange(self.leftDot, self.leftDot+2*self.dotsInScreen+1)
        self.clearAxes()
        self.plotFunc(npSlice)
        self.ax.set_xlim(dotNow-self.dotsInScreen/2,dotNow+self.dotsInScreen/2)
        self.vline.set_xdata(dotNow)
        self.canvas.draw()
        frameNow = self.currentTime_ms*self.framerate/1000
        framesInScreen = self.secondsInScreen*self.framerate
        self.signal.freshLowerPlotPanLeftAndWidth.emit(frameNow-framesInScreen/2,frameNow+framesInScreen/2)
        
    def toNextScreen(self):
        self.currentTime_ms += self.secondsInScreen*1000
        if self.currentTime_ms > self.media.totalTime():
            self.currentTime_ms = self.media.totalTime()
        self.mediaTimeChanged(self.currentTime_ms)
        
    def toPreviousScreen(self):
#        print repr(self.bombMedia.state())
#        self.bombMedia.stop()
#        self.bombMedia.play()
#        print repr(self.bombMedia.state())
        
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
        self.media2 = Phonon.MediaObject(self)
        self.media2.setCurrentSource(Phonon.MediaSource())
        self.output = Phonon.AudioOutput(Phonon.MusicCategory,self)
        Phonon.createPath(self.media2, self.output)
        self.media2.setCurrentSource(Phonon.MediaSource(path))
        
    def getBombMediaAudioOutput(self):
        return self.output
       
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
    currentFireworks = QtCore.Signal(str)
        
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
=======
#coding=utf-8
from PySide import QtCore
from matplotlib.figure import Figure
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.ticker as ticker
from PySide.phonon import Phonon
import matplotlib.lines as lines

class fig(Figure):
    
    def __init__(self):
        super(fig,self).__init__()
        self.signal = freshSignal()
        #每屏画点个数固定
        self.dotsInScreen = 2000
        #初始情况下，每屏显示20秒
        self.secondsInScreen = 20
        
        self.lineDataList = []
        self.lineDataList2 = []
        self.igniteDataList = []
        self.ingiteLines = []
        #爆破单类
        self.mo = mediaObject()
        self.bombMedia = self.mo.media2
        
    def mediaTimeChanged(self,time):
        #获取当时时间
        self.currentTime_ms = int(time)
#        print 'mediaTimeChanged time =',time
        #刷新图像
        self.fresh()
        #发出刷新当时时间的信号
        self.signal.freshScreenTime.emit(time)
        
    #图像移动时动态刷新函数
    def fresh(self):
        
        if not hasattr(self, 'ax'):
            return
        
        #当前帧
        frameNow = self.currentTime_ms*self.framerate/1000
        
        #当前图像的数据点
        dotNow = frameNow/self.zipRate  
        #发送信号、刷新lower plot figure的竖直线
        self.signal.freshLowerPlotCurrentTime.emit(frameNow)
        
        #手动拖拽进度条时，画当前时间范围内的图像
        if dotNow >= self.leftDot + self.dotsInScreen*3/2 or dotNow <= self.leftDot - self.dotsInScreen/2:
            numberOfScreens = (dotNow-self.dotsInScreen/2) // self.dotsInScreen
            self.leftDot = numberOfScreens * self.dotsInScreen
            npSlice = np.arange(self.leftDot, self.leftDot+self.dotsInScreen)
            self.clearAxes()
            self.plotFunc(npSlice)
            
        #随着时间的移动，需要间隔着画新的时刻范围内的图像
        if self.leftDot + self.dotsInScreen*3/2 > dotNow > self.leftDot + self.dotsInScreen/2:
            npSlice = np.arange(self.leftDot + self.dotsInScreen, self.leftDot+2*self.dotsInScreen)
            self.clearAxes()
            self.plotFunc(npSlice)
            self.leftDot += self.dotsInScreen
        
        #扫描所有点火效果线的时间，其等于当时时间内，发出爆破音
        for index in xrange(len(self.igniteTimes)):
            #时间值转化为画图的x轴的点的值
            doti = self.igniteTimes[index]*self.framerate/self.zipRate
            if dotNow <= doti:
                self.bombOrNotList[index] = 0
            #点火时间从>dotNow状态到>=dotNow状态转变的时刻点，发出爆破音
            elif self.bombOrNotList[index] == 0:
                self.bombOrNotList[index] = 1
                self.bombMedia.stop()
                self.bombMedia.play()
                #把当前发声的点火线传给数据库
                self.signal.currentFireworks.emit(self.igniteDataList[index].scriptUUID)
                break
            
#        print '--------------'
#        print 'dotNow',dotNow
#        print 'self.dotsInScreen',self.dotsInScreen
#        print 'dotNow-self.dotsInScreen/2',dotNow-self.dotsInScreen/2
#        print 'dotNow+self.dotsInScreen/2',dotNow+self.dotsInScreen/2
#        print '--------------'
        #调整x轴上下限，使表示当时时间的竖直线停留在图像中间
        self.ax.set_xlim(dotNow-self.dotsInScreen/2,dotNow+self.dotsInScreen/2) 
        self.vline.set_xdata(dotNow)
        framesInScreen = self.secondsInScreen*self.framerate
        #发出刷新lower plot figure 矩形条的宽度的信号
        self.signal.freshLowerPlotPanLeftAndWidth.emit(frameNow-framesInScreen/2,frameNow+framesInScreen/2)
        self.canvas.draw()
    
    #获取点火数据并保存
    def setIgniteList(self,list):
        self.igniteDataList = list
        #收集所有的点火时间
        self.igniteTimes = [igniteObject.itime for igniteObject in self.igniteDataList]
        #bombOrNotList用来记录、判断每一根点火线的状态，0表示ignite此点火线的点火时间<当时时间，1则相反
        self.bombOrNotList = [1]*len(self.igniteTimes)
##(itime=itime.total_seconds(), fireName=fireName,\
##                                        fire=fire, boxID=boxID, fireWork=firework,boxUUID=boxUUID )
#        print 'igniteTimes=',self.igniteTimes
#        print 'fireName=',[igniteObject.fireName for igniteObject in self.igniteDataList]
#        print 'fire=',[igniteObject.fire for igniteObject in self.igniteDataList]
#        print 'boxID=',[igniteObject.boxID for igniteObject in self.igniteDataList]
#        print 'fireWork=',[igniteObject.fireWork for igniteObject in self.igniteDataList]
#        print 'boxUUID=',[igniteObject.boxUUID for igniteObject in self.igniteDataList]
        
    #画点火效果线
    def drawIgniteLines(self):
        length = len(self.ingiteLines)
        for i in xrange(length):
            line = self.ingiteLines.pop()
            print 'line type',type(line)
            del line
#            line.remove()
        print 'length=',len(self.igniteDataList)
        #根据点火数据生成所有的点火线类
        for line in self.igniteDataList:
            xDot = line.itime*self.framerate/self.zipRate
#            print '------------'
#            print 'line.itime',line.itime
#            print 'self.framerate',self.framerate
#            print 'self.zipRate=',self.zipRate
            print 'xDot',xDot
            print 'xDot time',line.itime
#            print '------------'
            
            #每个对象表示一根点火线
            igiteLine = IgniteLine(ax=self.ax,\
                                    x=xDot,color='#0249ee',zorder=5,\
                                    textX=xDot,\
                                    textY=self.uplimit*5/6,\
                                    label=line.fireName+'--'+str(line.boxID))
            #加入list容器中，方便以后删除
            self.ingiteLines.append(igiteLine)
        #图像刷新
        self.canvas.draw()
        
    #图像的初始化
    def drawInit(self,dataDict):
        self.clf()
        self.media = dataDict['media']
        self.waveData = dataDict['data']
        self.framerate = dataDict['framerate']
        self.zipRate = int(self.secondsInScreen*self.framerate/self.dotsInScreen)
        self.lineDataList = []
        self.lineDataList2 = []
        self.igniteTimes = []
        #取得画图需要的数据
        self.getAllPlotData(self.zipRate)
        
        if hasattr(self, 'ax'):
            self.ax.clear()
            
        #得到画图所需的 axes
        self.ax = self.add_axes([0.1,0.1,0.8,0.8])
        self.ax.axhline(y=0,color='0.8',zorder=2)
        self.vline = self.ax.axvline(x=0,color='red',zorder=3)
        #设定边界
        self.ax.set_ylim(self.downlimit,self.uplimit)
        
        #self.leftDot从0开始，以self.dotsInScreen的间隔递增  
        self.leftDot = 0
        self.npSlice = [0]
        #初始情况下，画第一屏
        npSlice = np.arange(self.leftDot, self.leftDot+self.dotsInScreen)
        self.plotFunc(npSlice)
        self.mediaTimeChanged(0)
        #画效果线
        self.drawIgniteLines()
        
        #x轴，下x轴有刻度，上x轴无刻度；y轴，左y轴有刻度，右y轴无刻度
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
            #将已画过的线保存到list对象中，供以后删除
            self.lineDataList.append(line1)
            self.lineDataList2.append(line2)
            
        else:
            b = zip(npSlice,npSlice)
            npSlice = np.array([i[j] for i in b  for j in xrange(2)])
            if npSlice.size != ymean.size:
                return
            line,  = self.ax.plot(npSlice,ymean,'pink',zorder=1)
            #将已画过的线保存到list对象中，供以后删除
            self.lineDataList.append(line)
            
        self.drawIgniteLines()
        
        #画x轴上的刻度标注
        majorLocator   = MultipleLocator(self.dotsInScreen/20)
        def format_time(x, pos=None):
            if x < 0:
                return ''
            y = x*self.zipRate/self.framerate
            #标注格式：‘02：32.1’，表示 2min,32.1s
            tupleTime = divmod(y, 60)
            return '%d:%04.1f'%(tupleTime[0],tupleTime[1])
        self.ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_time))
        self.ax.xaxis.set_major_locator(majorLocator)
        
    #随着屏幕的滚动，定期清除不再显示在屏幕上的线
    def clearAxes(self):
        length = len(self.lineDataList)
        if length > 1:
            for i in xrange(length-1):
                line = self.lineDataList.pop(0)
                print 'type line=',type(line)
                print 'repr line',repr(line)
                del line
#                self.ax.lines.remove(line)
                
            if isinstance(self.waveData, list):
                for i in xrange(length-1):
                    line = self.lineDataList2.pop(0)
                    del line
#                    self.ax.lines.remove(line)
                         
    #将解析得到的数据  self.waveData 以zipRate的频率采样                 
    def getAllPlotData(self, zipRate):
        waveData = self.waveData
        #双声道
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
            
            #获取图像y轴的上、下限
            uplimit = max(max(mean_1),max(mean_2))
            downlimit = min(min(mean_1),min(mean_2))
            if uplimit+downlimit>0:
                self.uplimit = uplimit
                self.downlimit = -uplimit
            else:
                self.uplimit = -downlimit
                self.downlimit = downlimit
        #单声道   
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
            
            #获取图像y轴的上、下限
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
    
    #获取待画的图像所需的数据，npSlice表示总的数据中的某一部分
    def getSlicePlotData(self,npSlice):
        
        ymeanSlice = self.plotDataAllDict['y_mean'][npSlice[0]*2:npSlice[-1]*2+2]
        #双声道
        if isinstance(self.waveData, list):
            ymeanSlice2 = self.plotDataAllDict['y_mean_2'][npSlice[0]*2:npSlice[-1]*2+2]
            plotDataSliceDict = dict(y_mean=ymeanSlice, y_mean_2=ymeanSlice2)
        #单声道
        else:
            plotDataSliceDict = dict(y_mean=ymeanSlice)
        return plotDataSliceDict
    
    #放大
    def zoomIn(self):
        print '-----------------'
        print 'zoomIn'
        secondsInScreen =  self.secondsInScreen / 2
        zipRate = self.zipRate / 2
        if zipRate == 0:
            return
        else:
            self.secondsInScreen = secondsInScreen
            self.zipRate = zipRate
            
        self.getAllPlotData(self.zipRate)
        dotNow = self.currentTime_ms*self.framerate/1000/self.zipRate    
        self.currentTime_ms = self.media.totalTime()
        self.leftDot = ((dotNow-self.dotsInScreen/2) // self.dotsInScreen) * self.dotsInScreen
        self.fresh()
#        self.currentTime_ms = self.media.currentTime()
#        print 'self.currentTime_ms',self.currentTime_ms
#        dotNow = self.currentTime_ms*self.framerate/1000/self.zipRate
#        numberOfScreens = (dotNow-self.dotsInScreen/2) // self.dotsInScreen
#        self.leftDot = numberOfScreens * self.dotsInScreen
#        npSlice = np.arange(self.leftDot, self.leftDot+2*self.dotsInScreen)
#        print 'self.leftDot',self.leftDot
#        print 'dotsInScreen',self.dotsInScreen
#        print 'dotNow',dotNow
#        print 'dotNow time',self.currentTime_ms/1000
#        print 'dotNow-self.dotsInScreen/2',dotNow-self.dotsInScreen/2
#        print 'dotNow+self.dotsInScreen/2',dotNow+self.dotsInScreen/2
#        self.clearAxes()
#        self.plotFunc(npSlice)
#        self.ax.set_xlim(dotNow-self.dotsInScreen/2,dotNow+self.dotsInScreen/2)
#        self.vline.set_xdata(dotNow)
#        self.canvas.draw()
        
    #缩小
    def zoomOut(self):
         
        print '-----------------'
        print 'zoomOut'
        secondsInScreen =  self.secondsInScreen * 2
        if secondsInScreen > 60*60*2:
            return
        self.secondsInScreen = secondsInScreen
        self.zipRate = self.zipRate * 2
        self.getAllPlotData(self.zipRate)
#        self.ax.clear()
        dotNow = self.currentTime_ms*self.framerate/1000/self.zipRate
        self.currentTime_ms = self.media.totalTime()
        self.leftDot = ((dotNow-self.dotsInScreen/2) // self.dotsInScreen) * self.dotsInScreen
        self.fresh()
        
#        self.leftDot = 0
#        self.npSlice = [0]
#        #初始情况下，画第一屏
#        npSlice = np.arange(self.leftDot, self.leftDot+self.dotsInScreen)
#        self.plotFunc(npSlice)
#        self.mediaTimeChanged(0)
#        #画效果线
#        self.drawIgniteLines()
        
        
#        self.currentTime_ms = self.media.currentTime ()
#        dotNow = self.currentTime_ms*self.framerate/1000/self.zipRate    
#        numberOfScreens = (dotNow-self.dotsInScreen/2) // self.dotsInScreen
#        self.leftDot = numberOfScreens * self.dotsInScreen
#        print 'self.leftDot',self.leftDot
#        print 'dotsInScreen',self.dotsInScreen
#        print 'dotNow',dotNow
#        print 'dotNow time',self.currentTime_ms/1000
#        npSlice = np.arange(self.leftDot, self.leftDot+2*self.dotsInScreen)
#        self.clearAxes()
#        self.plotFunc(npSlice)
#        self.ax.set_xlim(dotNow-self.dotsInScreen/2,dotNow+self.dotsInScreen/2)
#        self.vline.set_xdata(dotNow)
#        self.canvas.draw()
      
    #当前时刻后移一屏  
    def toNextScreen(self):
        self.currentTime_ms += self.secondsInScreen*1000
        if self.currentTime_ms > self.media.totalTime():
            self.currentTime_ms = self.media.totalTime()
        self.mediaTimeChanged(self.currentTime_ms)
    
    #当前时刻前移一屏
    def toPreviousScreen(self):        
        self.currentTime_ms -= self.secondsInScreen*1000
        if self.currentTime_ms<0:
            self.currentTime_ms = 0
        self.mediaTimeChanged(self.currentTime_ms)

#发爆破音的类          
class mediaObject(QtCore.QObject):
    def __init__(self):
        super(mediaObject,self).__init__()
        
        #获取音乐文件的路径
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
        #播放音乐的对象
        self.media2 = Phonon.MediaObject(self)
        self.media2.setCurrentSource(Phonon.MediaSource())
        output = Phonon.AudioOutput(Phonon.MusicCategory,self)
        Phonon.createPath(self.media2, output)
        #选定路径
        self.media2.setCurrentSource(Phonon.MediaSource(path))

#画竖直线类    
class IgniteLine():
    def __init__(self,ax=None,x=None,color=None,zorder=None, textX=None,textY=None,label=None):
        #用于画图的axes
        self.ax = ax
        #画竖线
        self.line = self.ax.axvline(x=x,color=color,zorder=zorder)
        #文字
        self.text = None
        if not label.endswith('None'):
            self.text = self.ax.text(textX, textY, label,horizontalalignment='center',fontsize=10)
    #从图像中删除该IgniteLine
    def remove(self):
        print 'self.line type',type(self.line),repr(self.line)
#        self.line.remove()
        del self.line
        if not self.text==None:
            self.text.remove()
        
#信号类
class freshSignal(QtCore.QObject):
    #刷新lowerPlot 图像的中矩形条宽度和高度
    freshLowerPlotPanLeftAndWidth = QtCore.Signal(int, int)
    #刷新lowerPlot 图像的中表现current time 的垂直线
    freshLowerPlotCurrentTime = QtCore.Signal(int)
    #刷新现在时间供数据库读取
    freshScreenTime = QtCore.Signal(int)
    #提供当前效果线的信息
    currentFireworks = QtCore.Signal(str)
        
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
>>>>>>> aba9b2b1c03e42d225268c3c482cc1480acea3ce
