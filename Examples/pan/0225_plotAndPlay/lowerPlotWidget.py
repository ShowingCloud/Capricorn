# coding=utf-8
import numpy as np
from PySide import QtGui,QtCore
import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.collections import PatchCollection
import matplotlib.patches as mpatches
from matplotlib import mpl
import waveForm
import sys

class plotWidget(FigureCanvas):
    def __init__(self, parent=None):
        self.figure = fig()
        super(plotWidget,self).__init__(self.figure)
        self.setParent(parent)
        self.setWindowTitle("pyside test_plot fig FigureCanvas")
    
        
class fig(Figure):
    def __init__(self):
        super(fig,self).__init__()
        self.ax = None
        self.signal = freshSignal()
 
    def freshLeftAndWidthFromUpperPlot(self,left, width):
        if self.ax == None:
            return
        if self.span == None:
            return
        else:
                        
            self.left = left
            self.width = width
    #        if self.left<0:
    #            self.ax.set_xlim(self.left,self.dataLength)
    #        elif self.left+self.width<self.dataLength:
    #            self.ax.set_xlim(0,self.dataLength)
    #        else:
    #            self.ax.set_xlim(0,self.left+self.width)
            
            self.vline.set_xdata(self.left+self.width/2.0)
            
            right = self.left + self.width
            xy = np.array([[self.left,0.],[self.left,1.],[right,1.],[right,0.],[self.left,0.]])
            self.span.set_xy(xy)

        
            
        
        self.canvas.draw()
        self.ax.redraw_in_frame()

    def fresh2(self):
        self.freshFromUpperPlot(self.left, self.width)
        
    def drawImage(self,wave):
        self.clf()
        self.ax = self.add_axes([0.1,0.1,0.8,0.8])
        ax = self.ax
#        
        if isinstance(wave, list):
            dataOne = wave[0]
            dataTwo = wave[1]
            dataLength = len(dataOne)
            chunksize = 20000
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
            xcenters = xchunks

            ax.fill_between(xcenters, max_1_2, y2=min_1_2,color='0.6')
            ax.plot(xcenters,mean_1,'b',xcenters,mean_2,'y')
            
            
        else:
            dataOne = wave
            ax.plot(dataOne,'b')
        self.dataLength = len(dataOne)
        ax.set_xlim(0,self.dataLength)
        self.span = ax.axvspan(0, 0, facecolor='g', alpha=0.5,zorder=3)
        self.vline = ax.axvline(x=0,color='red')
        self.canvas.draw()
#        self.connectMoveAction()
        
#    def deleteImage(self):
#        del self.ax
#        self.canvas.draw()
#        
#    def connectMoveAction(self):
#        self.pressX = None
#        self.connect()
#        
#        
#    def connect(self):
#        'connect to all the events we need'
#        self.cidpress = self.canvas.mpl_connect(
#        'button_press_event', self.on_press)
#        self.cidrelease = self.canvas.mpl_connect(
#        'button_release_event', self.on_release)
#    def on_press(self, event):
#        if event.inaxes != self.ax: return
#        contains, attrd = self.span.contains(event)
#        if not contains: return
#        self.pressX =event.xdata
#        
#    def on_release(self, event):
#        if self.pressX is None: return
#        if event.inaxes != self.ax: return
#        dx = event.xdata - self.pressX
#        self.left += dx
#        self.fresh2()
#        self.signal.freshFunction.emit(self.left, self.width)        
#        self.pressX = None
#        

class freshSignal(QtCore.QObject):
    freshFunction = QtCore.Signal(int, int)
    
if __name__ == '__main__':
#    import time
    app = QtGui.QApplication(sys.argv)
    dialog = QtGui.QFileDialog()
    dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
    path = 0
    if dialog.exec_() == QtGui.QDialog.Accepted:
        path = dialog.selectedFiles()[0]
#        print path
    dialog.deleteLater()
    print path
    form = waveForm.waveform(path)
    plot_Widget = plotWidget()
#    time.sleep(2)
    plot_Widget.figure.drawImage(form.getWaveData())
#    plot_Widget.figure.drawImage((1,8,3))
    plot_Widget.show()
 
    sys.exit(app.exec_())
    