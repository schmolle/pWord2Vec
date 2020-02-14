import dbaccess as db
from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile
import numpy
import numpy.linalg
import time

def main():
    start = time.time()
    connection = db.getConnection()
    cursor = connection.cursor()
    model0 = Word2Vec.load("/home/jschmolzi/pModels/all.model")
    vocab0 = model0.wv.vocab
    connection = db.getConnection()
    cursor = connection.cursor()
    for word in vocab0:
        db.insertWord(connection,cursor,word)
    cursor.close()
    connection.close()
    end = time.time()
    print("full : " , end -start)

if __name__ == '__main__':
    main()