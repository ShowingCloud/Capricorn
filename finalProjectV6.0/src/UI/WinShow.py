from PySide import QtGui
from UI import ui_mainWindow
#from UI.mainWidget import MainWidget


class MainShow(QtGui.QMainWindow):
    def __init__(self, sess, session, fieldUUID, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.sess = sess
        self.session = session
        self.fieldUUID = fieldUUID
        
        self.ui=ui_mainWindow.Ui_MainWindow(self.sess, self.session, self.fieldUUID)
        self.ui.setupUi(self)
        


