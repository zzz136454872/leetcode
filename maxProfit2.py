from typing import *

# best time to buy and sale with cooldown. 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days=len(prices)
        if days<=1:
            return 0
        hold=[0 for i in range(days)]
        unhold=[0 for i in range(days)]
        hold[0]=-prices[0]

        for i in range(1,days):
            hold[i]=max(hold[i-1],-prices[i]+(unhold[i-2] if i>=2 else 0))
            unhold[i]=max(unhold[i-1],hold[i]+prices[i])

        return unhold[-1]

# 买卖股票的最佳时机含手续费
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        days=len(prices)
        if days<=1:
            return 0
        hold=-prices[0]
        unhold=0
        for i in range(1,days):
            next_hold=max(hold,unhold-prices[i])
            next_unhold=max(unhold, hold+prices[i]-fee)
            hold=next_hold
            unhold=next_unhold
        return unhold
     
sl=Solution()
# prices=[1,2,3,0,2]
prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(sl.maxProfit(prices,fee))
