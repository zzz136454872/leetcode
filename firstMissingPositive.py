from typing import *

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #tmp=[]
        #for i in nums:
        #    if i > 0 and i < len(nums)+1:
        #        tmp.append(i)
        #tmp.sort()
        #get=0
        #for i in range(len(tmp)):
        #    if tmp[i]>get+1:
        #        return get+1
        #    get=tmp[i]
        #return get+1
        nums.sort()
        get=0
        for i in range(len(nums)):
            if(nums[i] <= 0):
                continue
            if nums[i]>get+1:
                return get+1
            get=nums[i]
        return get+1

nums = [-1,2,3]
sl=Solution()
print(sl.firstMissingPositive(nums))

