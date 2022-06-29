import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'beautifulPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY A
#  2. INTEGER_ARRAY B
#

def beautifulPairs(A, B):
    A = sorted(A)
    B = sorted(B)
    ac = Counter(A)
    bc = Counter(B)
    
    result = 0
    spare = 0
    
    for i in ac:
        if i in bc:
            result += min(ac[i], bc[i])
        else:
            spare += 1
                
    if spare:
        return result + 1
    else:
        return result - 1
        
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
