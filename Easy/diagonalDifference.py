import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    primary_total = 0
    secondary_total = 0
    
    j = 0
    k = len(arr) - 1
    for i in arr:
        primary_total += i[j]
        j += 1
    for i in arr:
        secondary_total += i[k]
        k -= 1
        
    return abs(primary_total - secondary_total)
        
        
        
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
