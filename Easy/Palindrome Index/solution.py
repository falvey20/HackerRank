import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    l = len(s)
    i, j = 0, l-1
    
    while i < l:
        if s[i] != s[j]:
            break
        i += 1
        j -= 1
    if i > j:
        return -1
    # check if substring between i and j inclusive is palindrome.
    # if so return i
    x = i+1
    y = j
    while x < j and y > i+1:
        if s[x] != s[y]:
            return j
        x += 1
        y -= 1
    return i
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
