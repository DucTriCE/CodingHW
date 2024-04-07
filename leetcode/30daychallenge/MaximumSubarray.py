if __name__ == '__main__':
    # Add your code here
    nums = list(map(int, input().split()))
    ans = tmp = -1e9
    for i in nums:
        tmp = max(tmp+i, i)
        ans = max(ans, tmp)
    print(ans)
    