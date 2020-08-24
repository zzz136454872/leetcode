from typing import *

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        r=len(nums)-1
        now=0
        while now<=r:
            if nums[now]==2:
                nums[now],nums[r]=nums[r],nums[now]
                r-=1
            elif nums[now]==0:
                nums[now],nums[l]=nums[l],nums[now]
                l+=1
                now+=1
            else:
                now+=1

sl=Solution()
nums=[0,1,0,1,0]
sl.sortColors(nums)
print(nums)
            
