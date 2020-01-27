import dbaccess as db

def main():
    connection = db.getConnection()
    cursor = connection.cursor()
    print(insertWord(connection,cursor,'apple'))
    print(insertWord(connection,cursor,'apple'))
    cursor.close()
    connection.close()
    
if __name__ == '__main__':
    main()