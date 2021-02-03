from typing import *

import bisect
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        m1=k//2
        m2=(k-1)//2
        
        def median(log):
            return (log[m1]+log[m2])/2
        
        out=[]
        log=nums[:k]
        log.sort()
        out.append(median(log))
        l=0
        r=k
        for i in range(len(nums)-k):
            ll=bisect.bisect_right(log,nums[l])
            log.pop(ll-1)
            bisect.insort(log,nums[r])
            l+=1
            r+=1
            out.append(median(log))
        return out

sl=Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(sl.medianSlidingWindow(nums,k))

            
