#coding=utf-8
'''
Created on 2013-10-8

@author: YuJin
'''

class GlobalMessage:
    dicEnglish = {}
        
    @staticmethod
    def messageDisplayEn():
        GlobalMessage.dicEnglish.setdefault(u'��ɫ', 'White')
        GlobalMessage.dicEnglish.setdefault(u'��ɫ', 'Black')
        GlobalMessage.dicEnglish.setdefault(u'��ɫ', 'Red')
        GlobalMessage.dicEnglish.setdefault(u'��ɫ', 'Blue')
        GlobalMessage.dicEnglish.setdefault(u'��ɫ', 'Green')
        GlobalMessage.dicEnglish.setdefault(u'����ɫ', 'Cyan')
        GlobalMessage.dicEnglish.setdefault(u'���ɫ', 'Magenta')
        GlobalMessage.dicEnglish.setdefault(u'��ɫ', 'Yellow')
        GlobalMessage.dicEnglish.setdefault(u'��ɫ', 'Gray')
        
class MessageDisplay:
    @staticmethod
    def getMessage(dicKey):
        GlobalMessage.messageDisplayEn()
        return GlobalMessage.dicEnglish[dicKey]
        
