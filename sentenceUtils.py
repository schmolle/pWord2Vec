import re

def split_line(line):
    return re.split(r'[.?!-;]\s*',line.strip())

def clean_up_line(line):
    return line.lower().replace("'","")
    
    