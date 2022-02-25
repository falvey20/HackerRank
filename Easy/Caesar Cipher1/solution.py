import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
def caesarCipher(s, k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if k > 26: 
        k = k%26
    new_alphabet = alphabet[k:] + alphabet[0:k]
    
    result = ''
    
    for char in s:
        if char.isalpha():
            if char.isupper():
                result += new_alphabet[alphabet.index(char.lower())].upper()
            else:
                result += new_alphabet[alphabet.index(char)]
        else:
            result += char
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
