from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile

def main():
    model = Word2Vec.load("/home/jschmolzi/pModels/1987.model")
    result = model.most_similar(positive=['woman', 'king'], negative=['man'])
    print(result)
    result = word_vectors.most_similar(positive=['apple'],topn=5)
    print(result)
    
if __name__ == '__main__':
    main()