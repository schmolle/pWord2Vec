from utils import dbaccess as db
from utils import evalUtils
from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile
import time
from collections import OrderedDict
from operator import itemgetter 
   
def main():
    for i in range(1995,2005):
        word='apple'
        year=2007
        bestK=6
        evalSimilarWords(word,year,i,bestK)
    
def evalSimilarWords(word,year,targetYear,bestK):
    startTime = time.time()
    connection = db.getConnection()
    cursor = connection.cursor()
    connectTime = time.time()
    wordIds = db.getWordIdsFromYear(cursor,6,targetYear)
    wordTime = time.time()
    word = db.getWordId(cursor, word)
    vec = db.getVector(cursor,6,year,word)
    dict = initDict(bestK)
    for wordId in wordIds:
        targetVec = db.getVector(cursor,6,targetYear,wordId)
        sim = evalUtils.cosSim(vec,targetVec)
        for value in dict.values():
            if sim > value:
                dict.popitem()
                dict[wordId] = sim
                dict=OrderedDict(sorted(dict.items(), key = itemgetter(1), reverse = True))
                break
    for id,simi in dict:
        word = db.getWordFromId(cursor,id)
        print(word, " sim : ",simi)
    cursor.close()
    connection.close()
    endTime = time.time()
    print("words: : " , wordTime-connectTime)
    print("full : " , endTime -startTime)

def initDict(dictLength):
    d=OrderedDict()
    for i in range(0,dictLength):
        d[i]=-1
    return d
        
        
if __name__ == '__main__':
    main()