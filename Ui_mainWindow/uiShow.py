from PyQt4 import QtCore,QtGui
from ui_mainWindow import Ui_MainWindow
import sys

class uiShow(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = uiShow()
    window.show()
    sys.exit(app.exec_())
    
