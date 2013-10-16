#coding=utf-8
'''
Created on 2013-10-9

@author: YuJin
'''
from Models.ProjectDB import ProFireworksData, proSession
import uuid
from datetime import datetime

class FireworksEO(object):
    
    def __init__(self):
        self.session = proSession()
        
    def insert(self, data):
        with self.session.begin():
            record = ProFireworksData()
            record.UUID = str(uuid.uuid1())
            record.CTime = datetime.utcnow()
            record.MTime = datetime.utcnow()
            record.FireworkID = data['FireworkID']
            record.IgnitionTime = data['IgnitionTime']
            record.IgnitorID = data['IgnitorID']
            record.ConnectorID = data['ConnectorID']
            record.Notes = data['Notes']
            self.session.add(record)
            
    def query(self):
        with self.session.begin():
            records = self.session.query(ProFireworksData).all()
        return records
    
    def queryByUUID(self, UUID):
        with self.session.begin():
            record = self.session.query(ProFireworksData).filter_by(UUID == UUID).first()
        return record
    
    def update(self, UUID):
        with self.session.begin():
            record = self.session.query(ProFireworksData).filter_by(UUID == UUID).first()
            
    def deleteByUUID(self, UUID):
        with self.session.begin():
            record = self.session.query(ProFireworksData).filter_by(UUID == UUID).first()
            self.session.delete(record)
