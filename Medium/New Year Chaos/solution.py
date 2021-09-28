import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    bribes = 0
    
    q = [i-1 for i in q]
    for pos, val in enumerate(q):
        if val - pos > 2:
            return print("Too chaotic")
        for i in q[max(val-1, 0):pos]:
            if i > val:
                bribes += 1
                
    return print(bribes)
    
    

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
