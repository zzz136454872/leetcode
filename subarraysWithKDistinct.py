from typing import *

# not working!!!

class Solution:
    def subarraysWithKDistinct(self, A: List[int], k: int) -> int:
        n=len(A)
        log=[0 for i in range(n+1)]
        start=0
        count=0
        out=0
        lend=0
        rend=0
        for i in range(len(A)):
            # print(i)
            while count<k and lend<len(A):
                log[A[lend]]+=1
                if log[A[lend]]==1:
                    count+=1
                lend+=1
            if count<k:
                break
            rend=lend
            while rend<len(A) and log[A[rend]]>0:
                rend+=1
            # print(lend,rend)
            out+=rend-lend+1
            log[A[i]]-=1
            if log[A[i]]==0:
                count-=1
            # print(log,count)
        return out

A=[1,2]
K = 1
sl=Solution()
print(sl.subarraysWithKDistinct(A,K))
