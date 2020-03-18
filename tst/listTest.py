from collections import OrderedDict
from operator import itemgetter 

def main():
    lst2 = []
    lst = [1,2,3]
    lst2.append(lst)
    lst2.append(lst)
    lst2.append(lst)
    print(lst2)
    
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