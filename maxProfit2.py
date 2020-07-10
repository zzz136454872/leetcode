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
     
sl=Solution()
prices=[1,2,3,0,2]
print(sl.maxProfit(prices))
