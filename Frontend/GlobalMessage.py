#coding=utf-8
'''
Created on 2013-10-8

@author: YuJin
'''

class GlobalMessage:
    dicEnglish = {}
        
    @staticmethod
    def messageDisplayEn():
        GlobalMessage.dicEnglish.setdefault(u'白色', 'White')
        GlobalMessage.dicEnglish.setdefault(u'黑色', 'Black')
        GlobalMessage.dicEnglish.setdefault(u'红色', 'Red')
        GlobalMessage.dicEnglish.setdefault(u'蓝色', 'Blue')
        GlobalMessage.dicEnglish.setdefault(u'绿色', 'Green')
        GlobalMessage.dicEnglish.setdefault(u'蓝绿色', 'Cyan')
        GlobalMessage.dicEnglish.setdefault(u'洋红色', 'Magenta')
        GlobalMessage.dicEnglish.setdefault(u'黄色', 'Yellow')
        GlobalMessage.dicEnglish.setdefault(u'灰色', 'Gray')
        
class MessageDisplay:
    @staticmethod
    def getMessage(dicKey):
        GlobalMessage.messageDisplayEn()
        return GlobalMessage.dicEnglish[dicKey]
        
