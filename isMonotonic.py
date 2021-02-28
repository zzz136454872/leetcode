from typing import *

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        flag= 0
        for i in range(1,len(A)):
            diff=A[i]-A[i-1]
            if diff*flag<0:
                return False
            if flag==0:
                flag=diff
        return True

sl=Solution()
inp=[1,2,2,2,1]
print(sl.isMonotonic(inp))
