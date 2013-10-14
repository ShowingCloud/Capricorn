#!/usr/bin/python
#_*_encoding:utf-8_*_

#LocalDB.py

from sqlalchemy import Column, Integer, Sequence, String, create_engine, \
    DateTime, Interval, Text, Boolean, Float, Date, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

#本地数据库
##engine = create_engine("sqlite:///" + os.path.join (appdata, 'local', 'local.db'))
engine = create_engine("sqlite:///local.db")
session = scoped_session(sessionmaker(bind = engine, autocommit = True))
meta = MetaData()
base = declarative_base(metadata=meta)


#烟火库表
class FireworksData(base):
    
    __tablename__ = "Fireworks"
    
    ID = Column(Integer, Sequence("session_id_seq"), primary_key = True)
    UUID = Column(String, nullable = False, unique = True)    #
    CTime = Column(DateTime )                  #input time
    MTime = Column(DateTime )                  #modification time
    Type = Column(String)
    Name = Column(String)
    Alias = Column(String)
    Description = Column(String)
    Picture = Column(String)                   #类型待定(外链)
    Animation = Column(String)                 #类型待定(外链)
    Model = Column(String)                     #类型待定(外链)
    SoundEffect = Column(String)               #类型待定(外链)
    Size = Column(Float, nullable = False)   #尺寸(暂定英尺in)数据库里面为mm毫米
    UsedEffects = Column(Integer)              #燃放的几种效果暂定只有3种，后续可能会有第四种，单位为piece（块，件）
    Min = Column(Integer)                      #单位为piece（块，件）,不知道啥意思
    Best = Column(Integer)                     #单位为piece（块，件），不知道啥意思
    EffectsInfo = Column(Text)                 #主要包括color，effect， duration(单位用ms)(字典的形式)
    Combination = Column(Text)                 #组合烟花主要包括name，time(单位用ms)(字典的形式)
    Shots = Column(Integer)
    Indoor = Column(Boolean)                   #用0,1表示在室内或者室外
    RisingTime = Column(Integer)               #单位用ms(毫秒)
    RisingHeight = Column(Integer)             #单位用m（米）上升高度
    Diameter = Column(Integer)                 #单位用m（米）炸开的直径
    Class = Column(String)                    #品种等级，类型待定
    BAMNumber = Column(String)                #不清楚
    ADRClass = Column(String)                 #药量等级，类型待定
    UNNumber = Column(String)                 #不清楚
    Chipher = Column(Integer)                  #不清楚
    WeightNet = Column(Float)                #产品净重，单位k(克)
    WeightGross = Column(Float)              #产品毛重，单位k(克)
    SDHorizontal = Column(Integer)              #水平安全观看距离，单位m(米)
    SDVertical = Column(Integer)              #水平垂直观看距离，单位m(米)
    EffectID = Column(String)              #不清楚，类型待定（燃放的编号）
    Rating = Column(String)              #不清楚，类型待定(燃放成功效率)
    Information = Column(String)              
    Supplier = Column(String)              #供应厂商
    Producer = Column(String)              #生产者
    ItemNo = Column(String)                #产品编号
    Stock = Column(Integer)                #库存
    StockPlace = Column(String)           #库存地
    Price = Column(Float)                #价格，单位待定
    CalcFactor = Column(Float)           #不清楚，类型待定
    Notes = Column(Text)                 #用户自定义字段，类型待定
    Perm = Column(Integer)                 #0为私有，1为公有，其余均为权限号
    Owner = Column(String)                 #所有者用户ID
    
    CUser = Column(String)              #创建人
    MUser = Column(String)              #修改人
    
    def __init__(self, UUID = None, CTime = None, MTime = None,
                 Type = None, Name = None, Alias = None, Description = None, Picture = None, 
                 Animation = None, Model = None, SoundEffect = None, Size = None, 
                 UsedEffects = None, Min = None, Best = None, EffectsInfo = None, Combination = None,  
                 Shots = None, Indoor = None, RisingTime = None, RisingHeight = None, 
                 Diameter = None, Class = None, BAMNumber = None, ADRClass = None, 
                 UNNumber = None, Chipher = None, WeightNet = None, WeightGross = None, 
                 SDHorizontal = None, SDVertical = None, EffectID = None, Rating = None, 
                 Information = None, Supplier = None, Producer = None, ItemNo = None, Stock = None, 
                 StockPlace = None, Price = None, CalcFactor = None, Notes = None, Perm = None, Owner = None, CUser = None, MUser = None):
        
        self.UUID = UUID
        self.CTime = CTime
        self.MTime = MTime
        self.Type = Type
        self.Name = Name
        self.Alias = Alias
        self.Description = Description
        self.Picture = Picture
        self.Animation = Animation
        self.Model = Model
        self.SoundEffect = SoundEffect
        self.Size = Size
        self.UsedEffects = UsedEffects
        self.Min = Min
        self.Best = Best
        self.EffectsInfo = EffectsInfo
        self.Combination = Combination
        self.Shots = Shots
        self.Indoor = Indoor
        self.RisingTime = RisingTime
        self.RisingHeight = RisingHeight
        self.Diameter = Diameter
        self.Class = Class
        self.BAMNumber = BAMNumber
        self.ADRClass = ADRClass
        self.UNNumber = UNNumber
        self.Chipher = Chipher
        self.WeightNet = WeightNet 
        self.WeightGross = WeightGross 
        self.SDHorizontal = SDHorizontal 
        self.SDVertical = SDVertical 
        self.EffectID = EffectID 
        self.Rating = Rating 
        self.Information = Information 
        self.Supplier = Supplier 
        self.Producer = Producer 
        self.ItemNo = ItemNo 
        self.Stock = Stock 
        self.StockPlace = StockPlace 
        self.Price = Price 
        self.CalcFactor = CalcFactor 
        self.Notes = Notes 
        self.Perm = Perm 
        self.Owner = Owner 
        self.CUser = CUser
        self.MUser = MUser
        
        
#场景库表        
class ScenesData(base):
    
    __tablename__ = "Scenes"
    
    ID = Column(Integer, Sequence("session_id_seq"), primary_key = True)
    UUID = Column(String, nullable = False, unique = True)    #
    CTime = Column(DateTime )                  #input time
    MTime = Column(DateTime )                  #modification time
    Type = Column(String)                   #场景类型
    Name = Column(String)
    Description = Column(String)
    Picture = Column(String)                   #类型待定(外链)
    Animation = Column(String)                 #类型待定(外链)
    Model = Column(String)                     #类型待定(外链)
    Location = Column(String)                   #坐标，对应地图 
    Direction =  Column(String)                #主席台方向
    ParentScenes = Column(String)               #父场景的UUID，场景中有父场景概念，两级结构，子场景可以找到父场景，父场景不在有上一级场景。
    Area  = Column(Integer, nullable = False)   #面积
    FieldList = Column(Text)                  #不清楚，类型待定,阵地链
    Restriction = Column(String)               #约束,不知道啥意思
    Information = Column(String)              
    Notes = Column(Text)                 #用户自定义字段，类型待定
    Perm = Column(Integer)                 #0为私有，1为公有，其余均为权限号
    Owner = Column(String)                 #所有者用户ID
    
    CUser = Column(String)              #创建人
    MUser = Column(String)              #修改人
    
    def __init__(self, UUID = None, CTime = None, MTime = None,
                 Type = None, Name = None, Description = None, Picture = None, ParentScenes = None, 
                 Animation = None, Model = None, Location = None, Area = None, Direction = None, 
                 FieldList = None, Restriction = None,Information = None, Notes = None, Perm = None, Owner = None,  
                 CUser = None, MUser = None):
        
        self.UUID = UUID
        self.CTime = CTime
        self.MTime = MTime
        self.Type = Type
        self.Name = Name
        self.Description = Description
        self.Picture = Picture
        self.Animation = Animation
        self.Model = Model
        self.Location = Location
        self.Area = Area
        self.FieldList = FieldList
        self.Restriction = Restriction
        self.Information = Information 
        self.Notes = Notes 
        self.Perm = Perm 
        self.Owner = Owner 
        self.Direction = Direction
        self.CUser = CUser
        self.MUser = MUser
        self.ParentScenes = ParentScenes
        
        
#音乐库表        
class MusicData(base):
    
    __tablename__ = "Music"
    
    ID = Column(Integer, Sequence("session_id_seq"), primary_key = True)
    UUID = Column(String, nullable = False, unique = True)    #
    CTime = Column(DateTime )                  #input time
    MTime = Column(DateTime )                  #modification time
    Type = Column(String)                   #阵地、建筑及其它 
    Name = Column(String)
    Description = Column(String)
    Picture = Column(String)                   #类型待定(外链)
    Duration = Column(Integer)                 #类型待定, 播放时间
    File = Column(String)                     #类型待定(外链),原格式文件
    FileWav = Column(String)                     #类型待定(外链),Wave格式文件 
    ProjectID  = Column(Integer, nullable = False)   #关联的烟花工程 
    Information = Column(String)              
    Notes = Column(Text)                 #用户自定义字段，类型待定
    Perm = Column(Integer)                 #0为私有，1为公有，其余均为权限号
    Owner = Column(String)                 #所有者用户ID
    
    CUser = Column(String)              #创建人
    MUser = Column(String)              #修改人
    
    def __init__(self, UUID = None, CTime = None, MTime = None,
                 Type = None, Name = None, Description = None, Picture = None, 
                 Duration = None, File = None, FileWav = None, ProjectID = None, 
                 Information = None, Notes = None, Perm = None, Owner = None, CUser = None, MUser = None):
        
        self.UUID = UUID
        self.CTime = CTime
        self.MTime = MTime
        self.Type = Type
        self.Name = Name
        self.Description = Description
        self.Picture = Picture
        self.Duration = Duration
        self.File = File
        self.FileWav = FileWav
        self.ProjectID = ProjectID
        self.Information = Information 
        self.Notes = Notes 
        self.Perm = Perm 
        self.Owner = Owner 
        
        self.CUser = CUser
        self.MUser = MUser
        

#点火器表        
class IgnitorsData(base):
    
    __tablename__ = "Ignitors"
    
    ID = Column(Integer, Sequence("session_id_seq"), primary_key = True)
    UUID = Column(String, nullable = False, unique = True)    #
    CTime = Column(DateTime )                  #input time
    MTime = Column(DateTime )                  #modification time
    Name = Column(String)
    Description = Column(String)
    Picture = Column(String)                   #类型待定(外链)
    Animation = Column(String)                 #类型待定(外链)
    Model = Column(String)                     #类型待定(外链)
    Heads = Column(Integer)                   #点火器头
    Restriction = Column(String)               #约束,不知道啥意思
    Information = Column(String)              
    Notes = Column(Text)                 #用户自定义字段，类型待定
    
    CUser = Column(String)              #创建人
    MUser = Column(String)              #修改人
    
    def __init__(self, UUID = None, CTime = None, MTime = None, Name = None, Description = None, Picture = None, 
                 Animation = None, Model = None, Heads = None, Restriction = None,Information = None, Notes = None, CUser = None, MUser = None):
        
        self.UUID = UUID
        self.CTime = CTime
        self.MTime = MTime
        self.Name = Name
        self.Description = Description
        self.Picture = Picture
        self.Animation = Animation
        self.Model = Model
        self.Heads = Heads
        self.Restriction = Restriction
        self.Information = Information 
        self.Notes = Notes 
        
        self.CUser = CUser
        self.MUser = MUser
        
#烟花工程（关于导出工程？）表        
class ProjectsData(base):
    
    __tablename__ = "Projects"
    ID = Column(Integer, Sequence("session_id_seq"), primary_key = True)
    UUID = Column(String, nullable = False, unique = True)    #
    CTime = Column(DateTime )                  #input time   
    MTime = Column(DateTime )                  #modification time
    SceneID = Column(String)                   #使用的建筑ID
    FieldList = Column(Text)                 #选择使用的阵地列表（建筑内），包含Field号(类型待定)`
    Name = Column(String)
    Description = Column(String)
    Animation = Column(String)                 #类型待定
    Time = Column(Date)  
    Location  = Column(String)                   #（坐标，对应地图）详细的地点信息以便识别与搜索？
    MusicID  = Column(String)                 # 
    ProjectFile = Column(String)                     #类型待定(外链)
    Designer = Column(String)                     #
    Worker = Column(String)                     #
    ShellCount = Column(Integer)                     #总发数
    Duration = Column(Interval)                     #工程总时间
    Authorized = Column(String)          #许可工程燃放的密码，以官方私钥加密以上信息得到，公钥解开验证通过才可燃放 
    ModuleCount = Column(Integer)        
    Information = Column(String)              
    Notes = Column(Text)                 #用户自定义字段，类型待定
    
    CUser = Column(String)              #创建人
    MUser = Column(String)              #修改人
    
    def __init__(self, UUID = None, CTime = None, MTime = None,SceneID = None,FieldList = None,Name = None, Description = None,
                 Animation = None, Time = None, Location = None, MusicID = None, ProjectFile = None,
                 Designer = None, Worker = None, ShellCount = None, CUser = None, Duration = None,  MUser = None,
                 Authorized = None, ModuleCount = None, Information = None, Notes = None):
        
        self.UUID = UUID
        self.CTime = CTime
        self.MTime = MTime
        self.Name = Name
        self.FieldList = FieldList
        self.Description = Description
        self.Animation = Animation
        self.Time = Time
        self.Location = Location
        self.SceneID = SceneID
        self.MusicID = MusicID
        self.ProjectFile = ProjectFile
        self.Designer = Designer
        self.Worker = Worker
        self.ShellCount = ShellCount
        self.Duration = Duration
        self.Authorized = Authorized
        self.ModuleCount = ModuleCount
        self.Information = Information 
        self.Notes = Notes 
        
        self.CUser = CUser
        self.MUser = MUser
        
        
#用户设置表        
class UsersData(base):
    
    __tablename__ = "Users"
    
    ID = Column(Integer, Sequence("session_id_seq"), primary_key = True)
    UUID = Column(String, nullable = False, unique = True)    #
    CTime = Column(DateTime )                  #input time
    MTime = Column(DateTime )                  #modification time
    UserName = Column(String)
    FireworkPermList = Column(Integer)
    ScenePermList = Column(Integer)                 #用户对各项数据表中相关条目的访问权限表 
    MusicPermList = Column(Integer )  
    Statistics  = Column(Text)                   #用户的各项统计信息 
    Perferences  = Column(String)                 #用户的各项偏好选择 
    
    CUser = Column(String)              #创建人
    MUser = Column(String)              #修改人
    
    def __init__(self, UUID = None, CTime = None, MTime = None, UserName = None,FireworkPermList = None,
                  ScenePermList = None, MusicPermList = None, Statistics = None, Perferences = None, CUser = None, MUser = None):
        
        self.UUID = UUID
        self.CTime = CTime
        self.MTime = MTime
        self.UserName = UserName
        self.FireworkPermList = FireworkPermList
        self.ScenePermList = ScenePermList
        self.MusicPermList = MusicPermList
        self.Statistics = Statistics
        self.Perferences = Perferences
        
        self.CUser = CUser
        self.MUser = MUser

    
    
class Version(base):
    
    __tablename__ = "Version"

    ID = Column(Integer, Sequence("session_id_seq"), primary_key = True)
    Version = Column(Float, nullable = False)    #
    
    def __init__(self, Version = None):
        self.Version = Version
