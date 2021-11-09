import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    text=s.replace(" ","")
    cols=int(math.ceil(math.sqrt(len(text))))
    rows=int(cols)-1
    
    subs = ""
    for j in range(0, rows+1):
        subs += text[j::cols]+" "
    return(subs)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
