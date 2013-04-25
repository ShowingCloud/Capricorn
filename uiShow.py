from PySide import QtCore,QtGui
from deviceTest1 import Ui_MainWindow
import sys

class uiShow(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

    def closeEvent(self,event):
        reply = QtGui.QMessageBox.question(self, 'Message', 
                                'Are you sure to quit?',
                            QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
            self.ui.f.close()
        else:
            event.ignore()
        
def main():
    app = QtGui.QApplication(sys.argv)
    window = uiShow()
    window.show()
    #print sys.platform
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
