from typing import *

class Solution:
    def numTrees(self, n: int) -> int:
        log=[1 for i in range(n+1)]
        for i in range(2,n+1):
            log[i]=0
            for j in range(i):
                log[i]+=log[j]*log[i-1-j]
        return log[-1]

sl=Solution()
n=3
print(sl.numTrees(3))


