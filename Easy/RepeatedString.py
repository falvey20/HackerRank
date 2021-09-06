import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    a_in_difference = 0
    
    difference = n % len(s)
    a_count_s = 0
    for char in s:
        if char == 'a':
            a_count_s += 1
            
    for char in s[:difference]:
        if char == 'a':
            a_in_difference += 1
            
    total = a_in_difference + (a_count_s * (n//len(s)))
    return total
    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
