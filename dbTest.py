import psycopg2

def main():
    connection = psycopg2.connect(user = "postgres",
                                  password ="nYT!3mBEdd",
                                  host = "localhost",
                                  database = "vectordb")
    cursor = connection.cursor()
    selectquery = "select * from words"
    cursor.execute(selectquery)
    print(cursor.fetchcall())
    insertquery = "insert into words(word) values('success')"
    cursor.execute(insertquery)
    connection.commit()
    cursor.execute(selectquery)
    print(cursor.fetchcall())
    cursor.close()
    connection.close()
    
if __name__ == '__main__':
    main()