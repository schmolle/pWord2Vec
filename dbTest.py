import psycopg2

def main():
    connection = psycopg2.connect(user = "postgres",
                                  password ="nYT!3mBEdd",
                                  host = "localhost",
                                  database = "vectordb")
    cursor = connection.cursor()
    selectquery = "select * from words"
    print(cursor.execute(selectquery))
    insertquery = "insert into words(word) values('success')"
    cursor.execute(insertquery)
    print(cursor.execute(selectquery))
    cursor.close()
    connection.close()
    
if __name__ == '__main__':
    main()