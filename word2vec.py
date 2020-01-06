import logging
from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile

def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    path = get_tmpfile("/home/jschmolzi/pModels/all.model")
    all_sentences=[]
    model = Word2Vec(size=100, window=5, min_count=5, workers=4)
    print("VOCAB BUILDING")
    for i in range(1987,2008):
        with open("/home/jschmolzi/txtFiles/"+i+".txt","r") as file:
            print("start reading file : "+i)
            for line in file:
                sentences = line.strip().split('.')
                for sentence in sentences:
                    all_sentences.append(sentence.split())
        model.build_vocab(all_sentences,update=True)
    print("TRAINING")
    for i in range(1987,2008):
        with open("/home/jschmolzi/txtFiles/"+i+".txt","r") as file:
            print("start reading file : "+i)
            for line in file:
                sentences = line.strip().split('.')
                for sentence in sentences:
                    all_sentences.append(sentence.split())
        model.train(all_sentences)
    model.save("/home/jschmolzi/pModels/all.model")
    
if __name__ == '__main__':
    main()