#coding=utf-8
'''
Created on 2013-3-28

@author: Pyroshow
'''
from PySide import QtCore
from Models.ProjectDB import *
from Models.LocalDB import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import *
from reportlab.lib import pagesizes, colors
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import *
from reportlab.pdfbase import *
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import json


TABLEFields, TABLEProductList, TABLEFireSequence = xrange (3)

class PrintTable(QtCore.QObject):
    def __init__ (self, sess, session, table, parent = None):
        QtCore.QObject.__init__ (self, parent)
        self.table = table
#        print self.tr('Bomb moment'), self.tr('Firework name'), self.tr('Size'), self.tr('Color'), self.tr('Direction'), self.tr('Ignite moment'), self.tr('Rising time'), self.tr('Effect duration'), self.tr('End time'), self.tr('Ignitor Box'), self.tr('Ignite point')
        
        import copy
        'C:\Windows\Fonts\simhei.ttf'
        pdfmetrics.registerFont(TTFont('song',os.path.join (appdata, 'local', 'simhei.ttf')))
        styles = getSampleStyleSheet()
        stylesSong= copy.deepcopy(styles['Normal'])
        stylesSong.fontName ='song'
        stylesSong.fontSize = 10
        a = []
        if self.table == TABLEFields:
            #self.tr('Bomb moment'), self.tr('Firework name'), self.tr('Size'), self.tr('Color'), self.tr('Direction'), self.tr('Ignite moment'), self.tr('Rising time'), self.tr('Effect duration'), self.tr('End time'), self.tr('Ignitor Box'), self.tr('Ignite point')]
            tableHead = [self.tr('Bomb moment'), self.tr('Firework name'), self.tr('Size'), self.tr('Color'), self.tr('Direction'), self.tr('Ignite moment'), self.tr('Rising time'), self.tr('Effect duration'), self.tr('End time'), self.tr('Ignitor Box'), self.tr('Ignite point')]
        elif self.table == TABLEProductList:
            tableHead = ['ItemNo','Size','Type','Name']
        elif self.table == TABLEFireSequence:
            tableHead = ['BoxID','IgnitionTime','FieldID','Name']
        else:
            return
        headList = []
        for head in tableHead:
            headList.append(Paragraph(head, stylesSong))
        a.append(headList)
        
        with session.begin():
            data = session.query(ProFireworksData).order_by(ProFireworksData.IgnitionTime).all()
            
        for row1 in data:
            bombTime = int(row1.Notes.split(',')[0]) + row1.IgnitionTime
            endTime = bombTime + int(row1.Notes.split(',')[0])+int(row1.Notes.split(',')[1])
#             with session.begin():
#                 row2 = session.query(IgnitorsData).filter_by(UUID = row1.IgnitorID).first()
#                 int.parse(row1.Notes.split(',')[0])#risingTime
#                 int.parse(row1.Notes.split(',')[1])#effectTime
            with sess.begin():
                row3 = sess.query(FireworksData).filter_by(UUID = row1.FireworkID).first()
                
            info = json.loads(row3.EffectsInfo)
#             info["EffectsInfo"][0][1]#Color
                
            b = []

            if self.table == TABLEFields:
                b.append(self.intToTimeFormat(bombTime))
                b.append(Paragraph(row3.Name, stylesSong))
                b.append(row3.Size)
                b.append(Paragraph(info["EffectsInfo"][0][1], stylesSong))
                b.append(row1.Direction)
                b.append(self.intToTimeFormat(row1.IgnitionTime))
                b.append(self.intToTimeFormat(int(row1.Notes.split(',')[0])))
                b.append(self.intToTimeFormat(int(row1.Notes.split(',')[1])))
                b.append(self.intToTimeFormat(endTime))
                b.append(row1.IgnitorID)
                b.append(row1.ConnectorID)
            elif self.table == TABLEProductList:
                b.append(row3.Type)
                b.append(row3.ItemNo)
                b.append(row3.Name)
                b.append(row3.Size)
#             elif self.table == TABLEFireSequence:
#                 b.append(row2.BoxID)
#                 b.append(row1.IgnitionTime)
#                 b.append(row3.Name)
#                 b.append(row2.FieldID)

            a.append(b)

        self.creatTable(styles,a)
        
        
    def intToTimeFormat(self,timeGet):
        displayTime = QtCore.QTime(timeGet / 3600000, (timeGet / 60000) % 60, (timeGet / 1000) % 60, timeGet % 1000)
        return displayTime.toString('h:mm:ss.z')
    
    def Pages(self,canvas,doc):
        canvas.saveState()
        canvas.drawString((doc.pagesize[0]/2)-5,25,u'%d'%(doc.page))
        canvas.restoreState()
    
    def creatTable(self,styles, data):

        elements = []
        if self.table == TABLEFields:
            
            doc = SimpleDocTemplate(os.path.join (appdata, 'pdf', 'Fireworks.pdf'), pagesize = pagesizes.A4)
            pwidth = (doc.pagesize[0] - 50) / 1000
            elements.append(Paragraph('Fireworks', styles['Title']))
            colwidths = (pwidth*110,pwidth*100,pwidth*80,pwidth*80,pwidth*80,pwidth*110,pwidth*110,pwidth*110,pwidth*110,pwidth*80,pwidth*80)
            
            table1 = Table(data, colwidths)
            table1.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                                   ('GRID',(0,0),(-1,-1),0.5,colors.black)]))
            
            elements.append(table1)
        
        elif self.table == TABLEProductList:
            doc = SimpleDocTemplate(os.path.join (appdata, 'pdf', 'ProductList.pdf'), pagesize = pagesizes.A4)
            pwidth = (doc.pagesize[0] - 20) / 1000
            elements.append(Paragraph('ProductList', styles['Title']))
            colwidths = (pwidth*120,pwidth*120,pwidth*120,pwidth*120)
            table2 = Table(data, colwidths)
            table2.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                                       ('GRID',(0,0),(-1,-1),0.5,colors.black)]))
            elements.append(table2)
        
        elif self.table == TABLEFireSequence:
            doc = SimpleDocTemplate(os.path.join (appdata, 'pdf', 'FireSequence.pdf'), pagesize = pagesizes.A4)
            pwidth = (doc.pagesize[0] - 20) / 1000
            elements.append(Paragraph('FireSequence', styles['Title']))
            colwidths = (pwidth*130,pwidth*130,pwidth*130,pwidth*130)
            table3 = Table(data, colwidths)
            table3.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                                       ('GRID',(0,0),(-1,-1),0.5,colors.black)]))
            elements.append(table3)

        else:
            return
    
        doc.build(elements,onFirstPage=self.Pages,onLaterPages=self.Pages)
    

# if __name__=='__main__':
#     ptable = PrintTable()
#     sess = session()
#     sess1 = session1()
#     base.metadata.create_all (engine)
#     base1.metadata.create_all (engine1)
#     
#     a1 = [['BoxID','ConnectorID','Size','RisingHeight','Name']]
#     a2 = [['ItemNo','Size','Type','Name']]
#     a3 = [['BoxID','IgnitionTime','FieldID','Name']]
#     
#     with sess1.begin():
#         data1 = sess1.query(ScriptData).all()
# 
#     for row1 in data1:
#         with sess1.begin():
#             row2 = sess1.query(IgnitorsData).filter_by(UUID = row1.IgnitorID).first()
#         with sess.begin():
#             row3 = sess.query(FireworksData).filter_by(UUID = row1.FireworkID).first()
#         
#         b1 = []        
#         b1.append(row2.BoxID)
#         b1.append(row3.RisingHeight)
#         b1.append(row3.Name)
#         b1.append(row3.Size)
#         b1.append(row1.ConnectorID)
#         a1.append(b1)
#         
#         b2 = []        
#         b2.append(row3.Type)
#         b2.append(row3.ItemNo)
#         b2.append(row3.Name)
#         b2.append(row3.Size)
#         a2.append(b2)
#         
#         b3 = []        
#         b3.append(row2.BoxID)
#         b3.append(row1.IgnitionTime)
#         b3.append(row3.Name)
#         b3.append(row2.FieldID)
#         a3.append(b3)
#         
#     ptable.creatTable(a1, a2, a3)
