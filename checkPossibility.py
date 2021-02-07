from typing import *

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flag=0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                if not flag:
                    if i<=1 or nums[i-2]<=nums[i]:
                        nums[i-1]=nums[i]
                    flag=1
                    nums[i]=nums[i-1]
                else:
                    return False
        return True

sl=Solution()
nums = [4,2,3]
print(sl.checkPossibility(nums))

