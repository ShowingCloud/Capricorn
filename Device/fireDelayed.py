from PySide import QtCore, QtGui
from ui_fireDelayed import Ui_Dialog
from protocol import dataPack
import sys
import Queue
import time
from PySide.QtCore import Qt, QPoint, Slot, SIGNAL

try:
    import ftdi2 as ft
except:
    print "Unable to load ftdi2 driver"
    pass

class getMessage (QtCore.QObject):
    signalRead = QtCore.Signal()

    def __init__ (self, q, parent = None):
        QtCore.QObject.__init__ (self, parent)

        self.signalRead.connect(self.readFun)

        self.q = q

    def readFun (self):
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

        self.f = ft.open_ex(dev[0])
        print self.f

        while True:
            item = self.q.get()

            confirmFlag = False
            for i in xrange (3):
                self.f.write(item[0])
                break

#                if not item[1]: # We don't need a confirmation for TIME_SYNC
#                    confirmFlag = True
#                    readData = ""
#                    break

#                while self.f.get_queue_status() < 20:
#                    pass
#                readData = self.f.read(self.f.get_queue_status())
#                print repr(readData)

#                if item[0] == readData:
#                    confirmFlag = True
#                    break

#            if confirmFlag == False:
#                print 'Data damaged. Please check the device.'

#            print repr(item[0]),'\n',repr(readData)
            print repr(item[0])


class uiShow(QtGui.QDialog):

    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)

        self.ui = Ui_Dialog()
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
        time.sleep(1)
        self.c.signalRead.emit()

        self.pauseFlag = True
        self.deleteFlag = True
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
        self.ui.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tableView.customContextMenuRequested.connect(self.deleteBoxAction)

        self.ui.pushButtonAdd.clicked.connect(self.addFun)
        self.ui.pushButtonDownload.clicked.connect(self.downloadFun)
        self.ui.pushButtonStart.clicked.connect(self.startFun)
        self.ui.pushButtonPause.clicked.connect(self.pauseFun)
        self.ui.pushButtonDownload.setEnabled(False)
        self.ui.pushButtonStart.setEnabled(False)
        self.ui.pushButtonPause.setEnabled(False)

    @Slot(QPoint)
    def deleteBoxAction(self,point):
        if self.deleteFlag == False:
            return

        rightMenu = QtGui.QMenu(self)
        deleteAction = QtGui.QAction("Delete", self)
        self.row = self.ui.tableView.rowAt(point.y())
        deleteAction.connect(SIGNAL("triggered()"), self.deleteRecord)
        rightMenu.addAction(deleteAction)
        rightMenu.exec_(QtGui.QCursor.pos())

    def deleteRecord(self):
        print 'deleted'
        node = {'Box':None,'Head':None,'Time':None}
        node['Box'] = self.model.item(self.row,0).text()
        node['Head'] = self.model.item(self.row,1).text()
        node['Time'] = self.model.item(self.row,2).text()

        self.model.takeRow(self.row)
        for row in self.ExistList:
            if row['Box'] == node['Box'] and row['Head'] == node['Head']:
                self.ExistList.remove(row)

    def startFun(self):
        self.timer = QtCore.QTimer()
        QtCore.QObject.connect(self.timer,SIGNAL("timeout()"), self.timerEvent)
        self.timer.start(1000)
        self.timeCount = 0
        self.downloadFlag = False

        self.ui.pushButtonPause.setEnabled(True)
        self.ui.pushButtonStart.setEnabled(False)

    def pauseFun(self):
        if self.pauseFlag == True:
            self.timer.stop()
            self.pauseFlag = False
            self.ui.pushButtonPause.setText('Continue')
        else:
            self.timer.start(1000)
            self.pauseFlag = True
            self.ui.pushButtonPause.setText('Pause')

    def timerEvent(self):
        self.sync()

    def sync(self):
        print 'seconds' , self.timeCount
        self.dataSync['seconds'] = self.timeCount
        dataPacks = dataPack(self.dataSync)
        self.q.put((dataPacks.package, False))

        self.timeCount = self.timeCount + 1
        if self.timeCount > self.maxTime:
            self.timer.stop()
            self.deleteFlag = True
            self.ui.pushButtonPause.setEnabled(False)
            self.ui.pushButtonAdd.setEnabled(True)
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
        node['Time'] = float(self.ui.lineEditTime.text())
        self.ExistList.append(node)
        sortedList = sorted(self.ExistList,key = lambda k:k['Time'])

        self.model.clear()
        self.model.setHorizontalHeaderLabels(['BoxID','Heads','Time'])
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setColumnWidth(0,100)
        self.ui.tableView.setColumnWidth(1,100)
        self.ui.tableView.setColumnWidth(2,100)

        for node in sortedList:
            newRow = []
            newRow.append (QtGui.QStandardItem (node['Box']))
            newRow.append (QtGui.QStandardItem (node['Head']))
            newRow.append (QtGui.QStandardItem (str(node['Time'])))
            self.model.appendRow(newRow)

        self.ui.pushButtonDownload.setEnabled(True)

    def downloadFun(self):
        if len(self.ExistList)== 0:
            print 'Please add first'
            return

        self.maxTime = 0.0

        for node in self.ExistList:
            sec = node['Time']
            if sec > self.maxTime:
                self.maxTime = sec

            self.data['fireBox'] = int(node['Box'])
            self.data['firePoint'] = int(node['Head'])
            self.data['seconds'] = int(sec)
            self.data['offsetSec'] = int((sec - int(sec))*1000)
            print self.data['seconds'],'.',self.data['offsetSec']
            dataPackage = dataPack(self.data)
            print repr(dataPackage.package)
            self.q.put ((dataPackage.package, True))

        self.ExistList = []
        self.downloadFlag = True
        self.ui.pushButtonStart.setEnabled(True)
        self.ui.pushButtonAdd.setEnabled(False)
        self.ui.pushButtonDownload.setEnabled(False)
        self.deleteFlag = False


def main():
    app = QtGui.QApplication(sys.argv)
    window = uiShow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
