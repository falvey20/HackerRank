import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    result = []
    for num in range(p, q+1):
        sqr = str(num**2)
        right = sqr[len(sqr)//2:]
        left = 0 if sqr[:len(sqr)//2]=='' else sqr[:len(sqr)//2]
        if int(right)+int(left)==num:
            result.append(num)
    if len(result) == 0:
        print("INVALID RANGE")
    else:
        print(" ".join(str(num) for num in result))

        
if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
