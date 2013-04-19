'''
Created on 2013-3-28

@author: Pyroshow
'''
from Models.EngineeringDB import *
from Models.LocalDB import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import *
from reportlab.lib import pagesizes, colors
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import *
from reportlab.pdfbase import *

TABLEFields, TABLEProductList, TABLEFireSequence = xrange (3)

class PrintTable():
    def __init__ (self, sess, session, table, parent = None):
        self.table = table

        if self.table == TABLEFields:
            a = [['BoxID','ConnectorID','Size','RisingHeight','Name']]
        elif self.table == TABLEProductList:
            a = [['ItemNo','Size','Type','Name']]
        elif self.table == TABLEFireSequence:
            a = [['BoxID','IgnitionTime','FieldID','Name']]
        else:
            return

        with session.begin():
            data = session.query(ScriptData).all()

        for row1 in data:
            with session.begin():
                row2 = session.query(IgnitorsData).filter_by(UUID = row1.IgnitorID).first()
            with sess.begin():
                row3 = sess.query(FireworksData).filter_by(UUID = row1.FireworkID).first()

            b = []

            if self.table == TABLEFields:
                b.append(row2.BoxID)
                b.append(row3.RisingHeight)
                b.append(row3.Name)
                b.append(row3.Size)
                b.append(row1.ConnectorID)
            elif self.table == TABLEProductList:
                b.append(row3.Type)
                b.append(row3.ItemNo)
                b.append(row3.Name)
                b.append(row3.Size)
            elif self.table == TABLEFireSequence:
                b.append(row2.BoxID)
                b.append(row1.IgnitionTime)
                b.append(row3.Name)
                b.append(row2.FieldID)

            a.append(b)

        self.creatTable(a)

    def Pages(self,canvas,doc):
        canvas.saveState()
        canvas.drawString((doc.pagesize[0]/2)-5,25,u'%d'%(doc.page))
        canvas.restoreState()
    
    def creatTable(self, data):
        elements = []
        styles = getSampleStyleSheet()


        if self.table == TABLEFields:
            doc = SimpleDocTemplate(os.path.join (appdata, 'pdf', 'Fields.pdf'), pagesize = pagesizes.A4)
            pwidth = (doc.pagesize[0] - 20) / 1000
            elements.append(Paragraph('Field', styles['Title']))
            colwidths = (pwidth*120,pwidth*120,pwidth*120,pwidth*120,pwidth*120)
       
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
    

if __name__=='__main__':
    ptable = PrintTable()
    sess = session()
    sess1 = session1()
    base.metadata.create_all (engine)
    base1.metadata.create_all (engine1)
    
    a1 = [['BoxID','ConnectorID','Size','RisingHeight','Name']]
    a2 = [['ItemNo','Size','Type','Name']]
    a3 = [['BoxID','IgnitionTime','FieldID','Name']]
    
    with sess1.begin():
        data1 = sess1.query(ScriptData).all()

    for row1 in data1:
        with sess1.begin():
            row2 = sess1.query(IgnitorsData).filter_by(UUID = row1.IgnitorID).first()
        with sess.begin():
            row3 = sess.query(FireworksData).filter_by(UUID = row1.FireworkID).first()
        
        b1 = []        
        b1.append(row2.BoxID)
        b1.append(row3.RisingHeight)
        b1.append(row3.Name)
        b1.append(row3.Size)
        b1.append(row1.ConnectorID)
        a1.append(b1)
        
        b2 = []        
        b2.append(row3.Type)
        b2.append(row3.ItemNo)
        b2.append(row3.Name)
        b2.append(row3.Size)
        a2.append(b2)
        
        b3 = []        
        b3.append(row2.BoxID)
        b3.append(row1.IgnitionTime)
        b3.append(row3.Name)
        b3.append(row2.FieldID)
        a3.append(b3)
        
    ptable.creatTable(a1, a2, a3)
