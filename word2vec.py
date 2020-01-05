from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile

def main():
    path = get_tmpfile("/home/jschmolzi/pModels/all.model")
    all_sentences=[]
    with open("/home/jschmolzi/txtFiles/all.txt","r") as file:
        line = file.readline()
        while line:
            sentences = line.strip().split('.')
            for sentence in sentences:
                all_sentences.append(sentence.split())
            line = file.readline()
    model = Word2Vec(all_sentences,size=100, window=5, min_count=1, workers=4)
    model.save("/home/jschmolzi/pModels/all.model")
    
if __name__ == '__main__':
    main()