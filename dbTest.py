import dbaccess as db

def main():
    connection = db.getConnection()
    cursor = connection.cursor()
    vector=[1.5,2.5,3.3,4.2,21.1]
    db.insertVector(connection,cursor,'setting2','word2',2007,vector)
    db.insertVector(connection,cursor,'setting1','word1',2000,vector)
    cursor.close()
    connection.close()
    
if __name__ == '__main__':
    main()