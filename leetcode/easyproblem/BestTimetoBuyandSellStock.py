class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minPrice, maxProfit  = 10001, 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice
        return maxProfit


if __name__ == '__main__':
    pass