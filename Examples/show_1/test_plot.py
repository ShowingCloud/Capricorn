# -*- coding: utf-8 -*-
import sys
import numpy as np
from PySide import QtCore,  QtGui
import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
import pylab
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class fig(Figure):
    def __init__(self):
        super(fig,self).__init__(facecolor=(1,1,1))
        Z = np.arange(10000.0)
        Z.shape = 50,  200
        ax = self.add_axes([0.3,0.5,0.8,0.9])
        ax.set_axis_off()
#        print dir(ax)
        image = self.figimage(Z, xo=0, yo=0)
        ax.add_artist(image)


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    fig = fig()
    canvas = FigureCanvas(fig)
    canvas.adjustSize()
    win = QtGui.QMainWindow()
    win.setCentralWidget(canvas)
    win.adjustSize()
    win.show()
    sys.exit(app.exec_())
