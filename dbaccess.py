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
    query = sql.SQL("select id from words where word = (word)",word)
    return fetchFromDb(cursor, query)

def getWordFromId(cursor,id):
    query = sql.SQL("select word from words where id = (id)",id)
    return fetchFromDb(cursor, query)
    
    
    
    