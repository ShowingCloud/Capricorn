# coding=utf-8
from PySide import QtGui,QtCore
from PySide.QtGui import QProgressDialog
import sys
import time

class newThread(QtCore.QThread): 
    def __init__(self,parent=None): 
        print 3
        super(newThread,self).__init__(parent) 
        self.working=True 
        self.num=0
        self.progressDialog = waitWidget()
        self.progressDialog.show()
    def __del__(self): 
        self.working=False 
        self.wait() 
    def run(self): 
        print 'thread run in thread'
        while self.working==True: 
#            file_str='File index {0}'.format(self.num) 
            self.num+=1 
#            self.emit(QtCore.SIGNAL('output(QString)'),file_str) 
            self.emit(QtCore.SIGNAL('output(int)'),self.num)
            self.sleep(0.5)
#            self.progressDialog.setValue(self.num)
            
    def changeProgress(self,intValue):
        self.progressDialog.setValue(intValue)
            
class waitWidget(QtGui.QProgressDialog):
    def __init__(self,parent=None):
        super(waitWidget,self).__init__(parent)
        self.setGeometry(300,300,400,200)
        self.setMaximum(100)
        self.setValue(30)
#        for i in xrange(100):
#            self.setValue(i)
#            time.sleep(0.1)
        
#        progress.setValue(progress.value() + 1)
        
#        waitBar = QtGui.QProgressBar

    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    print 'before thread'
    thread = newThread()
    #    QtGui.QWidget.connect(wait, SIGNAL('canceled ()'), canceled)
    thread.start()
    print 'after  thread' 
#    for i in xrange(100):
#        wait.setValue(wait.value()+1)
#        time.sleep(0.3)
    
    sys.exit(app.exec_())