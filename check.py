from typing import *

class Solution:
    def check(self, nums: List[int]) -> bool:
        out=0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                test=nums[i:]+nums[:i]
                for j in range(1,len(nums)):
                    if test[j]<test[j-1]:
                        return False
                return True
        return True

sl=Solution()
nums = [3,4,5,1,2]
# nums = [2,1,3,4]
print(sl.check(nums))
