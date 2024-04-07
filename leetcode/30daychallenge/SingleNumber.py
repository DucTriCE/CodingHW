if __name__ == '__main__':
    lst = list(map(int, input().split()))
    ans=0
    for i in lst:
        # print(f"{ans}^{i}={ans^i}")
        ans^=i
    print(ans)