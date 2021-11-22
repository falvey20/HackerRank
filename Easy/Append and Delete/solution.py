import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Establish how many chars are shared at start of strings.
    shared_start = 0
    for s_char, t_char in zip(s, t):
        if s_char == t_char:
            shared_start += 1
        else:
            break
    
    s_diff = len(s)-shared_start
    t_diff = len(t)-shared_start
    total_diff = s_diff+t_diff
    # If k is greater or equal to total diff and is also equivalent ODD/EQUAL
    # Or if k longer than both combined strings, as can still remove from empty string.
    # Essentially able to counteract being odd/even.
    if (total_diff <= k and total_diff%2 == k%2) or k > len(s)+len(t):
        return "Yes"
    return "No"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
