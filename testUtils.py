import sentenceUtils

def main():
    line = "HeL,lo; tHi's- is. m\"e? or! not"
    print("Line : " + line)
    line = sentenceUtils.clean_up_line(line)
    print("Line after cleanup : " + line) 
    line = sentenceUtils.split_line(line)
    print("Line after split : ")
    print(line)    
if __name__ == '__main__':
    main()