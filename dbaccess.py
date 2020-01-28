import psycopg2
from psycopg2 import sql

def getConnection():
    connection = psycopg2.connect(user = "postgres",
                                  password ="nYT!3mBEdd",
                                  host = "localhost",
                                  database = "vectordb")
    return connection

def fetchFromDb(cursor,query):
    cursor.execute(query)
    return cursor.fetchall()

def commitToDb(connection,cursor,query):
    cursor.execute(query)
    connection.commit()
    
def insertWord(connection,cursor,word):
    cursor.execute("INSERT INTO words(word) VALUES (%s)\
                    ON CONFLICT DO NOTHING",(word,))
    connection.commit()
    return "Inserted word %s" %(word)

def getWordId(cursor,word):
    cursor.execute("SELECT wordId from words WHERE word = %s",(word,))
    return cursor.fetchall()[0][0]

def insertSetting(connection,cursor,setting):
    cursor.execute("INSERT INTO settings(setting) VALUES (%s)\
                    ON CONFLICT DO NOTHING",(setting,))
    connection.commit()
    return "Inserted Setting %s" %(setting)

def getSettingId(cursor,setting):
    cursor.execute("SELECT settingsId from settings WHERE setting = %s",(setting,))
    return cursor.fetchall()[0][0]

def insertVector(connection,cursor,setting,word,year,vector):
    settingsId = getSettingId(cursor,setting)
    wordId = getWordId(cursor,word)
    for idx,value in enumerate(vector):
        insertVectorValue(connection,cursor,wordId,settingsId,year,idx,value.item())
    connection.commit()

def insertVectorValue(connection,cursor,wordId,settingsId,year,dimension,value):
    cursor.execute("INSERT INTO vectors(settingsId,wordId,year,dimension,value) VALUES(%s, %s, %s, %s, %s) \
                    ON CONFLICT DO NOTHING",
                   (settingsId, wordId, year, dimension, value, ))

def getIdFromWord(cursor,word):
    cursor.execute("select id from words where word = %s",(word,))
    return cursor.fetchall()

def getWordFromId(cursor,id):
    cursor.execute("select word from words where id = %s",(id,))
    return cursor.fetchall()
    
    
    
    