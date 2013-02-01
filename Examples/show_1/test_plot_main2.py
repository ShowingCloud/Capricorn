# -*- coding: utf-8 -*-
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


class Widget(FigureCanvas):
    def __init__(self, parent=None):
        fig2 = fig()
        FigureCanvas.__init__(self, fig2)
        self.setWindowTitle("pyside test_plot fig FigureCanvas")
        self.resize(1000, 250)
        
        
class fig(Figure):
    def __init__(self):
        super(fig,self).__init__(facecolor=(1,1,1))
        ax = self.add_axes([0., 0., 1., 1.])
        ax.set_axis_off()
        
        rows = 20
        columns = 200
        
        width =0.18
        height = 1.0/rows
        
        leftStart = 0.3
        barNumber = 8
        
        patches = []
        for i in range(barNumber):
            i += 1
            left = leftStart + 1./columns*i
            bottom = 1./rows *2*i
            art = mpatches.Rectangle(np.array([left, bottom]), width, height,
                    fill=True, color='red')
            patches.append(art)
            
        colors = 100*np.random.rand(len(patches))
        print colors
        collection = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.4)
        #collection.set_array(np.array(colors))
        ax.add_collection(collection)
        
if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())


