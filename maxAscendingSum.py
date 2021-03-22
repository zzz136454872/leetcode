from typing import *

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum=nums[0]
        now_sum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                now_sum+=nums[i]
            else:
                now_sum=nums[i]
            max_sum=max(now_sum,max_sum)

        return max_sum

                
