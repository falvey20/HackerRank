import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    values = set(b)

    for i in values:
        if i != "_" and b.count(i)<2:
            return "NO"
    
    if "_" in values:
        return "YES"
    else:
        for i in range(1, len(b)-1):
            if b[i] != b[i-1] and b[i] != b[i+1]:
                return "NO"
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
