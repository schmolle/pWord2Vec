import dbaccess as db

def main():
    connection = db.getConnection()
    cursor = connection.cursor()
    vector=[1.5,2.5,3.3,4.2,21.1]

    cursor.close()
    connection.close()
    
if __name__ == '__main__':
    main()