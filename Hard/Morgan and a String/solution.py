import math
import os
import random
import re
import sys

#
# Complete the 'morganAndString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def morganAndString(a, b):
    result = ""
    la, lb = len(a), len(b)
    i = j = 0
    
    a += "x"
    b += "x"
    
    while i != la and j != lb:
        if a[i:] < b[j:]:
            result += a[i]
            i += 1
        else:
            result += b[j]
            j += 1
            
    result += a[i:-1] + b[j:-1]
        
    print(result)
    return result
            
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)

        fptr.write(result + '\n')

    fptr.close()
