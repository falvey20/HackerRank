import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):
    counts = Counter()
    
    for word in arr:
        for char in set(word):
            counts[char] += 1
            
    gemstones = 0
    for i in counts:
        if counts[i] == len(arr):
            gemstones += 1
    
    return gemstones

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
