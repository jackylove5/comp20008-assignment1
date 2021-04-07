## Part B Task 4
import re
import pandas as pd
import os
import sys
import nltk
from nltk.stem.porter import *

dirs = os.listdir("cricket")

def preposses(path):

    f = open(path, mode='r')
    
    new_str = ''
    
    for line in f.readlines():
        j = re.sub(r'\W', ' ', line)
        g = ' '.join(j.split())
        new_str = new_str + ' ' + g
        
    new_str = ' '.join(new_str.split())
    new_str = new_str.lower()
    #print(new_str)
    return(new_str)
    
porterStemmer = PorterStemmer()

keywords = []

keywords = [sys.argv[i] for i in range(1, len(sys.argv))]
keywords_stem = []

for i in keywords:
    stemWord = porterStemmer.stem(i)
    keywords_stem.append(stemWord)
print('keywords\' stem:', keywords_stem)
#print(keywords)
file_name = []

for i in dirs:
    path = str('cricket/%s'%i)
    prepossed_txt = preposses(path)
    word_list = nltk.word_tokenize(prepossed_txt)
    word_list_stem = []
    for j in word_list:
        stemWord = porterStemmer.stem(j)
        word_list_stem.append(stemWord)
    count = 0
    intersection = list(set(word_list_stem).intersection(set(keywords_stem)))
    #print(intersection)
    #print(len(intersection))
    #print(len(sys.argv))
    if len(intersection) == len(keywords):
        file_name.append(i)


print('file name:')
for j in file_name:
    print(j)
    
partb1 = pd.read_csv('partb1.csv',encoding = 'ISO-8859-1')

file_keywords = pd.DataFrame(columns=['file name', 'document ID'])
file_name_1 = []
document_ID_1 = []
count_1 = 0
for g in partb1['filename']:
    if g in file_name:
        file_name_1.append(g)
        document_ID_1.append(partb1.iloc[count_1,2])
    count_1 += 1

file_keywords['file name'] = file_name_1
file_keywords['document ID'] = document_ID_1
print(file_keywords)