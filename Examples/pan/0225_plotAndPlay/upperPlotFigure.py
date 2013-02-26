from PySide import QtCore
from matplotlib.figure import Figure


class fig(Figure):
    def __init__(self):
        super(fig,self).__init__()
        self.x = 1000
        self.zoomWidth = 600
        self.timeInterval = 10
        self.lengthPerMove = 3
        self.direction = 1
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timerFunction)
        self.signal = freshSignal()
        
        # connect signal and slot
#        self.signal.freshFunction.connect(self.saySomeWords)
        
#    def saySomeWords(self,words):
#        print words
        
    def fresh(self):
        self.ax.set_xlim(self.x,self.x+self.zoomWidth)
        self.vline.set_xdata(self.x+self.zoomWidth/2.0)
        self.canvas.draw()
        self.signal.freshFunction.emit(self.x, self.zoomWidth)
    
    def freshFromLowerPlot(self,left,width):
        self.x = left
        self.zoomWidth = width
        self.ax.set_xlim(self.x,self.x+self.zoomWidth)
        self.vline.set_xdata(self.x+self.zoomWidth/2.0)
        self.canvas.draw()
        
    def timerFunction(self):
        self.fresh()
        self.x = self.x + self.lengthPerMove*self.direction
        
    def pauseMove(self):
        self.timer.stop()
        
    def startMove(self):
        self.direction = 1
        self.timer.start(self.timeInterval)
        
    def reverseMove(self):
        self.direction = -1
        self.timer.start(self.timeInterval)
        
    def goRight(self):
        self.x = self.x + self.lengthPerMove
        self.fresh()
    
    def goLeft(self):
        self.x = self.x - self.lengthPerMove
        self.fresh()
        
    def zoomIn(self):
        self.zoomWidth = self.zoomWidth/2.0
        self.x = self.x + self.zoomWidth/2.0
        self.fresh()
        
    def zoomOut(self):
        self.zoomWidth = self.zoomWidth*2.0
        self.x = self.x - self.zoomWidth/4.0
        self.fresh()
        
    def speedUp(self):
        self.lengthPerMove = self.lengthPerMove*2.0
    
    def speedDown(self):
        self.lengthPerMove = self.lengthPerMove/2.0
        
    def drawImage(self,wave):
        self.clf()
        self.ax = self.add_axes([0.1,0.1,0.8,0.8])
        ax = self.ax
        ax.set_xlim(self.x,self.x+self.zoomWidth)
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
        
#        dataOne = zip(*waveData)[0]
#        dataTwo = zip(*waveData)[1]
#        line,  = ax.plot(dataOne)
#        ax.fill_between(t,dataOne,dataTwo)
#        print ax.fill_between(t,dataOne,dataTwo)
#        print dir(ax)
        ax.axhline(y=0,color='0.8')
        self.vline = ax.axvline(x=self.x+self.zoomWidth/2.0,color='red')
#        self.vline.set_xdata(self.x+self.zoomWidth/3.0)
#        ax.set_axis_on()
#        ax.fill_between(t,dataTwo)
#        ax.plot(t,[0]*dataNumber,'r')
        
#        ax.draw_artist(line[0])

#        self.canvas.draw()
#        ax.figure.canvas.draw()
#        line[0].figure.canvas.draw()
#        self.translation()


#        background = self.canvas.copy_from_bbox(ax.bbox)
#        ax.draw_artist(line)
#        self.canvas.blit(axes.bbox)
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
        
if __name__ == "__main__":
    fig2 = fig()
