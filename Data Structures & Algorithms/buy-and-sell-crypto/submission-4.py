class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = 0
        for i in range(len(prices) - 1):
            price = max(price, max(prices[i+1:]) - prices[i])
        return price
        