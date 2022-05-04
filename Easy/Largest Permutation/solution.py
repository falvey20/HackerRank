import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    index = {} # num: index
    l = len(arr)
    for i in range(l):
        index[arr[i]] = i
        
    swaps = 0
    i = 0
    while swaps < k and i < l:
        if arr[i] < l-i:
            idx = index[l-i]
            arr[i], arr[idx] = arr[idx], arr[i]
            index[arr[idx]] = idx
            index[l-i] = i
            swaps += 1
        i += 1
    return arr
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
