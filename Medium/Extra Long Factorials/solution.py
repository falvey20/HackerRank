import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    total = n
    for i in range(n-1, 1, -1):
        total *= i
    return print(total)
        
if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
