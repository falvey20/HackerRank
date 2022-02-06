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
    hour, ampm = s[:2], s[-2:]
    
    if hour == '12' and ampm == 'AM':
        hour = '00'
    elif ampm == 'PM' and hour != '12':
        hour = str(int(hour) + 12)
    
    return f"{hour}{s[2:-2]}"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
