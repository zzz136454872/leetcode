
from typing import *
class Solution:
    # 该算法超时
    def createSortedArray(self, instructions: List[int]) -> int:
        log=[]
        cost=0
        def bs1(start,end):
            while start<=end:
                mid=(start+end)//2
                if log[mid]<num:
                    start=mid+1
                else:
                    end=mid-1
            return start
        def bs2(start,end):
            while start<=end:
                mid=(start+end)//2
                if log[mid]<=num:
                    start=mid+1
                else:
                    end=mid-1
            return start
        for num in instructions:
            l=bs1(0,len(log)-1)
            r=bs2(0,len(log)-1)
            cost+=min(l,len(log)-r)
            log.insert(l,num)
        return cost%(10**9+7)

sl=Solution()
instructions = [1,3,3,3,2,4,2,1,2]
out=sl.createSortedArray(instructions)
print(out)
