
if __name__ == '__main__':
    n = int(input())
    minl = 10e9+1
    maxr = -1
    lst = []
    for i in range(n):
        l, r = map(int, input().split())
        minl = min(minl, l)
        maxr = max(maxr, r)
        lst.append([l, r])
    if [minl, maxr] not in lst:
        print(-1)
    else:
        print(lst.index([minl, maxr])+1)
    
