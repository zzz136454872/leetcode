from typing import *

class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        if primeFactors<=4:
            return primeFactors
        index=primeFactors//3
        rest=primeFactors%3
        times=1
        if rest==1:
            index-=1
            times=4
        elif rest==2:
            times=2
        mod=10**9+7
        def quick_mod(a,b,c):
            ans=1
            while b!=0:
                if b&1:
                    ans=(ans*a)%c
                b>>=1
                a=(a*a)%c
            return ans
        
        return (quick_mod(3,index,mod)*times)%mod

inp=8
sl=Solution()
print(sl.maxNiceDivisors(inp))

                    
        
