import dbaccess as db
from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile

def main():
    model0 = Word2Vec.load("/home/jschmolzi/pModels/all.model")
    #model2007 = Word2Vec.load("/home/jschmolzi/pModels/2007.model")
    vocab0 = model0.wv.vocab
    setting = 'window5,size100'
    connection = db.getConnection()
    cursor = connection.cursor()
    for word in vocab0:
        db.insertWord(connection,cursor,word)
    cursor.close()
    connection.close()
    
if __name__ == '__main__':
    main()