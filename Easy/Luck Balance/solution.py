import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    luck = 0
    important = []
    for i in contests:
        if i[1] == 0:
            luck += i[0]
        elif i[1] == 1:
            important.append(i[0])
    important = sorted(important)
    if k > len(important):
        luck += sum(important)
    else: 
        for i in range(k):
            highest = important.pop()
            luck += highest
        luck -= sum(important)
    return luck
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
