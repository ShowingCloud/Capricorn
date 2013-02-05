#coding=utf-8
'''
Created on 2013-2-4

@author: pyroshow

'''


import sys
from PySide import QtGui
import urllib
import xml.parsers.expat

#从网络获取XML资源文件


class MyXML:                                                #解析XML
    
    def __init__(self, edit):
        self.parser = xml.parsers.expat.ParserCreate()       #生成XMLParser
        self.parser.StartElementHandler = self.start         #起始标记处理方法
        self.parser.EndElementHandler = self.end             #起始标记处理方法
        self.parser.CharacterDataHandler = self.data         #起始标记处理方法
        
        
        
        self.title = False                                   #状态标志
        self.date = False                                    #状态标志
        self.edit = edit                                     #多行文本编辑框
        
        
    def start(self, name, attrs):                           # 起始标记处理方法
        
        if name == "title":                                 # 判断是否为title元素
            self.title = True                               #把标志设为真
            
        elif name == "pubDate":                             # 判断是否为pubDate元素
            self.date = True
            
        else:
            pass
        
        
    def end(self, name):                                    # 结束标记处理方法
        
        if name == "title":                                 # 判断是否为title元素
            self.title = False                              #把标志设为假
            
        elif name == "pubDate":                             # 判断是否为pubDate元素
            self.date = False
            
        else:
            pass
        
    def data(self, data):                                   #字符数据处理方法
        
        if self.title:
            self.edit.append('*'*90)
            self.edit.append('Title: '+data)
        
        elif self.date:
            self.edit.append("Date: "+data)
            
        else:
            pass
        
    def feed(self, data):
        self.parser.Parse(data, 0)
        
class Demo(QtGui.QWidget):
    
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        
        self.setWindowTitle("XML Test...")
        self.setGeometry(300, 300, 600, 400)
        
        self.button = QtGui.QPushButton(u"解析XML")
        self.edit = QtGui.QTextEdit()
        
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.edit)
        vbox.addWidget(self.button)
        self.setLayout(vbox)
        
        self.button.clicked.connect(self.startParse)
        
        
    def startParse(self):
        
        url = 'http://www.python.org/channews.rdf'          
        page = urllib.urlopen(url)                          #打开URL
        
        data = page.read()                                  #读取URL内容
        print data
        parser = MyXML(self.edit)                           #生成实例对象
        parser.feed(data)                                   #处理XML数据
        
        
            
app = QtGui.QApplication(sys.argv)
demo = Demo()
demo.show()
sys.exit(app.exec_())






