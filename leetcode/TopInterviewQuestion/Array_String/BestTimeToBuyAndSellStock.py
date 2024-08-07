with open('../input.txt','r') as f:
    lines = f.readlines()
prices = list(map(int, lines[0].split(',')))

# Easiest way (but tle)
'''
maxProfit = 0
for i in range(len(prices)-1):
    for j in range(i+1, len(prices)):
        profit = prices[j]-prices[i]
        if profit > maxProfit:
            print(prices[j]-prices[i])
            maxProfit = profit
print(maxProfit)
'''

buyPrice = prices[0]
maxProfit = 0
for price in prices:
    if price<buyPrice:
        buyPrice=price
    elif price-buyPrice > maxProfit:
        maxProfit = price-buyPrice
print(maxProfit)