# Part B Task 2
import re
import os
import sys


def pre_posses(path):
    path = list(path)
    path.insert(7, '/')
    path = ''.join(path)
    
    f = open(path, mode='r')
    
    new_str = ''
    
    for line in f.readlines():
        j = re.sub(r'\W', ' ', line)
        g = ' '.join(j.split())
        new_str = new_str + ' ' + g
        
    new_str = ' '.join(new_str.split())
    new_str = new_str.lower()
    
    return(new_str)


print(pre_posses(sys.argv[1]))