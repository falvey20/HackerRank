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
    hour, minute, secondsAMPM = s.split(':') 
    if secondsAMPM[2:] == "PM" and hour != '12': 
        hour = str(int(hour) + 12) 
    if secondsAMPM[2:] == "AM" and hour == '12': 
        hour = "00" 
    if secondsAMPM[2:] == "PM" and hour == '12': 
        hour = "12" 
    
    new_time = hour + ':' + minute + ':' + secondsAMPM[0:2] 
        
    return new_time

        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
