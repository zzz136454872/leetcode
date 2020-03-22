from typing import *
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if len(A)==0:
            return 0
        A.sort()
        now=A[0]-1
        out=0
        #print(A)
        for num in A:
            #print("num",num,"now",now,"out",out)
            if num<=now:
                out+=now+1-num
                now+=1
            else:
                now=num
        return out


inp=[3,2,1,2,1,7]
sl=Solution()
print(sl.minIncrementForUnique(inp))

            
        
