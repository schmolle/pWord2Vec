import dbaccess as db

def main():
    connection = db.getConnection()
    cursor = connection.cursor()
    for i in range(1987,2008):
        print("/home/jschmolzi/pModels/"+str(i)+".model")
    cursor.close()
    connection.close()
    
if __name__ == '__main__':
    main()