import dbaccess as db
from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile
import numpy
import numpy.linalg
import time
from _sqlite3 import connect

def main():
    start = time.time()
    connection = db.getConnection()
    cursor = connection.cursor()
    #vec1 = db.getVector(cursor,6,1987,2224)
    #vec2 = db.getVector(cursor,6,1987,2227)
    #model = Word2Vec.load("/home/jschmolzi/pModels/1987.model")
    #oVec1 = model['players']
    #oVec2 = model['mary']
    #print(model.similarity('players', 'mary'))
    #print(numpy.dot(vec1, vec2) / (numpy.linalg.norm(vec1) * numpy.linalg.norm(vec2)))
    #print(numpy.dot(oVec1, oVec2) / (numpy.linalg.norm(oVec1) * numpy.linalg.norm(oVec2)))
    connect = time.time()
    bestId = 0
    bestCosSim = 2
    wordIds = db.getWordIdsFromYear(cursor,6,1987)
    words = time.time()
    for wordId in wordIds:
        vec1 = db.getVector(cursor,6,1987,wordId)
        vec2 = db.getVector(cursor,6,1988,wordId)
        cosSim = numpy.dot(vec1, vec2) / (numpy.linalg.norm(vec1) * numpy.linalg.norm(vec2))
        if cosSim < bestCosSim :
            bestId = wordId
            bestCosSim = cosSim
    print(bestId , bestCosSim)
    eval=time.time()
    cursor.close()
    connection.close()
    end = time.time()
    print("connection : " , connect-start)
    print("words: : " , words-connect)
    print("eval : " , eval - words)
    print("full : " , end -start)

if __name__ == '__main__':
    main()