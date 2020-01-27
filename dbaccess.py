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
                    ON CONFLICT (word) DO UPDATE\
                    SET word=excluded.word\
                    RETURNING wordId",(word,))
    connection.commit()
    return cursor.fetchall()[0][0]
    

def getIdFromWord(cursor,word):
    cursor.execute("select id from words where word = %s",(word,))
    return cursor.fetchall()

def getWordFromId(cursor,id):
    cursor.execute("select word from words where id = %s",(id,))
    return cursor.fetchall()
    
    
    
    