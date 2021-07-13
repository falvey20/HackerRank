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
    pos = 0
    neg = 0
    zer = 0
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        elif num == 0:
            zer += 1
            
    length = len(arr)
    print(round((pos / length), 6))
    print(round((neg / length), 6))
    print(round((zer / length), 6))
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
