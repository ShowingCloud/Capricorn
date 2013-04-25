from PySide import QtCore,QtGui
from fireDelayed import Ui_Dialog
from protocol import dataPack
import sys
import ftdi2 as ft
import struct
import Queue
import time

class getMessage(QtCore.QObject):
    signalRead = QtCore.Signal()
    def __init__(self, q, parent = None):

        QtCore.QObject.__init__ (self, parent)

        self.signalRead.connect(self.readFun)
        
        self.q = q
        
    def readFun(self):
        try:
            dev = ft.list_devices()
        except:
            dev = []

        while len (dev) == 0:
            
            time.sleep (5)
            print "Rechecking hardware connection..."
            try:
                dev = ft.list_devices()
            except:
                dev = []
            print dev
        self.f = ft.open_ex(dev[0])
        print self.f
        while True:
            datalistR = [None]*20
            datalistW = [None]*20
            item = self.q.get()
            self.f.write(item)
            while self.f.get_queue_status() < 19:
                pass
            readData = self.f.read(self.f.get_queue_status())
            fmtR = '@19B'
            datalistR[0] = 0xAA
            (datalistR[1],datalistR[2],datalistR[3],datalistR[4],datalistR[5],
            datalistR[6],datalistR[7],datalistR[8],datalistR[9],datalistR[10],datalistR[11],
            datalistR[12],datalistR[13],datalistR[14],datalistR[15],datalistR[16],
            datalistR[17],datalistR[18],datalistR[19]) = struct.unpack(fmtR,readData)
            fmtW = '@20B'
            (datalistW[0],datalistW[1],datalistW[2],datalistW[3],datalistW[4],datalistW[5],
            datalistW[6],datalistW[7],datalistW[8],datalistW[9],datalistW[10],datalistW[11],
            datalistW[12],datalistW[13],datalistW[14],datalistW[15],datalistW[16],
            datalistW[17],datalistW[18],datalistW[19]) = struct.unpack(fmtW,item)
            confirmFlag = True
            for i in range(20):
#                print datalistW[i],' ',datalistR[i]
                if datalistR[i]!=datalistW[i]:
                    confirmFlag = False
                    for j in range(2):
                        self.f.write(item)
                        while self.f.get_queue_status() < 19:
                            pass
                        readData = self.f.read(self.f.get_queue_status())
                        fmtR = '@19B'
                        datalistR[0] = 0xAA
                        (datalistR[1],datalistR[2],datalistR[3],datalistR[4],datalistR[5],
                        datalistR[6],datalistR[7],datalistR[8],datalistR[9],datalistR[10],datalistR[11],
                        datalistR[12],datalistR[13],datalistR[14],datalistR[15],datalistR[16],
                        datalistR[17],datalistR[18],datalistR[19]) = struct.unpack(fmtR,readData)
                        fmtW = '@20B'
                        (datalistW[0],datalistW[1],datalistW[2],datalistW[3],datalistW[4],datalistW[5],
                        datalistW[6],datalistW[7],datalistW[8],datalistW[9],datalistW[10],datalistW[11],
                        datalistW[12],datalistW[13],datalistW[14],datalistW[15],datalistW[16],
                        datalistW[17],datalistW[18],datalistW[19]) = struct.unpack(fmtW,item)
                        for i in range(20):
                            if datalistR[i]!=datalistW[i]:
                                confirmFlag = False
            if confirmFlag == False:
                print 'Connect error'
                return 
                     
            print repr(item),'\n',repr(readData)


class uiShow(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        intVal = QtGui.QIntValidator()
        floatVal = QtGui.QDoubleValidator()
        self.ui.lineEditBoxID.setValidator(intVal)
        self.ui.lineEditHead.setValidator(intVal)
        self.ui.lineEditTime.setValidator(floatVal)
        self.data = {'head':0xAAF0,'length':0x14,'function':0x01,
                     'ID':0xAABBCCDD,'fireBox':None,'firePoint':None,
                     'seconds':None,'offsetSec':None,'crc':0,'tail':0xDD}
        self.dataSync = {'head':0xAAF0,'length':0x0A,'function':0x04,
                         'ID':0xAABBCCDD,'seconds':None,'crc':0,'tail':0xDD}
        self.ExistList = []
        
        self.q = Queue.Queue()
        self.c = getMessage(self.q)
        thread = QtCore.QThread()
        self.c.moveToThread(thread)
        thread.start()
        print 'signal emit'
        self.c.signalRead.emit()
        self.PauseFlag = True
        self.startFlag = False
        self.downloadFlag = False
        self.ui.tableView.setAlternatingRowColors(True)
        self.model = QtGui.QStandardItemModel(0, 2, self)
        self.model.setHorizontalHeaderLabels(['BoxID','Heads','Time'])
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setColumnWidth(0,100)
        self.ui.tableView.setColumnWidth(1,100)
        self.ui.tableView.setColumnWidth(2,100)
        self.proxyModel = QtGui.QSortFilterProxyModel()
        self.proxyModel.setDynamicSortFilter(True)
        self.proxyModel.setSourceModel(self.model)
        self.ui.tableView.setModel(self.proxyModel)
        self.ui.tableView.setSortingEnabled(True)
        self.ui.pushButtonAdd.clicked.connect(self.addFun)
        self.ui.pushButtonDownload.clicked.connect(self.downloadFun)
        self.ui.pushButtonStart.clicked.connect(self.startFun)
        self.ui.pushButtonPause.clicked.connect(self.pauseFun)

    def startFun(self):
        if self.downloadFlag == False:
            print 'Please download first'
            return
        self.startFlag = True
        if self.PauseFlag == False:
            return
        self.timer = QtCore.QTimer()
        QtCore.QObject.connect(self.timer,QtCore.SIGNAL("timeout()"), self.timerEvent)
        self.timer.start(1000)
        self.timeCount = 0
        self.downloadFlag = False
        
    def pauseFun(self):
        if self.startFlag == False:
            print 'please start first'
            return
        if self.PauseFlag == True:
            self.timer.stop()
            self.PauseFlag = False
            self.ui.pushButtonPause.setText('Continue')
        else:
            self.timer.start(1000)
            self.PauseFlag = True
            self.ui.pushButtonPause.setText('Pause')
        
    def timerEvent(self):
        self.sync()
        
    def sync(self):
        self.dataSync['seconds'] = self.timeCount
        dataPacks = dataPack(self.dataSync)
        self.q.put(dataPacks.package)
        self.timeCount = self.timeCount + 1
        print 'seconds' , self.timeCount
        if self.timeCount > self.maxTime:
            self.timer.stop()
            self.startFlag = False
            self.model.clear()
            self.model.setHorizontalHeaderLabels(['BoxID','Heads','Time'])
            self.ui.tableView.setModel(self.model)
            self.ui.tableView.setColumnWidth(0,100)
            self.ui.tableView.setColumnWidth(1,100)
            self.ui.tableView.setColumnWidth(2,100)
            print "*******************"
            print '   Fire finished'
            print "*******************"
            
    def addFun(self):
        if self.ui.lineEditBoxID.text() == '' or self.ui.lineEditHead.text() == '' or self.ui.lineEditTime.text() == '':
            print 'please input data'
            return
        for row in self.ExistList:
            if row['Box'] == self.ui.lineEditBoxID.text() and row['Head'] == self.ui.lineEditHead.text():
                print 'exist'
                return
        node = {'Box':None,'Head':None,'Time':None}
        node['Box'] =self.ui.lineEditBoxID.text()
        node['Head'] = self.ui.lineEditHead.text()
        node['Time'] = self.ui.lineEditTime.text()
        self.ExistList.append(node)
        
        newRow = []
        newRow.append (QtGui.QStandardItem (self.ui.lineEditBoxID.text()))
        newRow.append (QtGui.QStandardItem (self.ui.lineEditHead.text()))
        newRow.append (QtGui.QStandardItem (self.ui.lineEditTime.text()))
        
        self.model.appendRow(newRow)

    def downloadFun(self):
        if len(self.ExistList)== 0:
            print 'Please add first'
            return
        self.maxTime = 0.0
        for node in self.ExistList:
            sec = float(node['Time'])
            if sec>self.maxTime:
                self.maxTime = sec
            self.data['fireBox'] = int(node['Box'])
            self.data['firePoint'] = int(node['Head'])
            self.data['seconds'] = int(sec)
            self.data['offsetSec'] = int((sec - int(sec))*1000)
            print self.data['seconds'],'.',self.data['offsetSec']
            dataPackage = dataPack(self.data)
            print repr(dataPackage.package)
            self.q.put (dataPackage.package)
        self.ExistList = []
        self.downloadFlag = True

        
def main():
    app = QtGui.QApplication(sys.argv)
    window = uiShow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
