from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile

def main():
    model1987 = Word2Vec.load("/home/jschmolzi/pModels/1987.model")
    model2007 = Word2Vec.load("/home/jschmolzi/pModels/2007.model")
    while(True):
        word = input("compare word : ")
        result1987 = model1987.most_similar(positive=[word],topn=20)
        result2007 = model2007.most_similar(positive=[word],topn=20)
        i=0
        for r1,r2 in zip(result1987,result2007):
            print("{0:2d} :  {1} , {2} |  {3} , {4}".format(i,r1[0].ljust(15),r1[1],r2[0].ljuts(15),r2,[1]))
            i = i+1
            
if __name__ == '__main__':
    main()