import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    def mismatch(arr):
        sarr = list(sorted(arr))
        return [i for i in range(len(arr)) if arr[i]!=sarr[i]]
        
    def swappable(wrong_indxs):
        if len(wrong_indxs) == 2:
            return True
    
    def reversible(arr, mismatches):
        start, end = min(mismatches), max(mismatches)
        rev_arr = arr[start:end+1][::-1]
        if rev_arr == list(sorted(rev_arr)):
            return start,end
        return False
        
    wrong_indxs = mismatch(arr)
    if swappable(wrong_indxs):
        print(f"yes\nswap {wrong_indxs[0]+1} {wrong_indxs[1]+1}")
    else:
        rev_posible = reversible(arr, wrong_indxs)
        if rev_posible:
            print(f"yes\nreverse {rev_posible[0]+1} {rev_posible[1]+1}")
        else:
            print("no")
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
