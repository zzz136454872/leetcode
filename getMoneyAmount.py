from typing import *

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        table=[[-1 for j in range(n+1)] for i in range(n+1)]
        def recursion(y,x):
            if y>=x:
                return 0
            if table[y][x]>=0:
                return table[y][x]
            out=123456
            for i in range(y,x+1):
                out=min(out,i+max(recursion(y,i-1),recursion(i+1,x)))
            table[y][x]=out
            return out
        return recursion(1,n)

sl=Solution()
print(sl.getMoneyAmount(7))
            
