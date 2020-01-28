import dbaccess as db

def main():
    connection = db.getConnection()
    cursor = connection.cursor()
    print(db.getSettingId(cursor,'abc'))
    print(db.getWordId(cursor,'apple'))
    cursor.close()
    connection.close()
    
if __name__ == '__main__':
    main()