import math
import os
import random
import re
import sys
from itertools import combinations
#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    combs = list(combinations(list(set(s)), 2))
    strs = []
    for i in range(len(combs)):
        sub = ''
        for j in range(0, len(s)):
            if s[j] == combs[i][0] or s[j] == combs[i][1]:
                sub += s[j]
        strs.append(sub)
    print(strs)
    
    result = 0
    for st in strs:
        alternating = True
        for i in range(len(st) - 2) :
            if (st[i] != st[i+2]) :
                alternating = False
                break
        if alternating == True:
            if len(st) > result:
                result = len(st)
    return result
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
