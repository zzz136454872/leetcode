from typing import *

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        log=[]
        out=0
        for num in nums:
            start=0
            end=len(log)-1
            while start<=end:
                mid=(start+end)//2
                if log[mid]>num:
                    start=mid+1
                else:
                    end=mid-1
            out+=start
            log.insert(start,num)
        return out

inp=[1,3,2,3,1]
sl=Solution()
print(sl.reversePairs(inp))
            
