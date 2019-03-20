class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or len(prices) < 2:
            return 0
        else:
            minprice, maxprofit = prices[0], 0
            for i in prices:
                if i <= minprice:
                    minprice = i
                elif i - minprice > maxprofit:
                    maxprofit = i - minprice
        return maxprofit
