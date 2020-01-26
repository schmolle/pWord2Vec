import psycopg2
import dbaccess as db

def main():
    connection = db.getConnection()
    cursor = connection.getCursor()
    print(db.getIdFromWord(cursor,"apple"))
    print(db,getWordFromId(cursor,1))
    
if __name__ == '__main__':
    main()