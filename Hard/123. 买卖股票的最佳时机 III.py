class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        firstbuy, firstsell = -sys.maxsize, 0
        secbuy, secsell = -sys.maxsize, 0
        for i in prices:
            firstbuy = max(firstbuy,-i)
            firstsell = max(firstsell, firstbuy + i)
            secbuy = max(secbuy, firstsell - i)
            secsell = max(secsell,secbuy + i)
        return secsell
                
