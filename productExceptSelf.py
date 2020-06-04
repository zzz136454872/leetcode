from typing import *
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tmp=1
        log=[1 for i in range(len(nums))]
        for i in range(len(nums)):
            log[i]=tmp;
            tmp=tmp*nums[i]
        tmp=1
        for i in range(len(nums)-1,-1,-1):
            log[i]=tmp*log[i]
            tmp=tmp*nums[i]
        return log
inp=[1,2,3,4]
sl=Solution()
print(sl.productExceptSelf(inp))

