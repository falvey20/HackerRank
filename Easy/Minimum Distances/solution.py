import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    minimum = -1
    
    for i in range(0, len(a)-1):
        for j in range(i+1, len(a)):
            if a[i]==a[j]:
                distance = j-i
                if minimum == -1:
                    minimum = distance
                else:
                    if distance < minimum:
                        minimum = distance
    return minimum
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
