from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile

def main():
    model1987 = Word2Vec.load("/home/jschmolzi/pModels/1987.model")
    #model2007 = Word2Vec.load("/home/jschmolzi/pModels/2007.model")
    vecs1987 = model1987.wv.vectors
    vocab1987 = model1987.wv.vocab
    i=0
    for vec in vecs1987:
        print(vec)
        i = i+1
        if i >10 :
            break;
    i=0
    for word in words1987:
        print(vec)
        i = i+1
        if i >10 :
            break;
                
if __name__ == '__main__':
    main()