def isAnagram(s, t):
    s = sorted(s)
    t = sorted(t)
    return s == t
if __name__ == '__main__': 
    s, t = input(), input()
    print(isAnagram(s, t))