import re
#'r' toegevoegd voor string omdat hij een fout gaf

def is_number(string):
    return re.fullmatch(r'[0-9]+(\.[0-9]+)?', string)