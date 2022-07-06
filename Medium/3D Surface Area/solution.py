import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#1 3 4
#2 2 3
#1 2 4

def surfaceArea(A):
    area = 0
    for row in range(0, len(A)):
        for col in range(0, len(A[0])):
            a = 0
            #top + bottom
            if A[row][col] != 0:
                a += 2
            else:
                continue
            #front
            if col == 0:
                a += A[row][col]
            elif A[row][col] > A[row][col-1]:
                a += A[row][col] - A[row][col-1]
            #back
            if col == len(A[0])-1:
                a += A[row][col]
            elif A[row][col] > A[row][col+1]:
                a += A[row][col] - A[row][col+1]
            #left
            if row == 0:
                a += A[row][col]
            elif A[row][col] > A[row-1][col]:
                a += A[row][col] - A[row-1][col]
            #right
            if row == len(A)-1:
                a += A[row][col]
            elif A[row][col] > A[row+1][col]:
                a += A[row][col] - A[row+1][col]
            area += a
    return area
              

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
