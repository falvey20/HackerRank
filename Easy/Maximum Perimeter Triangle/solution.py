import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    sticks = sorted(sticks)
    result = [-1]
    for i in range(0, len(sticks)-2):
        if sticks[i] + sticks[i+1] > sticks[i+2]:
            result = sticks[i:i+3]
        elif sticks[i] == sticks[i+1] == sticks[i+2]:
            result = sticks[i:i+3]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
