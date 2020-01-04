from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile

def main():
    model = Word2Vec.load("/home/jschmolzi/pModels/1987.model")
    all_sentences=[]
    with open("/home/jschmolzi/txtFiles/2007.txt","r") as file:
        line = file.readline()
        while line:
            sentences = line.strip().split('.')
            print(sentences)
            for sentence in sentences:
                all_sentences.append(sentence.split())
            line = file.readline()
    model.train(all_sentences,total_examples=1)
    path = get_tmpfile("/home/jschmolzi/pModels/2007.model")
    model.save("/home/jschmolzi/pModels/2007.model")
                       
if __name__ == '__main__':
    main()