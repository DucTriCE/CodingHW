if __name__ == '__main__':
    # Add your code here
    prices = list(map(int, input().split()))
    ans = 0
    for i in range(1,len(prices)):
        print(prices[i], prices[i-1])
        if prices[i]>prices[i-1]:
            ans+=prices[i]-prices[i-1]
    print(ans)