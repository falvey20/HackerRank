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
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    shift = k%len(alphabet)
    
    new_alphabet = alphabet[shift:]+alphabet[0:shift]
    
    result = ""
    for char in s:
        if char.isupper():
            result += new_alphabet[alphabet.index(char.lower())].upper()
        elif char in alphabet:
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
