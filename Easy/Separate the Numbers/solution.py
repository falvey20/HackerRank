import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    if len(s) == 1:
        print("NO")
        return
    
    for i in range(1, len(s)//2 + 1):
        new_s = s[:i]
        prev = int(new_s)
        
        while len(new_s) < len(s):
            next_num = prev + 1
            new_s += str(next_num)
            prev = next_num
            
        if new_s == s:
            print(f"YES {s[:i]}")
            return
    print("NO")
        

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
