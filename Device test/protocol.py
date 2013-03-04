import struct
HEAD = 0xAAF0
FIRE_ON_TIME_SD = 0X01
FIRE_ON_TIME_BOX = 0XF1
FIRE_NOW = 0X02
CONNECT_TEST_SEND = 0X03
CONNECT_TEST_RECEIVE = 0X06
TIME_SYNC = 0X04
AUTO_PLAY = 0X05
def dataUnpack(package):
    datalist = [None]*14
    unpackDict = {'head':None,'length':None,'function':None,'ID':None,
                    'fireBox':None,'firePoint':None,'crc':None,'tail':None}
    
    fmt = '@14B'
    (datalist[0],datalist[1],datalist[2],datalist[3],datalist[4],datalist[5],
    datalist[6],datalist[7],datalist[8],datalist[9],datalist[10],datalist[11],
    datalist[12],datalist[13]) = struct.unpack(fmt,package)
    for node in datalist:
        print node
    if (datalist[2]*17+datalist[3]*16+datalist[4]*15+datalist[5]*14+
        datalist[6]*13+datalist[7]*12+datalist[8]*11+datalist[9]*10+
        datalist[10]*9+datalist[11]*8+datalist[12])%18 != 0 :
        print 'data damaged'
        return None
    else:
        unpackDict['head'] = datalist[0]*0x100+datalist[1]
        unpackDict['length'] = datalist[2]
        unpackDict['function'] = datalist[3]
        unpackDict['ID'] = datalist[4]*0x1000000+datalist[5]*0x10000+datalist[6]*0x100+datalist[7]
        unpackDict['fireBox'] = datalist[8]*0x100+datalist[9]
        unpackDict['firePoint'] = datalist[10]*0x100+datalist[11]
        unpackDict['crc'] = datalist[12]
        unpackDict['tail'] = datalist[13]
        for key in unpackDict:
            print 'unpackDict[%s] = %d'%(key,unpackDict[key])
        return unpackDict

    
class dataPack():
    def getList(self):
        self.dataList = [None]*self.data['length']
        if self.data['function'] == FIRE_ON_TIME_BOX or self.data['function'] ==  FIRE_ON_TIME_SD:
            self.dataList[0] = self.data['head']/0x100
            self.dataList[1] = self.data['head']%0x100
            self.dataList[2] = self.data['length']
            self.dataList[3] = self.data['function']
            self.dataList[4] = self.data['ID']/0x1000000
            self.dataList[5] = (self.data['ID']%0x1000000)/0x10000
            self.dataList[6] = (self.data['ID']%0x10000)/0x100
            self.dataList[7] = self.data['ID']%0x100
            self.dataList[8] = self.data['fireBox']/0x100
            self.dataList[9] = self.data['fireBox']%0x100
            self.dataList[10] = self.data['firePoint']/0x100
            self.dataList[11] = self.data['firePoint']%0x100
            self.dataList[12] = self.data['seconds']/0x1000000
            self.dataList[13] = (self.data['seconds']%0x1000000)/0x10000
            self.dataList[14] = (self.data['seconds']%0x10000)/0x100
            self.dataList[15] = self.data['seconds']%0x100
            self.dataList[16] = self.data['offsetSec']/0x100
            self.dataList[17] = self.data['offsetSec']%0x100
            self.dataList[18] = self.data['crc']
            self.dataList[19] = self.data['tail']

        elif self.data['function'] == FIRE_NOW or self.data['function'] == CONNECT_TEST_SEND:
            self.dataList[0] = self.data['head']/0x100
            self.dataList[1] = self.data['head']%0x100
            self.dataList[2] = self.data['length']
            self.dataList[3] = self.data['function']
            self.dataList[4] = self.data['ID']/0x1000000
            self.dataList[5] = (self.data['ID']%0x1000000)/0x10000
            self.dataList[6] = (self.data['ID']%0x10000)/0x100
            self.dataList[7] = self.data['ID']%0x100
            self.dataList[8] = self.data['fireBox']/0x100
            self.dataList[9] = self.data['fireBox']%0x100
            self.dataList[10] = self.data['firePoint']/0x100
            self.dataList[11] = self.data['firePoint']%0x100
            self.dataList[12] = self.data['crc']
            self.dataList[13] = self.data['tail']
            
            
        elif self.data['function'] == TIME_SYNC:
            self.dataList[0] = self.data['head']/0x100
            self.dataList[1] = self.data['head']%0x100
            self.dataList[2] = self.data['length']
            self.dataList[3] = self.data['function']
            self.dataList[4] = self.data['seconds']/0x1000000
            self.dataList[5] = (self.data['seconds']%0x1000000)/0x10000
            self.dataList[6] = (self.data['seconds']%0x10000)/0x100
            self.dataList[7] = self.data['seconds']%0x100
            self.dataList[8] = self.data['crc']
            self.dataList[9] = self.data['tail']
            
        elif self.data['function'] == AUTO_PLAY:
            self.dataList[0] = self.data['head']/0x100
            self.dataList[1] = self.data['head']%0x100
            self.dataList[2] = self.data['length']
            self.dataList[3] = self.data['function']
            self.dataList[4] = self.data['crc']
            self.dataList[5] = self.data['tail']
        
    def getCRC(self):
        if self.data['function'] ==  FIRE_ON_TIME_SD or self.data['function'] == FIRE_ON_TIME_BOX:
            self.data['crc']=18-(17*self.dataList[2]+16*self.dataList[3]+15*self.dataList[4]+
                             14*self.dataList[5]+13*self.dataList[6]+12*self.dataList[7]+
                             11*self.dataList[8]+10*self.dataList[9]+9*self.dataList[10]+
                             8*self.dataList[11]+7*self.dataList[12]+6*self.dataList[13]+
                             5*self.dataList[14]+4*self.dataList[15]+3*self.dataList[16]+
                             2*self.dataList[17])%18

        elif self.data['function'] == FIRE_NOW or self.data['function'] == CONNECT_TEST_SEND:
            self.data['crc']=18-(17*self.dataList[2]+16*self.dataList[3]+15*self.dataList[4]+
                             14*self.dataList[5]+13*self.dataList[6]+12*self.dataList[7]+
                             11*self.dataList[8]+10*self.dataList[9]+9*self.dataList[10]+
                             8*self.dataList[11])%18

        elif self.data['function'] == TIME_SYNC:
            self.data['crc']=18-(17*self.dataList[2]+16*self.dataList[3]+15*self.dataList[4]+
                             14*self.dataList[5]+13*self.dataList[6]+12*self.dataList[7])%18
        
        elif self.data['function'] == AUTO_PLAY:
            self.data['crc']=18-(17*self.dataList[2]+16*self.dataList[3])%18
            
        self.dataList[self.data['length']-2] = self.data['crc']
        

    
    def __init__(self,data):
        self.data = data
        self.getList()
        self.getCRC()
        
    def pack(self):
        fmt = '@'+str(self.data['length'])+'B'
        
        if self.data['function'] ==  FIRE_ON_TIME_SD or self.data['function'] == FIRE_ON_TIME_BOX:
            self.package = struct.pack(fmt,self.dataList[0],self.dataList[1],self.dataList[2],
                                       self.dataList[3],self.dataList[4],self.dataList[5],
                                       self.dataList[6],self.dataList[7],self.dataList[8],
                                       self.dataList[9],self.dataList[10],self.dataList[11],
                                       self.dataList[12],self.dataList[13],self.dataList[14],
                                       self.dataList[15],self.dataList[16],self.dataList[17],
                                       self.dataList[18],self.dataList[19])

        elif self.data['function'] == FIRE_NOW or self.data['function'] == CONNECT_TEST_SEND:
            self.package = struct.pack(fmt,self.dataList[0],self.dataList[1],self.dataList[2],
                                       self.dataList[3],self.dataList[4],self.dataList[5],
                                       self.dataList[6],self.dataList[7],self.dataList[8],
                                       self.dataList[9],self.dataList[10],self.dataList[11],
                                       self.dataList[12],self.dataList[13])
            
        elif self.data['function'] == TIME_SYNC:
            self.package = struct.pack(fmt,self.dataList[0],self.dataList[1],self.dataList[2],
                                       self.dataList[3],self.dataList[4],self.dataList[5],
                                       self.dataList[6],self.dataList[7],self.dataList[8],
                                       self.dataList[9])
        
        elif self.data['function'] == AUTO_PLAY:
            self.package = struct.pack(fmt,self.dataList[0],self.dataList[1],self.dataList[2],
                                       self.dataList[3],self.dataList[4],self.dataList[5])
        print repr(self.package)



def main():
    data = {'head':0xAAF0,'length':0x0e,'function':FIRE_NOW,'ID':0xAABBCCDD,
            'fireBox':0xAABB,'firePoint':0xCCDa,'seconds':0xAABBCCDD,
            'offsetSec':0xAABa,'crc':0,'tail':0xDD}
    for key in data:
        print 'data[%s] = %X'%(key,data[key])
    test = dataPack(data)
    test.pack()
    dataUnpack(test.package)
    
if __name__=='__main__':
    main()
