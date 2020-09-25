from typing import *

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.append(1)
        nums=[1]+nums
        n=len(nums)
        log=[[0 for k in range(n)] for i in range(n)]
        def rs(begin, end):
            if begin>=end-1:
                return 0
            if log[begin][end]!=0:
                return log[begin][end]
            out=0
            for i in range(begin+1,end):
                out=max(out,rs(begin,i)+rs(i,end)+nums[begin]*nums[i]*nums[end])
            log[begin][end]=out
            return out
        return rs(0,n-1)

nums=[3,1,5,8]
sl=Solution()
print(sl.maxCoins(nums))
