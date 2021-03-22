from typing import *

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        pre_sum=0
        i=0
        while i<len(coins) and pre_sum>=coins[i]-1:
            pre_sum+=coins[i]
            i+=1
        return pre_sum+1

sl=Solution()
nums = [2,3,5,100,101,102]
print(sl.getMaximumConsecutive(nums))
            
