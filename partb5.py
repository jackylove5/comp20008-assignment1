## Part B Task 5
import re
import pandas as pd
import os
import sys
import nltk
from nltk.stem.porter import *
import math

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
TF = []
for i in dirs:
    path = str('cricket/%s'%i)
    prepossed_txt = preposses(path)
    word_list = nltk.word_tokenize(prepossed_txt)
    word_list_stem = []
    for j in word_list:
        stemWord = porterStemmer.stem(j)
        word_list_stem.append(stemWord)
    keyword_freq = 0
    for x in keywords_stem:
        for y in word_list_stem:
            if x == y :
                keyword_freq += 1
                #print(keyword_freq)
    
    #print(len(TF))
    intersection = list(set(word_list_stem).intersection(set(keywords_stem)))
    #print(intersection)
    #print(len(intersection))
    #print(len(sys.argv))
    if len(intersection) == len(keywords):
        file_name.append(i)
        TF.append(keyword_freq/len(word_list_stem))
print(TF)
IDF = math.log(124/(len(file_name)+1),10)
print(IDF)
print('file name:')
for j in file_name:
    print(j)
    
for i in range(len(TF)):
    TF[i] = round(TF[i]*IDF,4)
print(TF)
    
partb1 = pd.read_csv('partb1.csv',encoding = 'ISO-8859-1')

file_keywords = pd.DataFrame(columns=['file name', 'document ID','score'])
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
file_keywords['score'] = TF
print(file_keywords.sort_values(axis=0,ascending=False,by=['score']))