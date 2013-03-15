from PyQt4 import QtCore,QtGui
from deviceTest import Ui_MainWindow
import sys

class uiShow(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

def main():
    app = QtGui.QApplication(sys.argv)
    window = uiShow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
