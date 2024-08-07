with open('../input.txt','r') as f:
    lines = f.readlines()
prices = list(map(int, lines[0].split(',')))

maxProfit = 0
for i in range(1, len(prices)):
    if prices[i]>prices[i-1]:
        maxProfit+=prices[i]-prices[i-1]
print(maxProfit)