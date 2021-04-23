from typing import *

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        log=[1]*len(nums)
        pre=[-1]*len(nums)
        nums.sort()
        for i in range(1,len(nums)):
            for j in range(i-1,-1,-1):
                if nums[i]%nums[j]==0:
                    if log[i]<log[j]+1:
                        log[i]=log[j]+1
                        pre[i]=j
        maxValue=1
        maxLoc=0
        for i in range(len(nums)):
            if maxValue<log[i]:
                maxValue=log[i]
                maxLoc=i
        out=[]
        loc=maxLoc
        while loc!=-1:
            out.append(nums[loc])
            loc=pre[loc]
        return out


nums = [1,2,4,8]
sl=Solution()
print(sl.largestDivisibleSubset(nums))

