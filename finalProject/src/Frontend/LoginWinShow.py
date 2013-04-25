from PySide import QtCore,QtGui
from UI import ui_mainWindow
import sys


class uiShow(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self)
        self.ui=ui_mainWindow.Ui_MainWindow()
        self.ui.setupUi(self)

def main():
    app = QtGui.QApplication(sys.argv)
    window = uiShow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
