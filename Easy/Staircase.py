import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for i in range(1, n + 1):
        spaces = n - i
        hashes = i
        string = ""
        for space in range(spaces):
            string += " "
        for hashes in range(hashes):
            string += "#"
        print(string)
        

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
