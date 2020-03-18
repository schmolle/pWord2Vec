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
        print("usage : cmd bestK nrOfYears word")
    else:
        bestK = int(sys.argv[1])
        nrOfYears = int(sys.argv[2])
        word = sys.argv[3]
        evalMostChangingPeriod(bestK, nrOfYears, word)
    
def evalMostChangingPeriod(topK, nrOfYears, word):
    startTime = time.time()
    connection = db.getConnection()
    cursor = connection.cursor()
    vecs = []
    dict = initDict(topK)
    wordId = db.getWordId(cursor, word)
    for i in range(1987, 2008):
        vec = db.getVector(cursor,6,i,wordId)
        vecs.append(vec)
    endLoop = 2009 - nrOfYears
    for i in range(1987, endLoop):
        indx = i - 1987
        res = 0
        for j in range(0, nrOfYears-1):
            vec1 = vecs[indx + j]
            vec2 = vec[indx + j + 1] 
            cosSim = evalUtils.cosSim(vec1,vec2)
            res += cosSim
        for value in dict.values():
            if res < value:
                dict.popitem()
                dict[wordId] = res
                dict=OrderedDict(sorted(dict.items(), key = itemgetter(1), reverse = False))
                break
    
    for year,sim in dict.items():
        print("From %d to %d : %d" % yeah, year+ nrOfYears, sim)
    
def initDict(dictLength):
    d=OrderedDict()
    for i in range(0,dictLength):
        d[i]= 25
    return d
    
if __name__ == '__main__':
    main()