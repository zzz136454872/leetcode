from typing import *

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        log=[0]*(target+1)
        log[0]=1
        nums.sort()
        for i in range(1,target+1):
            for j in range(len(nums)):
                if nums[j]<=i:
                    log[i]+=log[i-nums[j]]
                else:
                    break
        return log[-1]

sl=Solution()
nums = [9]
target = 3
nums = [1,2,3]
target = 4
print(sl.combinationSum4(nums,target))

