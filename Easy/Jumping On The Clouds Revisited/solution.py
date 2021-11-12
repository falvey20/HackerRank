import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    energy = 100
    l = len(c)
    # Set cloud position to start at 0
    pos = 0
    # Continue until break condition met (pos==0)
    while True:
        pos = (pos+k)%l
        if c[pos] == 1:
            energy -= 3
        else:
            energy -= 1
        if pos == 0:
            break
    return energy
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
