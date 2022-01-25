import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    val = arr[-1]
    for i in range(n-1, 0, -1):
        if val > arr[i-1]:
            arr[i] = val
            print(' '.join(map(str, arr)))
            break
        elif val < arr[i-1]:
            arr[i] = arr[i-1]
            print(' '.join(map(str, arr)))
    if arr[0] > val:
        arr[0] = val
        print(" ".join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
