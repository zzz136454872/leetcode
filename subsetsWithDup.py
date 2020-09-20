from typing import *

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def subset(table):
            if len(table)==0:
                return [[]]
            i=0
            while i<len(table) and table[i]==table[0]:
                i+=1
            tmp=subset(table[i:])
            out=[]
            for j in range(i+1):
                out+=[table[:j]+t for t in tmp]
            return out
        return subset(nums)

sl=Solution()
nums=[1,2,2]
print(sl.subsetsWithDup(nums))
