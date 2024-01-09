class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        profit = 0

        for i in range(len(prices)-1):
            if prices[r]<prices[l]:
                l=r
                r+=1
            else:
                profit = max(profit, prices[r]-prices[l])
                r+=1
        return profit
