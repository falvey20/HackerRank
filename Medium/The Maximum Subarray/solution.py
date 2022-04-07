import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    if max(arr) < 0:
        return [max(arr), max(arr)]
    else: 
        maxsubseq = sum(i for i in arr if i > 0)
        maxsubarr = 0
        current = 0
    for i in arr:
        current = max(0, current + i)
        maxsubarr = max(current, maxsubarr)
    return [maxsubarr, maxsubseq]
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
