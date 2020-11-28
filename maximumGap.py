from typing import *

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        nums.sort()
        out=0
        for i in range(len(nums)-1):
            out=max(out,nums[i+1]-nums[i])
        return out

sl=Solution()
nums=[3,6,9,1]
print(sl.maximumGap(nums))

