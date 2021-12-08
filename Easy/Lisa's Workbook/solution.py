import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    pages = []
    specials = 0
    
    # create pages of max length k for each problem in each chapter.
    for chapter in arr:
        page = []
        for i in range(1, chapter+1):
            page.append(i)
            if len(page) == k:
                pages.append(page)
                page = []
            elif i == chapter:
                pages.append(page)
    
    # check if problem numbers correspond to page numbers.            
    for i in range(0, len(pages)):
        if i+1 in pages[i]:
            specials += 1
            
    return specials
    
       


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
