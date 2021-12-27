import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if s[:2] == "12":
        if s[-2:]== "AM":
            new_hour = "00"
        else:
            new_hour = "12"
        return f"{new_hour}{s[2:-2]}"
        
    elif s[-2:] == "AM":
        return s[:-2]
        
    else:
        new_hour = str(int(s[:2]) + 12)
        return f"{new_hour}{s[2:-2]}"
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
