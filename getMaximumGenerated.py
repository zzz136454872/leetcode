from typing import *

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        log=[0 for i in range(n+1)]
        log[1]=1
        for i in range(2,n+1):
            if i%2==0:
                log[i]=log[i//2];
            else:
                log[i]=log[i//2]+log[i//2+1]
        print(log)
        return max(log)

sl=Solution()
print(sl.getMaximumGenerated(7))
            
