import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c = sorted(c)[::-1]
    result = 0
    flower = 0
    turn = 0
    cust = 0
    while flower != len(c):
        result += (turn + 1) * c[flower]
        flower += 1
        cust += 1
        if cust == k:
            turn += 1
            cust = 0
    return result
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
