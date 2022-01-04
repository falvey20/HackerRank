import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    sarr = sorted(arr)
    closest = []
    min_dif = abs(sarr[0]-sarr[1])
    
    for i in range(0, len(sarr)-1):
        diff = sarr[i+1]-sarr[i]
        if diff<min_dif:
            min_dif = diff
            closest = [sarr[i], sarr[i+1]]
        elif diff == min_dif:
            closest.append(sarr[i])
            closest.append(sarr[i+1])
    
    return closest
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
