import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    l = len(arr)
    pos, neg, zer = 0, 0, 0
    for i in arr:
        if i < 0:
            neg += 1
        elif i == 0:
            zer += 1
        else:
            pos += 1
    print(pos/l)
    print(neg/l)
    print(zer/l)        
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
