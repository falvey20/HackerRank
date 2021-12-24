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
    pos = 0
    neg = 0
    zer = 0
    
    for num in arr:
        if num > 0:
            pos += 1
        if num < 0:
            neg += 1
        if num == 0:
            zer += 1
            
    print("{:.6f}".format(pos/l))
    print("{:.6f}".format(neg/l))
    print("{:.6f}".format(zer/l))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
