import dbaccess as db

def main():
    connection = db.getConnection()
    cursor = connection.cursor()
    query = "select * from words"
    print(fetchFromDb(cursor,query))
    print(db.getIdFromWord(cursor,"apple"))
    print(db,getWordFromId(cursor,1))
    cursor.close()
    connection.close()
    
if __name__ == '__main__':
    main()