class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=-prices[0]
        sell=0
        for price in prices:
            buy = max(buy,-price)#cheapest cost at which u can buy a stock
            sell = max(sell,buy+price)#calculates max profit
        return sell