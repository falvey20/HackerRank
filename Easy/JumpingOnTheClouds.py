import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    
    jumps = 0
    current_cloud = 0
    penultimate_cloud = len(c) - 2
    last_cloud = len(c) - 1
    
    while current_cloud < penultimate_cloud:
        if c[current_cloud + 2] == 0:
            current_cloud += 2
        else:
            current_cloud += 1
        jumps += 1
        
    if current_cloud != last_cloud:
        jumps += 1
        
    return jumps
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
