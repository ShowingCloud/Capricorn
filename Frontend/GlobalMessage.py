#coding=utf-8
'''
Created on 2013-10-8

@author: YuJin
'''

class GlobalMessage:
    dicEnglish = {}
    
    @staticmethod
    def messageDisplayEn():
        GlobalMessage.dicEnglish.setdefault('a', 'a')
        GlobalMessage.dicEnglish.setdefault('b', 'b')
        GlobalMessage.dicEnglish.setdefault('c', 'c')
        GlobalMessage.dicEnglish.setdefault('d', 'd')
        
class MessageDisplay:
    @staticmethod
    def getMessage(dicKey):
        GlobalMessage.messageDisplayEn()
        return GlobalMessage.dicEnglish[dicKey]
        
