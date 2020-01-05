from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile

def main():
    model1987 = Word2Vec.load("/home/jschmolzi/pModels/1987.model")
    model2007 = Word2Vec.load("/home/jschmolzi/pModels/2007.model")
    while(true):
        word = input("compare word : ")
        result = model1987.most_similar(positive=[word],topn=20)
        print(result)
        result = model2007.most_similar(positive=[word],topn=20)
        print(result)
    
if __name__ == '__main__':
    main()