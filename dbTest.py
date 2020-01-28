import dbaccess as db

def main():
    connection = db.getConnection()
    cursor = connection.cursor()
    print(db.getSettingId('abc'))
    print(db.getWordId('apple'))
    cursor.close()
    connection.close()
    
if __name__ == '__main__':
    main()