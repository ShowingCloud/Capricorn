from PySide import QtCore,QtGui
import Queue, time
from ui_connectTest import Ui_Dialog
import sys
from protocol import dataPack

class getMessage(QtCore.QObject):
    signalRead = QtCore.Signal()
    def __init__(self, q,p,parent = None):

        QtCore.QObject.__init__ (self, parent)

        self.signalRead.connect(self.readFun)
        self.p = p
        self.q = q
##        list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
##        for i in list1:
##            self.p.put(i)
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
            datalistR = [None]*14
            datalistW = [None]*14
            item = self.q.get()
            self.f.write(item)
            while self.f.get_queue_status() < 13:
                pass
            readData = self.f.read(self.f.get_queue_status())
            fmtR = '@13B'
            datalistR[0] = 0xAA
            (datalistR[1],datalistR[2],datalistR[3],datalistR[4],datalistR[5],
            datalistR[6],datalistR[7],datalistR[8],datalistR[9],datalistR[10],datalistR[11],
            datalistR[12],datalistR[13]) = struct.unpack(fmtR,readData)
            fmtW = '@14B'
            (datalistW[0],datalistW[1],datalistW[2],datalistW[3],datalistW[4],datalistW[5],
            datalistW[6],datalistW[7],datalistW[8],datalistW[9],datalistW[10],datalistW[11],
            datalistW[12],datalistW[13]) = struct.unpack(fmtW,item)
            confirmFlag = True
            for i in range(14):
#                print datalistW[i],' ',datalistR[i]
                if datalistR[i]!=datalistW[i]:
                    confirmFlag = False
                    for j in range(2):
                        self.f.write(item)
                        while self.f.get_queue_status() < 13:
                            pass
                        readData = self.f.read(self.f.get_queue_status())
                        fmtR = '@13B'
                        datalistR[0] = 0xAA
                        (datalistR[1],datalistR[2],datalistR[3],datalistR[4],datalistR[5],
                        datalistR[6],datalistR[7],datalistR[8],datalistR[9],datalistR[10],datalistR[11],
                        datalistR[12],datalistR[13]) = struct.unpack(fmtR,readData)
                        fmtW = '@14B'
                        (datalistW[0],datalistW[1],datalistW[2],datalistW[3],datalistW[4],datalistW[5],
                        datalistW[6],datalistW[7],datalistW[8],datalistW[9],datalistW[10],datalistW[11],
                        datalistW[12],datalistW[13]) = struct.unpack(fmtW,item)
                        for i in range(14):
                            if datalistR[i]!=datalistW[i]:
                                confirmFlag = False
            if confirmFlag == False:
                print 'Connect error'
            else:
                head = dataListR[10]*256+dataListR[11]
                self.p.put(head)
                print head
                print repr(item),'\n',repr(readData)


class uiShow(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.buttonConnect()
        self.data = {'head':0xAAF0,'length':0x0E,'function':0x02,
                     'ID':0xAABBCCDD,'fireBox':None,'firePoint':None,
                     'crc':0,'tail':0xDD}
        
        self.q = Queue.Queue()
        self.p = Queue.Queue()
        self.c = getMessage(self.q,self.p)
        thread = QtCore.QThread()
        self.c.moveToThread(thread)
        thread.start()
        print 'signal emit'
        self.c.signalRead.emit()
        self.timer = QtCore.QTimer()
        QtCore.QObject.connect(self.timer,QtCore.SIGNAL("timeout()"), self.timerEvent)
        self.timer.start(1000)
        
    def timerEvent(self):
#        print "get message...."
        if self.p.empty():
            return
        head = self.p.get()
        if head == 1 :
            self.ui.radioButton_1.setChecked(True)
        elif head == 2 :
            self.ui.radioButton_2.setChecked(True)
        elif head == 3:
            self.ui.radioButton_3.setChecked(True)
        elif head == 4 :
            self.ui.radioButton_4.setChecked(True)
        elif head == 5 :
            self.ui.radioButton_5.setChecked(True)
        elif head == 6 :
            self.ui.radioButton_6.setChecked(True)
        elif head == 7 :
            self.ui.radioButton_7.setChecked(True)
        elif head == 8 :
            self.ui.radioButton_8.setChecked(True)
        elif head == 9 :
            self.ui.radioButton_9.setChecked(True)
        elif head == 10 :
            self.ui.radioButton_10.setChecked(True)
        elif head == 11 :
            self.ui.radioButton_11.setChecked(True)
        elif head == 12 :
            self.ui.radioButton_12.setChecked(True)
        elif head == 13 :
            self.ui.radioButton_13.setChecked(True)
        elif head == 14 :
            self.ui.radioButton_14.setChecked(True)
        elif head == 15 :
            self.ui.radioButton_15.setChecked(True)
        elif head == 16 :
            self.ui.radioButton_16.setChecked(True)
     
        
    def buttonConnect(self):
        self.ui.pushButtonTest.clicked.connect(self.buttonTest)
        self.ui.pushButtonReset.clicked.connect(self.buttonReset)
                         
    def buttonTest(self):
        self.data['fireBox'] = int(self.ui.lineEditBoxID.text())
        for i in range(16):
            self.data['firePoint'] = i+1
            dataPackage = dataPack(self.data)
            print repr(dataPackage.package)
            self.q.put (dataPackage.package)

    def buttonReset(self):
        self.ui.radioButton_1.setChecked(False)
        self.ui.radioButton_2.setChecked(False)
        self.ui.radioButton_3.setChecked(False)
        self.ui.radioButton_4.setChecked(False)
        self.ui.radioButton_5.setChecked(False)
        self.ui.radioButton_6.setChecked(False)
        self.ui.radioButton_7.setChecked(False)
        self.ui.radioButton_8.setChecked(False)
        self.ui.radioButton_9.setChecked(False)
        self.ui.radioButton_10.setChecked(False)
        self.ui.radioButton_11.setChecked(False)
        self.ui.radioButton_12.setChecked(False)
        self.ui.radioButton_13.setChecked(False)
        self.ui.radioButton_14.setChecked(False)
        self.ui.radioButton_15.setChecked(False)
        self.ui.radioButton_16.setChecked(False)
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    window = uiShow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()