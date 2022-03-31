import math
import os
import random
import re
import sys

# {{()[]}} {{([ 
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    if len(s)%2 != 0:
        return 'NO'
    stack = []
    opens = ['(', '{', '[']
    if s[0] not in opens:
        return 'NO'
    for i in s:
        if i in opens:
            stack.append(i)
        else:
            if len(stack) == 0:
                return 'NO'
            if i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return 'NO'
    if stack:
        return 'NO'
    return 'YES'
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
