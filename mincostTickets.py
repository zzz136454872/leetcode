
from typing import *

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        if len(days)==0:
            return 0
        dp=[0 for i in range(days[-1]+1)]
        for i in range(1,len(dp)):
            if i not in days:
                dp[i]=dp[i-1] 
                continue
            dp[i]=min(dp[i-1]+costs[0],dp[max(0,i-7)]+costs[1],dp[max(0,i-30)]+costs[2])
        return dp[-1]

days = [1,4,6,7,8,20]
costs = [2,7,15]
sl=Solution()
print(sl.mincostTickets(days,costs))
