import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
# Its digits can only be 3's and/or 5's.
# The number of 3's it contains is divisible by 5.
# The number of 5's it contains is divisible by 3.
# It is the largest such number for its length.

def decentNumber(n):
    if n <= 2 or n == 4:
        return print(-1)
    elif n == 5:
        return print('3'*5)
    elif n % 3 == 0:
        return print('5'*n)
    else:
        i = n
        while i > 3:
            i -= 5
            if i % 3 == 0:
                return print(('5'*i) + ('3'*(n-i)))
    return print(-1)
    
     

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
