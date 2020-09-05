from typing import *

class Solution:
    def jump(self, nums: List[int]) -> int:
        count=[30000 for i in range(len(nums))]
        count[0]=0
        for i in range(len(nums)):
            if i>0 and nums[i]<nums[i-1]:
                continue
            for j in range(i+1,nums[i]+i+1):
                if j>=len(nums):
                    break
                if count[i]+1<count[j]:
                    count[j]=count[i]+1
        return count[-1]

inp=[2,3,1,1,4]
sl=Solution()
print(sl.jump(inp))

