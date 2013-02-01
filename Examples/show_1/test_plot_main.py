import test_plot
from PySide import QtCore,  QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import os

class Widget(FigureCanvas):
    def __init__(self, parent=None):
        fig = test_plot.fig()
        FigureCanvas.__init__(self, fig)
        self.setWindowTitle("pyside test_plot fig FigureCanvas")
        self.adjustSize()
#        print dir(fig)
#        print fig.get_size_inches()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())
