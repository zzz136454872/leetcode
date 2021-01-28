from typing import *

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        log1=[0 for i in range(n+1)]
        log2=[0 for i in range(n)]
        s=0
        for i in range(n):
            log1[i]=s
            s+=nums[i]
        log1[n]=s
        s=0
        for i in range(n-1,-1,-1):
            log2[i]=s
            s+=nums[i]
        for i in range(n):
            if log1[i]==log2[i]:
                return i
        return -1

nums = [1]
sl=Solution()
print(sl.pivotIndex(nums))
        

