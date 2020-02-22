from utils import dbaccess as db
from utils import evalUtils
from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile
import time

id1 = 0
id2 = 0
id3 = 0
sim1 =1.1
sim2 =1.1
sim3 =1.1
    
def main():
    for i in range(1987,1990):
        word='apple'
        year=1987
        evalSimilarWords(word,year,i)
    
def evalSimilarWords(word,year,targetYear):
    startTime = time.time()
    connection = db.getConnection()
    cursor = connection.cursor()
    connectTime = time.time()
    wordIds = db.getWordIdsFromYear(cursor,6,targetYear)
    wordTime = time.time()
    word = db.getWordId(word)
    vec = db.getVector(cursor,6,year,word)
    for wordId in wordIds:
        targetVec = db.getVector(cursor,6,targetYear,wordId)
        sim = evalUtils.cosSim(vec,targetVec)
        if sim < sim1:
            betterThanSim1(sim, wordId)
        elif sim < sim2:
            betterThanSim2(sim, wordId)
        elif sim < sim3:
            betterThanSim3(sim, wordId)
    word1 = word = db.getWordFromId(cursor,id1)
    word2 = word = db.getWordFromId(cursor,id2)
    word3 = word = db.getWordFromId(cursor,id3)
    cursor.close()
    connection.close()
    print("1 : ", word1 , "sim : ", sim1)
    print("2 : ", word2 , "sim : ", sim2)
    print("3 : ", word3 , "sim : ", sim3)
    endTime = time.time()
    print("words: : " , wordTime-connectTime)
    print("full : " , endTime -startTime)
    
def betterThanSim1(sim,id):
    sim3=sim2
    id3=id2
    sim2=sim1
    id2=id1
    id1=id
    sim1=sim

def betterThanSim2(sim,id):
    sim3=sim2
    id3=id2
    id2=id
    sim2=sim
    
def betterThanSim3(sim,id):
    sim3=sim
    id3=id
        
if __name__ == '__main__':
    main()