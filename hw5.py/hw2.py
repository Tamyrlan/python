# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

## Честно скажу что не разобрался до конца по этой работе, прибегнул к гуглу и подсмотрел .
from itertools import groupby, starmap
from os import path

def encode(text = "text_words.txt",coded_text = "text_code_words.txt"):
    if path.exists(text) and not path.exists(coded_text):
        with open(text) as my_file,\
                open(coded_text,"a") as my_file2:
            for i in my_file:
                my_file2.write("".join([f"{len(list(v))}{ch}" for ch,v in groupby(i)]))
    else:
        print('The files do not exist')
    

def decode(name):
    if path.exists(name):
        with open(name) as my_f:
            n=""
            for k in my_f:
                word_nums =[]
                for i in k.strip():
                    if i.isdigit():
                        n+=i
                    else:
                        word_nums.append([int(n),i])
                        n =""
                print("".join(starmap(lambda x,y:x*y,word_nums)))
    else:
        print("The files do not exist")

encode(input('Enter the name of the file with the text:'), input("Enter the file name to record:"))
decode(input('Enter the name of the file to decode:'))
