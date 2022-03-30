import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    counts = [s.count(i) for i in set(s)]
    if len(set(counts)) == 1:
        return 'YES'
    if len(set(counts)) > 2:
        return 'NO'
    if len(set(counts)) == 2:
        if counts.count(min(counts)) == len(counts)-1:
            if max(counts) - min(counts) == 1:
                return 'YES'
        elif counts.count(max(counts)) == len(counts)-1:
            if min(counts) == 1:
                return 'YES'
    return 'NO'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
