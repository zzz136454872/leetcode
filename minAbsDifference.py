from typing import *
from time import time

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n=len(nums)
        ln=n//2
        r=nums[ln:]
        rn=n-ln
        def make(lis,loc,lis_out):
            if loc==len(lis):
                return lis_out
            temp=lis_out+[k+lis[loc] for k in lis_out]
            return make(lis,loc+1,temp)
        ll=make(nums[:ln],0,[0])
        rr=make(nums[ln:],0,[0])
        ll.sort()
        rr.sort()
        pl=0
        pr=2**rn-1
        out=1234567890
        while pl<2**ln and pr>=0:
            out=min(out,abs(ll[pl]+rr[pr]-goal))
            if ll[pl]+rr[pr]>goal:
                pr-=1
            else:
                pl+=1
        return out

sl=Solution()
nums = [1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1]
goal = -5
print(sl.minAbsDifference(nums,goal))
