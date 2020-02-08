import dbaccess as db
from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile

def main():
    connection = db.getConnection()
    cursor = connection.cursor()
    vec = db.getVector(cursor,6,1987,2224)
    model = Word2Vec.load("/home/jschmolzi/pModels/1987.model")
    oVec = model['players']
    print(vec)
    print(oVec)
    for val,oVal in zip(vec,oVec):
        print(val , oVal)
    cursor.close()
    connection.close()
    
if __name__ == '__main__':
    main()