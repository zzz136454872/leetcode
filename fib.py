from typing import *

class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        log=[0 for i in range(n+1)]
        log[0]=0
        log[1]=1
        for i in range(2,n+1):
            log[i]=log[i-1]+log[i-2]
        return log[n]
