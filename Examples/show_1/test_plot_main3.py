# coding=utf-8
import sys
import numpy as np
from PySide import QtGui
import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.collections import PatchCollection
import matplotlib.patches as mpatches
from matplotlib import mpl
class Widget(FigureCanvas):
    def __init__(self, parent=None):
        fig2 = fig()
        FigureCanvas.__init__(self, fig2)
        self.setWindowTitle("pyside test_plot fig FigureCanvas")
        self.resize(1000, 250)
        
class fig(Figure):
    def __init__(self):
        super(fig,self).__init__(facecolor=(1,1,1))
##        ax = self.add_axes([0.3, 0.2, .35, .25])
##        ax.set_axis_off()
##        cmap1 = mpl.colors.ListedColormap(['#582233', 'g'])
##        bounds1 = [0,2,4]
##        norm = mpl.colors.BoundaryNorm(bounds1, cmap1.N)
##        cb2 = mpl.colorbar.ColorbarBase(ax, cmap=cmap1,
##                                             orientation='horizontal')
          
          
        rows = 20
        columns = 200
        
        width =0.18
        height = 1.0/rows
        
        leftStart = 0.3
        barNumber = 8
        
        for i in range(barNumber):
            i += 1
            left = leftStart + 1./columns*i
            bottom = 1./rows *2*i
            
            rect = [left, bottom, width, height]
            
            colorList = ['#582233', 'g','r']
            rate = [1,2,4,9]
            
#            colorList = ['#582233']
#            rate = [1,2]

            self.createRectangle(rect,colorList,rate)
        
        
    def createRectangle(self,rect,colorList,rate):
        '''
        eg, rect = [0.3, 0.2, .35, .25],
            colorList = ['#582233', 'g']
            rete = '1:2:3'
        '''
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
      
      
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())


