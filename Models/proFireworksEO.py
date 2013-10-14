#coding=utf-8
'''
Created on 2013-10-9

@author: YuJin
'''
from Models.ProjectDB import ProFireworksData, proSession

class FireworksEO:
    session = proSession()
    def insert(self, data):
        with FireworksEO.session.begin():
            record = ProFireworksData()
            
            FireworksEO.session.add(record)
    def query(self):
        with FireworksEO.session.begin():
            record = FireworksEO.session.query(ProFireworksData)
        return record
    
