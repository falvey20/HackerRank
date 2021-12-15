import math
import os
import random
import re
import sys

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(s):
    num_vals = [ord(i) for i in s]
    # print(num_vals)
    
    result = 0
    
    # Iterate from start and end.
    for i in range(0, int(len(s)//2)):
        if num_vals[i] != num_vals[len(s)-i-1]:
            result += abs(num_vals[i] - num_vals[len(s)-i-1])
    
    return result
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
