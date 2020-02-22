def main():
    #fullList = testList(1,3)
    #print(str(fullList))
    #l = len(fullList) -1
    #for i,subList in enumerate(fullList):
    #    print("current : " , str(subList))
    #    if(i < l):
    #        print("next : ",str(fullList[i+1]) )
    start = 1987
    end = 1989
    arr=[0 for i in range(0,end-start)]
    print(str(arr))
    
def testList(start,end):
    number = end - start + 1
    arr = [[] for i in range(number)]
    for i in range(start,end+1):
        index = i - start
        arr[index] = [1+i,2+i,3+i]
    return arr
    
    
    
if __name__ == '__main__':
    main()