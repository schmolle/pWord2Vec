from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile

def main():
    model1987 = Word2Vec.load("/home/jschmolzi/pModels/1987.model")
    model2007 = Word2Vec.load("/home/jschmolzi/pModels/2007.model")
    while(True):
        word = input("compare word : ")
        result1987 = model1987.most_similar(positive=[word],topn=20)
        result2007 = model2007.most_similar(positive=[word],topn=20)
        for r1,r2,i in zip(result1987,result2007):
            print("{} :  {}  |  {}".format(i,r1,r2))
            
if __name__ == '__main__':
    main()