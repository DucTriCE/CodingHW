#!/bin/python3

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
    k%=26
    tmp = ''
    for i in range(len(s)):
        if s[i]>='a' and s[i]<='z':
            if ord(s[i])+k>ord('z'):
                tmp += chr(ord(s[i])+k-26)
            else:
                tmp += chr(ord(s[i])+k)
        elif s[i]>='A' and s[i]<='Z':
            if ord(s[i])+k>ord('Z'):
                tmp += chr(ord(s[i])+k-26)
            else:
                tmp += chr(ord(s[i])+k)
        else:
            tmp+=s[i]
    print(tmp)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    # fptr.write(result + '\n')

    # fptr.close()

