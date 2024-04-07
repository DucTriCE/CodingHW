if __name__ == '__main__':
    # Add your code here
    strs = list(map(str, input().split()))
    di = dict()
    for str in strs:
        lst = [0]*26
        for ch in str:
            lst[ord(ch)-ord('a')]+=1
        key = tuple(lst)
        if key not in di:
            di[key] = []
        di[key].append(str)
    ans = []
    for value in di.values():
        ans.append(value)
    print(ans)
        
