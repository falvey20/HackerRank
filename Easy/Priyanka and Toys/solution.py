import math
import os
import random
import re
import sys

#
# Complete the 'toys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY w as parameter.
#

def toys(w):
    w = sorted(w)
    containers = 1
    cur_weight = w[0]
    
    for i in range(1, len(w)):
        if w[i] > cur_weight+4:
            containers += 1
            cur_weight = w[i]
    return containers
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
