from typing import *

class Solution:
    def rob(self, nums: List[int]) -> int:
        log = [0 for i in range(len(nums))]
        m=0
        for i in range(len(nums)):
            if i<=1:
                log[i]=nums[i]
            else:
                log[i]=nums[i]+max(log[:i-1])
            m=max(m,log[i])
        return m
inp=[2,1,1,2]
sl=Solution()
print(sl.rob(inp))
                
