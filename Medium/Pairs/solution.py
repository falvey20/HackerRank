import math
import os
import random
import re
import sys
from itertools import combinations
#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    result = 0
    arr = sorted(arr)
    p = 1
    for i in range(0, len(arr)):
        while p < len(arr):
            if arr[p] == arr[i]+k:
                result += 1
                break
            elif arr[p] > arr[i]+k:
                break
            else:
                p += 1
    return result
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
