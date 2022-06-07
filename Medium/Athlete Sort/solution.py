import math
import os
import random
import re
import sys
from operator import itemgetter

def athlete_sort(arr, k):
    order_by_k = sorted(arr, key=itemgetter(k))
    for i in order_by_k:
        print(' '.join(map(str, i)))
        

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    athlete_sort(arr, k)
