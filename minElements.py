from typing import *

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        need=abs(goal-sum(nums))
        last=need//limit
        if last*limit==need:
            return last
        return last+1

sl=Solution()
nums = [1,-10,9,1]
limit = 100
goal = 0
nums = [1,-1,1]
limit = 3
goal = -4
print(sl.minElements(nums,limit,goal))
