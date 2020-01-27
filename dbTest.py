import dbaccess as db

def main():
    connection = db.getConnection()
    cursor = connection.cursor()
    print(db.insertWord(connection,cursor,'apple'))
    rows = db.insertWord(connection,cursor,'apple')
    print(rows)
    print(rows[0])
    cursor.close()
    connection.close()
    
if __name__ == '__main__':
    main()