# coding=utf-8
import sys
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

import time

class Widget(FigureCanvas):
    def __init__(self, parent=None):
        leftStart =0.1
        width = 0.2
        self.fig2 = fig(leftStart=leftStart, width=width)
        FigureCanvas.__init__(self, self.fig2)
        self.setWindowTitle("pyside test_plot fig FigureCanvas")
        self.resize(1000, 250)
        
class fig(Figure):
    def __init__(self,leftStart=0.1, width=0.2):
        super(fig,self).__init__(facecolor=(1,1,1))
    
        self.rows = 20
        self.columns = 200
        self.width = width
        self.height = 1.0/20
        self.barNumber = 8
        self.leftStart = leftStart

        self.drawRectangles()
        self.translation()
        
    def translation(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.rightMove)
        self.timer.start(100)
        
    def rightMove(self):
        self.clf()
        print 7
        self.leftStart +=0.01

        self.drawRectangles()
        
        self.canvas.draw()
        
    def changeSize(self, value):
        self.width = value
        self.clf()
        self.drawRectangles()
        self.canvas.draw()
        
    def drawRectangles(self):
        rows = self.rows
        columns = self.columns
        width = self.width
        height = self.height
        barNumber = self.barNumber
        leftStart = self.leftStart
        
        for i in range(barNumber):
            i += 1
            left = leftStart + 1./columns*i
            bottom = 1./rows *2*i
            rect = [left, bottom, width, height]
            colorList = ['#582233', 'g','r']
            rate = [1,2,4,9]
            self.createRectangle(rect,colorList,rate)
            
    def createRectangle(self,rect,colorList,rate):
        ax = self.add_axes(rect)
        ax.set_axis_off()
        cmap1 = mpl.colors.ListedColormap(colorList)
        bounds1 = rate
        norm = mpl.colors.BoundaryNorm(bounds1, cmap1.N)
        cb2 = mpl.colorbar.ColorbarBase(ax, cmap=cmap1,
                                        norm=norm,
                                        boundaries=bounds1,
                                             orientation='horizontal',
                                             spacing='proportional')
def timer(interval,aaa):
    global w
    print  dir(w)
    x = 0
    while 1:
        time.sleep(interval)
        x = x + 1
        print x

def test():
    thread.start_new_thread(timer, (1,2))
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    global w
    w = Widget()
    w.show()
#    test()
    sys.exit(app.exec_())
