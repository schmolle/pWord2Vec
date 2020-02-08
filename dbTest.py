import dbaccess as db
from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile

def main():
    connection = db.getConnection()
    cursor = connection.cursor()
    vec = db.getVector(cursor,6,1987,2224)
    for val in vec:
        print(val[0])
    cursor.close()
    connection.close()
    
if __name__ == '__main__':
    main()