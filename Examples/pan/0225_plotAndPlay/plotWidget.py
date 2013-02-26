from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from upperPlotFigure import fig
class plotWidget(FigureCanvas):
    def __init__(self, parent=None):
        self.figure = fig()
        super(plotWidget,self).__init__(self.figure)
        self.setWindowTitle("pyside test_plot fig FigureCanvas")
#        self.resize(1000, 250)
    def zoomIn(self):
        self.figure.zoomIn()
    def zoomOut(self):
        self.figure.zoomOut()
    def pauseMove(self):
        self.figure.pauseMove()
        
    def contextMenuEvent(self, event):
        actionzoomIn = QtGui.QAction('zoomIn',self)
        actionzoomOut = QtGui.QAction('zoomOut',self)
        actionstart = QtGui.QAction('start',self)
        actionstop = QtGui.QAction('stop',self)
               
        actionzoomIn.triggered.connect(self.zoomIn)
        actionzoomOut.triggered.connect(self.zoomOut)
        actionstart.triggered.connect(self.figure.startMove)
        actionstop.triggered.connect(self.pauseMove)
        
        menu = QtGui.QMenu(self)
        menu.addAction(actionzoomIn)
        menu.addAction(actionzoomOut)
        menu.addSeparator()
        menu.addAction(actionstart)
        menu.addAction(actionstop)
        
        menu.exec_(event.globalPos())