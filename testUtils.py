import sentenceUtils

def main():
    line = 'Hello; this- is. me? or! not'
    print("split_line(" + line + ") -> ")
    print(sentenceUtils.split_line(line))
    line = "John's boOk iS losT"
    print("clean_up_line(" + line + ") -> ")
    print(sentenceUtils.clean_up_line(line))
    
if __name__ == '__main__':
    main()