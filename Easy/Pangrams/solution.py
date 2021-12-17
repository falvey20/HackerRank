import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # lowercase s, remove spaces, get set of chars, sort and rejoin.
    s_char_set = "".join(sorted(set(s.lower().replace(" ", ""))))
    
    if s_char_set == alphabet:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
