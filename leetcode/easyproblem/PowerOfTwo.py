import math
def isPowerOfTwo(n):
    if math.log2(n).is_integer():
        return True
    return False
    # return  (n>0 && (n & (n-1))==0) ? true:false;
    # '&' operator between multiple of two and next lower numbers always give 0

if __name__ == '__main__':
    n = int(input())
    flag = isPowerOfTwo(n)
    print(flag)