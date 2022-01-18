import math
import os
import random
import re
import sys
from itertools import combinations
#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    sarr = sorted(arr)
    min_dif = max(sarr)
    for i in range(0, len(sarr)-k+1):
        dif = abs(sarr[i+k-1]-sarr[i])
        if dif < min_dif:
            min_dif = dif
    return min_dif
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
