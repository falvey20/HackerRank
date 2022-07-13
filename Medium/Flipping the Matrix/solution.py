import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    n = len(matrix)//2
    
    result = 0
    for i in range(0, n):
        for j in range(0, n):
            nw = matrix[i][j]
            ne = matrix[i][len(matrix)-1 - j]
            se = matrix[len(matrix)-1 - i][len(matrix)-1 - j]
            sw = matrix[len(matrix)-1 - i][j]
            result += max(nw, ne, se, sw)
    return result
            
              

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
