from typing import *

class Solution:
    def massage(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums) < 3:
            return max(nums)
        log=[0 for i in range(len(nums))]
        log[0]=nums[0]
        log[1]=nums[1]
        for i in range(2,len(nums)):
            log[i]=max(log[:i-1])+nums[i]
        return max(log)
inp=[2,1,4,5,3,1,1,3]
sl=Solution()
print(sl.massage(inp))
