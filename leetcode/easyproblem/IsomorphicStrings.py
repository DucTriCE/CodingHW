if __name__ == '__main__':
    s = input()
    t = input()
    mp1 = []
    mp2 = []
    for ch in s:
        mp1.append(s.index(ch))
    for ch in t:
        mp2.append(t.index(ch))
    
    if mp1 == mp2:
        print(True)
    else:
        print(False)