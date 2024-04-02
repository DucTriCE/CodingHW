#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    # Write your code here
    print(sum([j>0 for j in arr])/len(arr))
    print(sum([j<0 for j in arr])/len(arr))
    print(sum([j==0 for j in arr])/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
