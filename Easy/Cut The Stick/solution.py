import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    num_of_sticks = []
    length = len(arr)
    
    sticks = Counter(arr)
    for i in sorted(sticks.keys()):
        num_of_sticks.append(length)
        length -= sticks[i]
    return num_of_sticks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
