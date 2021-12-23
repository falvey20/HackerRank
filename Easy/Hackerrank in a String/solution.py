import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def hackerrankInString(s):
    hr = [char for char in 'hackerrank']
    p = 0
    
    for i in range(0, len(s)):
        if s[i] == hr[p]:
            p += 1
            if p == len(hr):
                return "YES"
    return "NO"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
