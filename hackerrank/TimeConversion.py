#!/bin/python3

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
    # Write your code here
    time, s = s[-2:], s[-10:-2]
    if time == 'AM' and s[0:2]=='12':
        print("00:"+s[3:])
    elif time == 'PM' and int(s[0:2])>=1 and int(s[0:2])<=11:
        print(str(int(s[0:2])+12)+":"+s[3:])
    else:
        print(s)
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    # fptr.write(result + '\n')
    # fptr.close()
