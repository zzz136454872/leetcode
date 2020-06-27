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
        # nums.sort()
        # get=0
        # for i in range(len(nums)):
        #     if(nums[i] <= 0):
        #         continue
        #     if nums[i]>get+1:
        #         return get+1
        #     get=nums[i]
        # return get+1
        
        n=len(nums)
        if n==0:
            return 1
        flag=(nums[0]==n)
        i=0
        while i<n:
            if nums[i]!=i and nums[i]<n and nums[i]>=0 and nums[i]!=nums[nums[i]]:
                tmp=nums[i]
                nums[i]=nums[nums[i]]
                nums[tmp]=tmp
            else:
                i+=1
        for i in range(1,n):
            if i != nums[i]:
                return i
        if flag or nums[0]==n:
            return n+1
        else:
            return n

nums = [1,2,3]#,-1,1]
sl=Solution()
print(sl.firstMissingPositive(nums))

