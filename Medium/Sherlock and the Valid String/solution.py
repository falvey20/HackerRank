import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    counts = [s.count(char) for char in set(s)]
    print(counts)
    
    if len(set(counts))==1:
        return "YES"
    
    if len(set(counts))==2:
        if (counts.count(max(counts))==1 and max(counts)-1 == min(counts)) or (counts.count(min(counts))==1 and min(counts)==1):
            return "YES"
        
    return "NO"
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
