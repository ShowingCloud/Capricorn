#coding=utf-8
'''
Created on 2013-2-22

@author: pyroshow
'''



from sqlalchemy import Column, Integer, Sequence, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


engine = create_engine("sqlite:///pyro.db")
session = scoped_session(sessionmaker(bind = engine, autocommit= True))
base = declarative_base() 

class Data(base):
    
    __tablename__ = "Fireworks"
    
    Id = Column(Integer, Sequence("session_id_seq"), primary_key = True)
    Type = Column(String)
    Item = Column(String)
    Description = Column(String)
    Size = Column(Integer)
    Stock = Column(Integer)
    Used_Effects = Column(Integer)
    Rising_Time = Column(Integer)
    Effect = Column(String)
    Color = Column(Integer)
    Angle = Column(Integer)
    Combination = Column(String)
    
    def __init__(self, Type = None, Item = None, Description = None, 
                 Size = None, Stock = None, Used_Effects = None, 
                 Rising_Time = None, Effect = None, Color = None, Angle = None, Combination = None):
        self.Type = Type
        self.Item = Item
        self.Description = Description
        self.Size = Size
        self.Stock = Stock
        self.Used_Effects = Used_Effects
        self.Rising_Time = Rising_Time
        self.Effect = Effect
        self.Color = Color
        self.Angle = Angle
        self.Combination = Combination



class Data1(base):
    
    __tablename__ = "CustomFireworks"
    
    Id = Column(Integer, Sequence("session_id_seq"), primary_key = True)
    Type = Column(String)
    Item = Column(String)
    Description = Column(String)
    Size = Column(Integer)
    Stock = Column(Integer)
    Used_Effects = Column(Integer)
    Rising_Time = Column(Integer)
    Effect = Column(String)
    Color = Column(String)
    Angle = Column(String)
    Combination = Column(String)
    
    def __init__(self, Type = None, Item = None, Description = None, 
                 Size = None, Stock = None, Used_Effects = None, 
                 Rising_Time = None, Effect = None, Color = None, Angle = None, Combination = None):
        self.Type = Type
        self.Item = Item
        self.Description = Description
        self.Size = Size
        self.Stock = Stock
        self.Used_Effects = Used_Effects
        self.Rising_Time = Rising_Time
        self.Effect = Effect
        self.Color = Color
        self.Angle = Angle
        self.Combination = Combination



