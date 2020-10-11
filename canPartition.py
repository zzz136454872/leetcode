from typing import *

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==0:
            return True
        s=sum(nums)
        if n<2 or s%2!=0:
            return False
        target=s//2
        log=[[False for j in range(target+1)] for i in range(n+1)]
        log[0][0] = True
        for i in range(1,n+1):
            for j in range(target+1):
                if log[i-1][j] or (j>=nums[i-1] and log[i-1][j-nums[i-1]]):
                    log[i][j]=True
        return log[-1][-1]

nums=[1, 5, 11, 5]
nums=[1, 2, 5]
sl=Solution()
print(sl.canPartition(nums))

        
        

