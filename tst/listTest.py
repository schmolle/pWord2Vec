from collections import OrderedDict
from operator import itemgetter 

def main():
    d=initDict(5)
    print(d)
    sim =1 
    wordId=99
    for value in d.values():
            if sim > value:
                d.popitem()
                d[wordId] = sim
                d=OrderedDict(sorted(d.items(), key = itemgetter(1), reverse = True))
                break
    print(d)
    
def testList(start,end):
    number = end - start + 1
    arr = [[] for i in range(number)]
    for i in range(start,end+1):
        index = i - start
        arr[index] = [1+i,2+i,3+i]
    return arr
    
def initDict(dictLength):
    d=OrderedDict()
    for i in range(0,dictLength):
        d[i]=-1
    return d
    
if __name__ == '__main__':
    main()