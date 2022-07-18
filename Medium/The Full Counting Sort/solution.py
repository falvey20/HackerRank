import math
import os
import random
import re
import sys
import collections
#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    
    d = collections.defaultdict(list)
    for i in range(len(arr)):
        key, val = arr[i][0], arr[i][1]
        if i < (len(arr)//2):
            d[int(key)].append("-")
        else:
            d[int(key)].append(val)
    
    ordered_d = collections.OrderedDict(sorted(d.items()))
    print(" ".join([" ".join(i) for i in ordered_d.values()]))
        
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
