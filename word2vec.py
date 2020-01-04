from gensim.models import Word2Vec

def main():
    model = Word2Vec(size=100, window=5, min_count=1, workers=4)
    with open("/home/jschmolzi/txtFiles/1987.txt","r") as file:
        line = fp.readline()
        while line:
            sentences = line.strip().split('.')
            print(sentences)
            for sentence in sentences:
                # model.train(sentence.split(),epochs=1)
                print(sentence.split())
            line = fp.readline()

def train_model(name):
    print("Starting : " + name)
    path = get_tmpfile("/home/jschmolzi/pModels/"+name+".model")
    model = Word2Vec("/home/jschmolzi/txtFiles/"+name+".txt", size=100, window=5, min_count=5, workers=4)
    model.save("/home/jschmolzi/pModels/1987.model")
    print(name + " finished")
    return(model)
    
if __name__ == '__main__':
    main()