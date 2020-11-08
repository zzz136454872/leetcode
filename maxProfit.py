from typing import *

# 买卖股票的最佳时机
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 100000000
        profit=0
        for price in prices:
            min_price=min(min_price,price)
            profit=max(profit,price-min_price)
        return profit

# 买卖股票的最佳时机II

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        preMin=100000
        last=100000
        out=0
        for i in range(len(prices)):
            if prices[i]>last:
                last=prices[i]
                continue
            out+=last-preMin
            last=prices[i]
            preMin=last
        out+=last-preMin
        return out

        
sl=Solution()
prices=[7,1,5,3,6,4]
print(sl.maxProfit(prices))
