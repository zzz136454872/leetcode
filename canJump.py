from typing import *

class Solution:
    def canJump(self, nums: List[int])-> bool:
        if(len(nums)<=1):
            return True
        end=0
        for i in range(len(nums)):
            if i > end:
                return False
            else:
                end=max(i+nums[i],end)
        return True

sl=Solution()
inp=[3,2,1,0,4]
print(sl.canJump(inp))

