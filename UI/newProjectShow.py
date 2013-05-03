from PySide import QtGui
from ui_newProject import Ui_Dialog
import sys
from UI.newImportProjectShow import ImportProjectShow
class newProjectShow(QtGui.QDialog):
    def __init__(self,sess,parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonImport.clicked.connect(self.importProject)
        self.sess = sess
    def importProject(self):
        print 'import'
        self.project = ImportProjectShow(self.sess)
        self.project.show()
        self.close()
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = newProjectShow()
    window.show()
    sys.exit(app.exec_())
        
