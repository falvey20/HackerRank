import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    rev = s[::-1]
    s_abs_diff = []
    rev_abs_diff = []
    
    for i in range(0, len(s)-1):
        s_abs_diff.append(abs(ord(s[i]) - ord(s[i+1])))
        rev_abs_diff.append(abs(ord(rev[i]) - ord(rev[i+1])))
        
    if s_abs_diff == rev_abs_diff:
        return "Funny"
    else:
        return "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
