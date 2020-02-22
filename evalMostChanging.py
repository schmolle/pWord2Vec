from utils import dbaccess as db
from utils import evalUtils
from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile
import time

def main():
    for i in range(1987,1990):
        evalDifference(i, i+1)
    
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
            cosSim = evalUtils.cosSim(vec1,vec2)
            # compare with current 'best'
            if cosSim < cosSims[j]:
                ids[j] = wordId
                cosSims[j] = cosSim
    print(start," - ",end," :")
    for i in range(start,end):
        id=ids[i-start]
        word = db.getWordFromId(cursor,id)
        print(word,": ",cosSims[i-start])
    cursor.close()
    connection.close()
    endTime = time.time()
    print("words: : " , wordTime-connectTime)
    print("eval : " , endTime - wordTime)
    print("full : " , endTime -startTime)
        
    
if __name__ == '__main__':
    main()