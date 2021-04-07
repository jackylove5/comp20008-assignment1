## Part B Task 1

import re
import pandas as pd
import os
import sys

dirs = os.listdir("cricket")

pattern = re.compile(r'([A-Z])([A-Z])([A-Z])([A-Z])-([0-9])([0-9])([0-9])')
pattern_2 = re.compile(r'([A-Z])([A-Z])([A-Z])([A-Z])-([0-9])([0-9])([0-9][A-Z][A-Z])')

doc_ID = []
file_name = []

for i in dirs:
    f = open('cricket/%s'%i,mode='r')
    for line in f.readlines():
        j = pattern.search(line)
        g = pattern_2.search(line)
        if j != None and g == None:
            print(j.group())
            doc_ID.append(j.group())
        if g != None and g.group() !=j.group():
            print(g.group()[:9])
            doc_ID.append(g.group()[:9])
    print(f.name[8:])
    file_name.append(f.name[8:])
    
partb1 = pd.DataFrame()

partb1['filename'] = file_name
partb1['documentID'] = doc_ID

partb1.to_csv(sys.argv[1])