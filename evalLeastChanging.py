from utils import dbaccess as db
from utils import evalUtils
from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile
import time
import sys
from collections import OrderedDict
from operator import itemgetter 

def main():
    if len(sys.argv) != 4:
        print("usage : cmd bestK targetStartYear targetEndYear")
    else:
        bestK=int(sys.argv[1])
        targetStartYear=int(sys.argv[2])
        targetEndYear=int(sys.argv[3])
        evalLeastChanging(targetStartYear, targetEndYear, bestK)
    
def evalLeastChanging(start,end,topK):
    startTime = time.time()
    connection = db.getConnection()
    cursor = connection.cursor()
    wordIds = db.getWordIdsFromYear(cursor,6,start)
    leng = end - start
    dict = initDict(topK)
    nrOfUnchanged  = 0
    numberOfVecs = end - start + 1
    maxVal = 0.9 * (numberOfVecs-1)
    for wordId in wordIds:
        # init vec array
        vecs = [[] for i in range(numberOfVecs)]
        # fill vec array
        for i in range(start,end+1):
            index = i - start
            vecs[index] = db.getVector(cursor,6,i,wordId)
        l = len(vecs) -1
        # compute cosSim for each tuple of following years
        res = 0
        for j in range(0,l):
            vec1 = vecs[j]
            vec2 = vecs[j+1]
            cosSim = evalUtils.cosSim(vec1,vec2)
            res += cosSim
        if res > maxVal:
            nrOfUnchanged = nrOfUnchanged +1
        for value in dict.values():
            if res > value:
                dict.popitem()
                dict[wordId] = res
                dict=OrderedDict(sorted(dict.items(), key = itemgetter(1), reverse = True))
                break
    print(start," - ",end," :")
    for id,simi in dict.items():
        word = db.getWordFromId(cursor,id)
        print(word, " sim : ",simi)
    print(nrOfUnchanged, " words didnt change")
    print(len(wordIds)," words found")
    cursor.close()
    connection.close()
    endTime = time.time()
    print("full : " , endTime -startTime)
    
def initDict(dictLength):
    d=OrderedDict()
    for i in range(0,dictLength):
        d[i]= -25
    return d
    
if __name__ == '__main__':
    main()