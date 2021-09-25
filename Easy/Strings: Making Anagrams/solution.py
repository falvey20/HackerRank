import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    a_counts = Counter(a)
    b_counts = Counter(b)
    
    a_difference = a_counts - b_counts
    b_difference = b_counts - a_counts
    
    return sum(a_difference.values()) + sum(b_difference.values())
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
