#coding=utf-8
'''
Created on 2013-5-7

@author: pyroshow
'''
from config import appdata
from sqlalchemy.engine import create_engine
import os



def addColumn(conn, tabName,colName, dataType):
    try : 
            conn.execute("select  "+colName+" from Fireworks")
    except:
            conn.execute("alter table "+tabName +" add column "+ colName +" "+  dataType )

def upgrade():
    engine = create_engine("sqlite:///" + os.path.join (appdata, 'local', 'local.db'))
    connection =  engine.connect()
    
    older = connection.execute("select  Version from Version").first()
    print "older", older[0]
#    if not older :
#        connection.execute("drop database local.db") 
##        createDB()
    if older[0] < 0.2:
        
        addColumn(connection, "Fireworks", "test1", "varchar(20)")
        
        connection.execute("update  Version set Version = 0.2 where ID = 1") 
        print "*********************"
        
#    if older < 0.3:
#        
#        addColumn("Fireworks", "test2", "varchar(20)")
#        
#        connection.execute("update  Version set Version = 0.3 where ID = 1") 
#    if older < 0.4:
#        
#        addColumn("Fireworks", "test3", "varchar(20)")
#        
#        connection.execute("update  Version set Version = 0.4 where ID = 1") 
#    if older < 0.5:
#        
#        addColumn("Fireworks", "test4", "varchar(20)")
#        
#        connection.execute("update  Version set Version = 0.5 where ID = 1") 
#    if older < 0.6:
#        
#        addColumn("Fireworks", "test5", "varchar(20)")
#        
#        connection.execute("update  Version set Version = 0.6 where ID = 1") 
#    if older < 0.7:
#        
#        addColumn("Fireworks", "test6", "varchar(20)")
#        
#        connection.execute("update  Version set Version = 0.7 where ID = 1") 

        connection.close()
        
        

        




    

