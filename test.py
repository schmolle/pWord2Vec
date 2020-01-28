from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile
import dbaccess

def main():
    model1987 = Word2Vec.load("/home/jschmolzi/pModels/1987.model")
    #model2007 = Word2Vec.load("/home/jschmolzi/pModels/2007.model")
    vecs1987 = model1987.wv.vectors
    vocab1987 = model1987.wv.vocab
    setting = "window5,size100"
    connection = db.getConnection()
    cursor = connection.cursor()
    print(db.insertSetting(connection,cursor,setting))
    for word in vocab1987:
        print(dbaccess.insertWord(connection,cursor,word))
        dbaccess.insertVector(connection,cursor,setting,word,1987,model1987[word])
    cursor.close()
    connection.close()
                
if __name__ == '__main__':
    main()