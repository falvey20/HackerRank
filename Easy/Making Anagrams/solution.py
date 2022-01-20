import math
import os
import random
import re
import sys

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    result = 0
    
    for i in set(s1):
        if s1.count(i) > s2.count(i):
            result += s1.count(i) - s2.count(i)
    for i in set(s2):
        if s2.count(i) > s1.count(i):
            result += s2.count(i) - s1.count(i)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
