from PySide import QtGui,QtCore
from UI import ui_mainWindow
from Device import protocol
from Models.EngineeringDB import ScriptData,IgnitorsData
import struct
import Queue

try:
    import ftdi2 as ft
except:
    pass
#from UI.mainWidget import MainWidget
#
#class getMessage(QtCore.QObject):
#    signalRead = QtCore.Signal()
#    def __init__(self, q, parent = None):
#        print 'thread1'
#        QtCore.QObject.__init__ (self, parent)
#        print 'thread2'
#        self.signalRead.connect(self.readFun)
#        self.q = q
#    def readFun(self):
#        try:
#            dev = ft.list_devices()
#            print dev[0]
#            self.f = ft.open_ex(dev[0])
#        except:
#            return
#        
#        while True:
#            datalistR = [None]*14
#            datalistW = [None]*14
#            item = self.q.get()
#            self.f.write(item)
#            while self.f.get_queue_status() < 13:
#                pass
#            readData = self.f.read(self.f.get_queue_status())
#            fmtR = '@13B'
#            datalistR[0] = 0xAA
#            (datalistR[1],datalistR[2],datalistR[3],datalistR[4],datalistR[5],
#            datalistR[6],datalistR[7],datalistR[8],datalistR[9],datalistR[10],datalistR[11],
#            datalistR[12],datalistR[13]) = struct.unpack(fmtR,readData)
#            fmtW = '@14B'
#            (datalistW[0],datalistW[1],datalistW[2],datalistW[3],datalistW[4],datalistW[5],
#            datalistW[6],datalistW[7],datalistW[8],datalistW[9],datalistW[10],datalistW[11],
#            datalistW[12],datalistW[13]) = struct.unpack(fmtW,item)
#            confirmFlag = True
#            for i in range(14):
##                print datalistW[i],' ',datalistR[i]
#                if datalistR[i]!=datalistW[i]:
#                    confirmFlag = False
#                    for j in range(2):
#                        self.f.write(item)
#                        while self.f.get_queue_status() < 13:
#                            pass
#                        readData = self.f.read(self.f.get_queue_status())
#                        fmtR = '@13B'
#                        datalistR[0] = 0xAA
#                        (datalistR[1],datalistR[2],datalistR[3],datalistR[4],datalistR[5],
#                        datalistR[6],datalistR[7],datalistR[8],datalistR[9],datalistR[10],datalistR[11],
#                        datalistR[12],datalistR[13]) = struct.unpack(fmtR,readData)
#                        fmtW = '@14B'
#                        (datalistW[0],datalistW[1],datalistW[2],datalistW[3],datalistW[4],datalistW[5],
#                        datalistW[6],datalistW[7],datalistW[8],datalistW[9],datalistW[10],datalistW[11],
#                        datalistW[12],datalistW[13]) = struct.unpack(fmtW,item)
#                        for i in range(14):
#                            if datalistR[i]!=datalistW[i]:
#                                confirmFlag = False
#            if confirmFlag == False:
#                print 'Connect error'
#                return 
#                     
#            print repr(item),'\n',repr(readData)
#
#
#        
class MainShow(QtGui.QMainWindow):
    def __init__(self, sess, session, fieldUUID,musicPath, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.sess = sess
        self.session = session
        self.fieldUUID = fieldUUID
        self.musicPath = musicPath
        self.ui=ui_mainWindow.Ui_MainWindow(self.sess, self.session, self.fieldUUID,self.musicPath)
        self.ui.setupUi(self)
        
        self.ui.actionDownload.triggered.connect(self.downloadToDevice)
        self.ui.actionExportPDF.triggered.connect(self.exportPDF)
        self.ui.actionProjectExport.triggered.connect(self.projectExport)

        
#        self.q = Queue.Queue()
#        self.c = getMessage(self.q)
#        thread = QtCore.QThread()
#        self.c.moveToThread(thread)
#        thread.start()
#        print 'before emit'
#        self.c.signalRead.emit()
#        print 'after emit'
#        
    def downloadToDevice(self):
        with self.session.begin():
            tableFire = self.session.query(ScriptData).all()
        node = {'head':0xAAF0,'length':0x0E,'function':0x02,'ID':0xAABBCCDD,'fireBox':None,
                'firePoint':None,'seconds':None,'offsetSec':None,'crc':0,'tail':0xDD}
        for row in tableFire:
            if  row.ConnectorID == None:
                reply = QtGui.QMessageBox.question(None,'message','Please choose ignitorBox first',
                                           QtGui.QMessageBox.Ok)
                if reply == QtGui.QMessageBox.Ok:
                    return
            else:
                print 'fire head',row.IgnitorID
        for row in tableFire:
            with self.session.begin():
                ignitorBoxRow = self.session.query(IgnitorsData).filter_by(UUID = row.IgnitorID).first()
            node['fireBox'] = int(ignitorBoxRow.BoxID)
            node['firePoint'] = row.ConnectorID
            node['seconds'] = row.IgnitionTime.seconds
            node['offsetSec'] = row.IgnitionTime.microseconds/1000
            package = protocol.dataPack(node)
            package.pack()
            self.q.put (package.package)
        reply = QtGui.QMessageBox.question(None,'message','DownLoad Finish',
                                           QtGui.QMessageBox.Ok)
        
        
    def exportPDF(self):
        print 'ExportPDF'
        pass
    
    
    def projectExport(self):
        print 'Export Project'
        pass
