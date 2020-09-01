from typing import *

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)
        log=[[None for j in range(n)] for i in range(n)]

        def get(i,j):
            if i>j:
                return 0
            if log[i][j]!=None:
                return log[i][j]
            m=max(nums[i]-get(i+1,j),nums[j]-get(i,j-1))
            log[i][j]=m
            return m
        return get(0,n-1)>=0

nums=[1, 5, 233, 7]
nums=[1, 5, 2]
sl=Solution()
print(sl.PredictTheWinner(nums))
