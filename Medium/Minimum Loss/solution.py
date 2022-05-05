import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    p = sorted(price, reverse=True)
    l = len(price)
    result = max(price)
    for i in range(0, l-1):
        if (p[i] - p[i+1] < result) and (price.index(p[i]) < price.index(p[i+1])):
            result = p[i] - p[i+1]
            if result == 1:
                return 1
    return result
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
