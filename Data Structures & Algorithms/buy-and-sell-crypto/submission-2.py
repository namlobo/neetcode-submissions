class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''buy=-prices[0]
        sell=0
        for price in prices:
            buy = max(buy,-price)#cheapest cost at which u can buy a stock
            sell = max(sell,buy+price)#calculates max profit
        return sell'''

        
        l,r = 0,1
        maxp=0
        #l = buy, r = sell
        while r<len(prices):
            if prices[l]< prices[r]:
                profit = prices[r]-prices[l]
                maxp = max(maxp,profit)
            else:
                l = r
            r=r+1
        return maxp
        