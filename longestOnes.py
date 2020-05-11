from typing import *

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start=-1
        end=0
        rest=K
        length=0
        while end < len(A):
            if A[end]==0:
                rest-=1
                while(rest<0):
                    start+=1
                    if A[start]==0:
                        rest+=1
            length=max(end-start,length)
            end+=1
        return length

sl=Solution()
A=[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
print(sl.longestOnes(A,3))
