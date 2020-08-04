from typing import *

class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        out=0
        m=10**9+7
        n=len(A)
        exp=[1 for i in range(n)]
        A.sort()
        for i in range(1,n):
            exp[i]=2*exp[i-1]%m
        for i in range(n):
            out=(out+A[i]*(exp[i]-exp[n-i-1]))%m
        return out

sl=Solution()
inp=[2,1,3]
print(sl.sumSubseqWidths(inp))
