import logging
import sentenceUtils
from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile

def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    path = get_tmpfile("/home/jschmolzi/pModels/all.model")
    all_sentences=[]
    model = Word2Vec(size=100, window=5, min_count=5, workers=4)
    print("VOCAB BUILDING")
    with open("/home/jschmolzi/txtFiles/1987.txt","r") as file:
            print("start reading file : 1987")
            for line in file:
                line = line.lower().replace(",","")
                sentences = line.strip().split('. |! |? |- |; ')
                for sentence in sentences:
                    all_sentences.append(sentence.split())
    model.build_vocab(all_sentences)
    all_sentences=[]
    for i in range(1988,2008):
        with open("/home/jschmolzi/txtFiles/"+str(i)+".txt","r") as file:
            print("start reading file : "+str(i))
            for line in file:
                line = sentenceUtils.clean_up_line(line)
                sentences = sentenceUtils.split_line(line)
                for sentence in sentences:
                    all_sentences.append(sentence.split())
        model.build_vocab(all_sentences,update=True)
        all_sentences=[]
    print("TRAINING")
    for i in range(1987,2008):
        with open("/home/jschmolzi/txtFiles/"+str(i)+".txt","r") as file:
            print("start reading file : "+str(i))
            for line in file:
                line = sentenceUtils.clean_up_line(line)
                sentences = sentenceUtils.split_line(line)
                for sentence in sentences:
                    all_sentences.append(sentence.split())
        model.train(all_sentences,total_examples=len(all_sentences),epochs=model.epochs)
        all_sentences=[]
    model.save("/home/jschmolzi/pModels/all.model")
    
if __name__ == '__main__':
    main()