import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    while True:
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                s = s[:i]+s[i+2:]
                break
        else:
            break
        
    return s if s else "Empty String"
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
