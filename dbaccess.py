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

def getIdFromWord(cursor,word):
    cursor.execute("select id from words where word=(word)",word)
    return cursor.fetchall()

def getWordFromId(cursor,id):
    query = ("select word from words where id=(id)",id)
    return cursor.fetchall()
    
    
    
    