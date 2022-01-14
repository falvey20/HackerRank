import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    result = 0
    combos = []
    for i in range(0, len(s)):
        for j in range(i+1, len(s)+1):
            combos.append(str(sorted(s[i:j])))      
    
    for i in set(combos):
        result += sum(range(combos.count(i)))
    return result   
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
