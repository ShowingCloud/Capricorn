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

class PrintTable():
    def Pages(self,canvas,doc):
        canvas.saveState()
        canvas.drawString((doc.pagesize[0]/2)-5,25,u'%d'%(doc.page))
        canvas.restoreState()
    
    def creatTable(self, data1, data2, data3):
        elements = []
        styles = getSampleStyleSheet()
        doc = SimpleDocTemplate('H:/project.pdf', pagesize = pagesizes.A4)
        elements.append(Paragraph('Field', styles['Title']))
        pwidth = (doc.pagesize[0] - 20) / 1000
        colwidths = (pwidth*120,pwidth*120,pwidth*120,pwidth*120,pwidth*120)
       
        table1 = Table(data1, colwidths)
        table1.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                                   ('GRID',(0,0),(-1,-1),0.5,colors.black)]))
        elements.append(table1)
        
        elements.append(PageBreak())
        elements.append(Paragraph('ProductList', styles['Title']))
        colwidths = (pwidth*120,pwidth*120,pwidth*120,pwidth*120)
        table2 = Table(data2, colwidths)
        table2.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                                   ('GRID',(0,0),(-1,-1),0.5,colors.black)]))
        elements.append(table2)
        
        elements.append(PageBreak())
        elements.append(Paragraph('FireSequence', styles['Title']))
        colwidths = (pwidth*130,pwidth*130,pwidth*130,pwidth*130)
        table3 = Table(data3, colwidths)
        table3.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                                   ('GRID',(0,0),(-1,-1),0.5,colors.black)]))
        elements.append(table3)
    
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
