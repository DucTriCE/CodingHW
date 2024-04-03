#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def checkPalindrome(s):
    left, right =  0, len(s)-1
    while (left<=right):
        if s[left]==s[right]:
            left+=1
            right-=1
        else:
            return False
    return True

def palindromeIndex(s):
    # Write your code here
    if checkPalindrome(s):
        return -1
    else:
        for i in range(len(s)):
            tmp = s[:i] + s[i+1:]
            if checkPalindrome(tmp):
                return i
        return -1



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)
        print(result)
    #     fptr.write(str(result) + '\n')

    # fptr.close()
