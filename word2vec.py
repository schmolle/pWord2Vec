from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile

def main():
    path = get_tmpfile("/home/jschmolzi/pModels/1987.model")
    all_sentences=[]
    with open("/home/jschmolzi/txtFiles/1987.txt","r") as file:
        line = file.readline()
        while line:
            sentences = line.strip().split('.')
            print(sentences)
            for sentence in sentences:
                all_sentences.append(sentence.split())
            line = file.readline()
    model = Word2Vec(all_sentences,size=100, window=5, min_count=1, workers=4)
    model.save("/home/jschmolzi/pModels/1987.model")
    
def train_model(name):
    print("Starting : " + name)
    path = get_tmpfile("/home/jschmolzi/pModels/"+name+".model")
    model = Word2Vec("/home/jschmolzi/txtFiles/"+name+".txt", size=100, window=5, min_count=5, workers=4)
    model.save("/home/jschmolzi/pModels/1987.model")
    print(name + " finished")
    return(model)
    
if __name__ == '__main__':
    main()