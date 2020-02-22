import logging
from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile
from utils import sentenceUtils

def main():
    print("training 1987 ....")
    train_model("1987")
    print("training 2007 ....")
    train_model("2007")
    
def train_model(name):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    all_sentences=[]
    with open("/home/jschmolzi/txtFiles/"+name+".txt","r") as file:
        line = file.readline()
        while line:
            line = sentenceUtils.clean_up_line(line)
            sentences = sentenceUtils.split_line(line)
            for sentence in sentences:
                all_sentences.append(sentence.split())
            line = file.readline()
    model = Word2Vec(all_sentences,size=100, window=5, min_count=5, workers=4)
    path = get_tmpfile("/home/jschmolzi/pModels/"+name+"no.model")
    model.save("/home/jschmolzi/pModels/"+name+"no.model")
                   
if __name__ == '__main__':
    main()