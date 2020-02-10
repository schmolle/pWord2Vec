import dbaccess as db
from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile
import numpy
import numpy.linalg
import time

def main():
    evalDifference(1988, 1989)
    
def evalDifference(start,end):
    startTime = time.time()
    connection = db.getConnection()
    cursor = connection.cursor()
    connectTime = time.time()
    wordIds = db.getWordIdsFromYear(cursor,6,start)
    wordTime = time.time()
    leng = end - start
    ids = [0 for i in range(0,leng)]
    cosSims = [2 for i in range(0,leng)]
    print(str(ids))
    print(str(cosSims))
    
    for wordId in wordIds:
        numberOfVecs = end - start + 1
        # init vec array
        vecs = [[] for i in range(numberOfVecs)]
        # fill vec array
        for i in range(start,end+1):
            index = i - start
            vecs[index] = db.getVector(cursor,6,i,wordId)
        l = len(vecs) -1
        # compute cosSim for each tuple of following years
        for j in range(0,l):
            vec1 = vecs[j]
            vec2 = vecs[j+1]
            cosSim = numpy.dot(vec1, vec2) / (numpy.linalg.norm(vec1) * numpy.linalg.norm(vec2))
            # compare with current 'best'
            if cosSim < cosSims[j]:
                ids[j] = wordId
                cosSims[j] = cosSim
    cursor.close()
    connection.close()
    endTime = time.time()
    print("connection : " , connectTime - startTime)
    print("words: : " , wordTime-connectTime)
    print("eval : " , endTime - wordTime)
    print("full : " , endTime -startTime)
    print(str(ids))
    print(str(cosSims))       
        
    
if __name__ == '__main__':
    main()