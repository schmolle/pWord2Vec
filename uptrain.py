import logging
import sentenceUtils
from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile

def main():
    print("training 1987 ....")
    train_model("1987")
    print("training 2007 ....")
    train_model("2007")
    
def train_model(name):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    model = Word2Vec.load("/home/jschmolzi/pModels/all.model")
    all_sentences=[]
    with open("/home/jschmolzi/txtFiles/"+name+".txt","r") as file:
        for line in file:
            line = sentenceUtils.clean_up_line(line)
            sentences = sentenceUtils.split_line(line)
            for sentence in sentences:
                all_sentences.append(sentence.split())
            line = file.readline()
    model.train(all_sentences,total_examples=len(all_sentences),epochs=model.epochs)
    path = get_tmpfile("/home/jschmolzi/pModels/"+name+".model")
    model.save("/home/jschmolzi/pModels/"+name+".model")
                   
if __name__ == '__main__':
    main()