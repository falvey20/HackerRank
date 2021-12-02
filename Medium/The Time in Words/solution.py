import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Hours includes zero to account for 0 in array.
    # Incorporates up to twenty.
    times = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
            'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',                         'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',                   'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine']
    
    # determine if one minute past, quarter, half or o'clock
    if m == 0:
        return f"{times[h]} o' clock"
    elif m == 1:
        return f"{times[m]} minute past {times[h]}"
    elif m == 15:
        return f"quarter past {times[h]}"
    elif m == 45:
        return f"quarter to {times[h+1]}"
    elif m == 30:
        return f"half past {times[h]}"
    
    # if m less than thirty construct string from times 
    # else: 60-m gives remaining minutes 'to' hour+1
    elif m < 30:
        return f"{times[m]} minutes past {times[h]}"
    else:
        return f"{times[60-m]} minutes to {times[h+1]}"
        
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
