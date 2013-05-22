from PySide import QtGui,QtCore
from UI import ui_mainWindow
from Device import protocol
from Models.ProjectDB import ScriptData,IgnitorsData,ParametersData,FieldsData
from Models.LocalDB import ProjectsData
import Queue
import time
from datetime import datetime
from config import appdata
import tarfile, os, sys, subprocess, shutil
from Frontend.PrintPDF import PrintTable, TABLEFields, TABLEProductList, TABLEFireSequence
import json
import struct
try:
    from Device import ftdi2 as ft
except:
    pass

class getMessage(QtCore.QObject):
    signalRead = QtCore.Signal()
    def __init__(self, q, statusQueue,parent = None):

        QtCore.QObject.__init__ (self, parent)

        self.signalRead.connect(self.readFun)
        self.q = q
        
        self.statusQueue = statusQueue
        
    def readFun(self):
        try:
            dev = ft.list_devices()
        except:
            dev = []
            
        while len (dev) == 0:
            if not self.q.empty():
                item = self.q.get()
#                self.statusQueue.put(item)
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
            item = self.q.get()
            self.f.write(item)
            while self.f.get_queue_status() < 19:
                pass
            readData = self.f.read(self.f.get_queue_status())
            confirmFlag = True
            if item[1:20:1] != readData :
                confirmFlag = False
                for i in range(2):
                    self.f.write(item)
                    while self.f.get_queue_status() < 19:
                        pass
                    readData = self.f.read(self.f.get_queue_status())
                    if item[1:20:1] == readData:
                        confirmFlag = True
                        break
            if confirmFlag == False:
                self.statusQueue.put(item)
                print 'Connect error,please check device'
                
            elif self.q.empty() and confirmFlag != False:
                self.statusQueue.put('Finished')
                
            print repr(item),'\n',repr(readData)
        
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
        self.ui.widget_wave.upAndDownWaveWidget.analyzeWaveAndDrawInit()
        self.ui.actionMinimize.triggered.connect(self.showMinimized)

        self.q = Queue.Queue()
        self.statusQueue = Queue.Queue()
        self.c = getMessage(self.q,self.statusQueue)
        self.thread = QtCore.QThread()
        self.c.moveToThread(self.thread)
        self.getLocalData()
        self.thread.start()
        self.showMaximized()
        print 'Read signal emit'
        self.c.signalRead.emit()
        self.ui.widgetDatabase.musicSignal.emit()

        
    def downloadToDevice(self): 
        try:
            dev = ft.list_devices()
        except:
            dev = []
        if not len(dev) :
            QtGui.QMessageBox.question(None,'message','No device ,please check',
                                                            QtGui.QMessageBox.Ok)
            return
        with self.session.begin():
            tableFire = self.session.query(ScriptData).all()
        node = {'head':0xAAF0,'length':0x14,'function':0x01,'ID':0xAABBCCDD,'fireBox':None,
                'firePoint':None,'seconds':None,'offsetSec':None,'crc':0,'tail':0xDD}
        
        for row in tableFire:
            if  row.ConnectorID == None:
                reply = QtGui.QMessageBox.question(None,'message','Please choose ignitorBox first',
                                           QtGui.QMessageBox.Ok)
                if reply == QtGui.QMessageBox.Ok:
                    return
                
        for row in tableFire:
            with self.session.begin():
                ignitorBoxRow = self.session.query(IgnitorsData).filter_by(UUID = row.IgnitorID).first()
            node['fireBox'] = int(ignitorBoxRow.BoxID)
            node['firePoint'] = row.ConnectorID
            node['seconds'] = int(row.IgnitionTime.seconds)
            node['offsetSec'] = int(row.IgnitionTime.microseconds/1000)
            package = protocol.dataPack(node)
            package.pack()
            self.q.put (package.package)
            print 'fire head',node['firePoint'],'fire Box ',node['fireBox']
            print repr(package.package)
            self.timer = QtCore.QTimer()
            QtCore.QObject.connect(self.timer,QtCore.SIGNAL("timeout()"), self.checkQueue)
            self.timer.start(2000)
            
    def checkQueue(self):
        print 'Checking Queue...'
        if self.statusQueue.empty():
            return
        statusReturn = self.statusQueue.get()
        if statusReturn == 'Finished':
            QtGui.QMessageBox.question(None,'message','Upload Finish',
                                                QtGui.QMessageBox.Ok)
        else:
            datalist = [0]*20
            (datalist[0],datalist[1],datalist[2],datalist[3],datalist[4],datalist[5],
             datalist[6],datalist[7],datalist[8],datalist[9],datalist[10],datalist[11],
             datalist[12],datalist[13],datalist[14],datalist[15],datalist[16],datalist[17],
             datalist[18],datalist[19]) = struct.unpack('@20B',statusReturn)
            boxID = datalist[8] * 0x100 + datalist[9]
            fireHead = datalist[10] * 0x100 + datalist[11]
            seconds = datalist[12] * 0x1000000 + datalist[13] * 0x10000 + datalist[14] * 0x100 + datalist[15]
            offsetSec = datalist[16] * 0x100 + datalist[17]
            igniteTime = float(seconds) + float(offsetSec)/1000
            QtGui.QMessageBox.question(None,'message','Upload failed,\n BoxID is %d ,ignite head is %d ,time is %f'%(boxID,fireHead,round(igniteTime,2)),
                                                QtGui.QMessageBox.Ok)
            
      
        
    def exportPDF(self,OpenReader = True):
        print 'ExportPDF'

        PrintTable (self.sess, self.session, TABLEFields)
        PrintTable (self.sess, self.session, TABLEProductList)
        PrintTable (self.sess, self.session, TABLEFireSequence)

        if not OpenReader:
            return

        try:
            for pdfs in ['Fields', 'FireSequence', 'ProductList']:
                if sys.platform == 'darwin':
                    subprocess.call (('open', os.path.join (appdata, 'pdf', pdfs + '.pdf')))
                elif sys.platform == 'win32':
                    os.startfile (os.path.join (appdata, 'pdf', pdfs + '.pdf'))
                else:
                    subprocess.call (('xdg-open', os.path.join (appdata, 'pdf', pdfs + '.pdf')))
        except:
            pass
    def getLocalData(self):
        FieldList = []
        with self.session.begin():
            ignitorCount = self.session.query(IgnitorsData).count()
        with self.session.begin():
            fireworksCount = self.session.query(ScriptData).count()
            print 'ignitorCount= ',ignitorCount
            print 'fireworksCount= ',fireworksCount
        with self.session.begin():
            fieldTable = self.session.query(FieldsData).all()
        for row in fieldTable:
            FieldList.append(row.UUID)
        FieldList1 = json.dumps(FieldList)
        
        with self.session.begin():
            parameter = self.session.query(ParametersData).all()[0]
            parameter.MTime = datetime.utcnow()
            parameter.FieldList = FieldList1
            parameter.ShellCount = fireworksCount
            parameter.ModuleCount = ignitorCount
            
        with self.sess.begin():
            project = self.sess.query(ProjectsData).filter_by(Name = parameter.Name).first()
            project.MTime = datetime.utcnow()
            project.ShellCount = fireworksCount
            project.ModuleCount = ignitorCount
            
    def closeEvent(self,event):
        self.getLocalData()
        self.thread.quit()
        self.thread.exit()
        print 'closeEvent'
        event.accept()

    def projectExport(self):
        print 'Export Project'
        self.getLocalData()

        tmpdir = os.path.join (appdata, 'tmp')
        if os.path.exists (tmpdir):
            if not os.path.isdir (tmpdir):
                os.remove (tmpdir)
                os.mkdir (tmpdir)
        else:
            os.mkdir (tmpdir)

        tar = tarfile.open (os.path.join (tmpdir, "export.tgz"), "w:gz")

        print self.session.bind.url.database
        files = [(os.path.join (appdata, self.session.bind.url.database), os.path.basename (self.session.bind.url.database))]

        self.exportPDF (False)
        for pdfs in ['Fields', 'FireSequence', 'ProductList']:
            files.append ((os.path.join (appdata, 'pdf', pdfs + '.pdf'), pdfs + '.pdf'))

        for f, name in files:
            tar.add (f, arcname = name)

        tar.close()

        filename = QtGui.QFileDialog.getSaveFileName (self,
                self.tr ("Save Project As..."),
                "output.tgz",
                self.tr ("Compressed Archives (*.tgz, *.tar.gz)"))
        shutil.copy2 (os.path.join (tmpdir, "export.tgz"), filename[0])
        pass
