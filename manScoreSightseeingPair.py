
from typing import *

class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        left=A[0]
        target=0
        for i in range(1,len(A)):
            target=max(target,A[i]-i+left)
            print('target',target)
            left=max(left,A[i]+i)
            print('left',left)
            
        return target
inp=[8,1,5,2,6]
sl=Solution()
print(sl.maxScoreSightseeingPair(inp))



            
