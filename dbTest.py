import dbaccess as db

def main():
    connection = db.getConnection()
    cursor = connection.cursor()
    print(db.getIdFromWord(cursor,"apple"))
    print(db,getWordFromId(cursor,1))
    
if __name__ == '__main__':
    main()