from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile
import dbaccess as db

def main():
    model0 = Word2Vec.load("/home/jschmolzi/pModels/1987.model")
    #model2007 = Word2Vec.load("/home/jschmolzi/pModels/2007.model")
    vocab0 = model0.wv.vocab
    setting = 'window5,size100'
    connection = db.getConnection()
    cursor = connection.cursor()
    print(db.insertSetting(connection,cursor,setting))
    for word in vocab0:
        db.insertVector(connection,cursor,setting,word,0,model0[word])
    
    for i in range(1987,2008):
        print(i)
        model = Word2Vec.load("/home/jschmolzi/pModel/"+str(i)+".model")
        vocab = model.wv.vocab
        for word in vocab:
            db.insertVector(connection,cursor,setting,word,i,model[word])
    cursor.close()
    connection.close()
                
if __name__ == '__main__':
    main()