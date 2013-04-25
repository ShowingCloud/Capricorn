#coding=utf-8
'''
Created on 2013-3-4

@author: pyroshow
'''
from sqlalchemy import Column, Integer, Sequence, String, DateTime,Interval, Text , Boolean
#    create_engine
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import sessionmaker, scoped_session

#工程数据库
#engine = create_engine("sqlite:///engineering.db")
#session = scoped_session(sessionmaker(bind = engine, autocommit = True))
base1 = declarative_base()



#工程烟花库表        
class ScriptData(base1):
    
    __tablename__ = "Fireworks"
    
    ID = Column(Integer, Sequence("session_id_seq"), primary_key = True)
    UUID = Column(String, nullable = False, unique = True)    #
    FieldID = Column(String)                    #阵地号，（自定义的）
    CTime = Column(DateTime )                  #input time
    MTime = Column(DateTime )                  #modification time
    IgnitionTime = Column(Interval)            #点火时间
    FireworkID = Column(String)                 #对应每条烟花数据库里面的UUID
    IgnitorID = Column(String)                 #点火器
    ConnectorID = Column(Integer)              #连接器
    Location = Column(String)                   #坐标，对应地图 
    Angle  = Column(Integer)                    #角度
    Notes = Column(Text)                 #用户自定义字段，类型待定
    
    def __init__(self, UUID = None, FieldID = None, CTime = None, MTime = None, IgnitionTime = None, FireworkID = None, 
                 IgnitorID = None, ConnectorID = None, Location = None, Angle = 0, Notes = None):
        
        self.UUID = UUID
        self.FieldID = FieldID
        self.CTime = CTime
        self.MTime = MTime
        self.IgnitionTime = IgnitionTime
        self.FireworkID = FireworkID
        self.IgnitorID = IgnitorID
        self.ConnectorID = ConnectorID
        self.Location = Location
        self.Angle = Angle
        self.Notes = Notes 
        
        
        
#包括点火盒及从机表        
class IgnitorsData(base1):
    
    __tablename__ = "Ignitors"
    
    ID = Column(Integer, Sequence("session_id_seq"), primary_key = True)
    UUID = Column(String, nullable = False, unique = True)    #
    CTime = Column(DateTime )                  #input time
    MTime = Column(DateTime )                  #modification time
    IgnitorID = Column(String)                 #点火器
    FieldID = Column(String)                   #阵地号
    BoxID = Column(Integer)                   #点火盒号
    TotalHeads = Column(Integer)                   #阵地号
    SurplusHeads = Column(Integer)                   #阵地号
    Notes = Column(Text)                 #用户自定义字段，类型待定
    
    def __init__(self, UUID = None, CTime = None, MTime = None, IgnitorID = None, FieldID = None, 
                 BoxID = None, TotalHeads = None, SurplusHeads = None,Notes = None):
        
        self.UUID = UUID
        self.CTime = CTime
        self.MTime = MTime
        self.IgnitorID = IgnitorID
        self.FieldID = FieldID
        self.BoxID = BoxID
        self.TotalHeads = TotalHeads
        self.SurplusHeads = SurplusHeads
        self.Notes = Notes
        
#工程阵地表        
class FieldsData(base1):
    
    __tablename__ = "Fields"
    
    ID = Column(Integer, Sequence("session_id_seq"), primary_key = True)
    UUID = Column(String, nullable = False, unique = True)    #
    CTime = Column(DateTime )                  #input time
    MTime = Column(DateTime )                  #modification time
    FieldID = Column(String)                   #阵地号 和编辑里面的阵地相对应
    Parent = Column(Integer)                   #父场景号
    Notes = Column(Text)                 #用户自定义字段，类型待定
    
    def __init__(self, UUID = None, CTime = None, MTime = None, FieldID = None, Parent = None, Notes = None):
        
        self.UUID = UUID
        self.CTime = CTime
        self.MTime = MTime
        self.FieldID = FieldID
        self.Parent = Parent
        self.Notes = Notes
        
        
        
#建筑表        
class ScenesData(base1):
    
    __tablename__ = "Scenes"
    
    ID = Column(Integer, Sequence("session_id_seq"), primary_key = True)
    UUID = Column(String, nullable = False, unique = True)    #
    CTime = Column(DateTime )                  #input time
    MTime = Column(DateTime )                  #modification time
    SceneID = Column(Integer)                   #使用的建筑ID
    FieldList = Column(Integer)                   #选择使用的阵地列表（建筑内），包含Field号(类型待定)
    Location = Column(String)                   #坐标（可覆盖原始设置）
    Notes = Column(Text)                 #用户自定义字段，类型待定
    
    def __init__(self, UUID = None, CTime = None, MTime = None, SceneID = None, FieldList = None, Location = None, Notes = None):
        
        self.UUID = UUID
        self.CTime = CTime
        self.MTime = MTime
        self.SceneID = SceneID
        self.FieldList = FieldList
        self.Location = Location
        self.Notes = Notes
        
        
        
#工程属性表        
class ParametersData(base1):
    
    __tablename__ = "Parameters"
    
    ID = Column(Integer, Sequence("session_id_seq"), primary_key = True)
    CTime = Column(DateTime )                  #input time
    MTime = Column(DateTime )                  #modification time
    SceneID = Column(Integer)                   #使用的建筑ID
    FieldList = Column(Integer)                   #选择使用的阵地列表（建筑内），包含Field号(类型待定)
    Notes = Column(Text)                 #用户自定义字段，类型待定
    
    def __init__(self, CTime = None, MTime = None, SceneID = None, FieldList = None, Notes = None):
        
        self.CTime = CTime
        self.MTime = MTime
        self.SceneID = SceneID
        self.FieldList = FieldList
        self.Notes = Notes
 



