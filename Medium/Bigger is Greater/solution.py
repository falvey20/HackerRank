import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # convert w to list of chars
    chars = [str(i) for i in w]
    # highest possible order
    highest = sorted(list(w), reverse=True)
    
    # if w is already highest possible order return no answer
    if w == ''.join(highest):
        return "no answer"    
    
    # iterating from end of list, j i always position prior to i
    for i in range(len(chars)-1, 0, -1):
        j = i-1
        if chars[i]>chars[j]:
            # get list of character from j onwards
            j_and_after = [l for l in chars[j:]]
            # string up until if condition met
            start = ''.join([l for l in chars[:j]])
            # establish the next highest value in character after j
            next_highest = str(min([l for l in chars[j:] if l>chars[j]]))
            #remove the next highest number from remainder of chars
            j_and_after.remove(next_highest)
            # sort remainder of chars to lowest possible order
            end = ''.join(l for l in sorted(j_and_after))
            return start + next_highest + end
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
