from typing import *

def countPrime(n):
    if n<=1:
        return 0
    log=[True for i in range(n+1)]
    log[0]=False
    log[1]=False
    i=2
    while i<n**0.5+1:
        for k in range(2,n//i+1):
            log[k*i]=False
        i+=1
        while i<n and not log[i]:
            i+=1
    return log.count(True)
            
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        num=countPrime(n)
        tmp=num
        out=1
        mod=10**9+7
        while tmp>1:
            out=(out*tmp)%mod
            tmp-=1
        tmp=n-num
        while tmp>1:
            out=(out*tmp)%mod
            tmp-=1
        return out

sl=Solution()
n=2
print(sl.numPrimeArrangements(n))

