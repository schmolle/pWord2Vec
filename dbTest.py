import dbaccess as db
from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile

def main():
    connection = db.getConnection()
    cursor = connection.cursor()
    print(db.getVector(cursor,6,1987,2224))
    cursor.close()
    connection.close()
    
if __name__ == '__main__':
    main()