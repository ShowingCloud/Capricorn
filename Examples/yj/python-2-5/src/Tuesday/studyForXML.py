#coding=utf-8
'''
Created on 2013-2-5

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
        
        
        
        self.id = False                                       #状态标志
        self.name = False                                       #状态标志
        self.age = False                                       #状态标志
        self.sex = False                                       #状态标志
        self.edit = edit                                     #多行文本编辑框
        
        
    def start(self, name, attrs):                           # 起始标记处理方法
        
        if name == "student":                                 # 判断是否为student元素
            self.edit.append('*'*90)
            self.edit.append(" "*40+'Student')
        if name == "id":                             # 判断是否为id元素
            self.id = True
        elif name == "name":                             # 判断是否为name元素
            self.name = True
        elif name == "age":                             # 判断是否为age元素
            self.age = True
        elif name == "sex":                             # 判断是否为sex元素
            self.sex = True
            
        else:
            pass
        
        
    def end(self, name):                                    # 结束标记处理方法
        
        if name == "id":                             # 判断是否为id元素
            self.id = False
        elif name == "name":                             # 判断是否为name元素
            self.name = False
        elif name == "age":                             # 判断是否为age元素
            self.age = False
        elif name == "sex":                             # 判断是否为sex元素
            self.sex = False
            
        else:
            pass
        
    def data(self, data):                                   #字符数据处理方法
        
        if self.id:
            self.edit.append("Id: "+data)
        elif self.name:
            self.edit.append("Name: "+data)
        elif self.age:
            self.edit.append("Age: "+data)
        elif self.sex:
            self.edit.append("Sex: "+data)
            
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
        #从网络读取数据
#        url = 'http://www.python.org/channews.rdf'          
#        page = urllib.urlopen(url)                          #打开URL
#        
#        data = page.read()                                  #读取URL内容
#        print data
        #从本地读取文件
        f = open("stu.xml", "r").read()
        print f
        parser = MyXML(self.edit)                           #生成实例对象
        parser.feed(f)                                   #处理XML数据
        
        
            
app = QtGui.QApplication(sys.argv)
demo = Demo()
demo.show()
sys.exit(app.exec_())






















