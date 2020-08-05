from typing import *

# not working!!!

class Solution:
    def subarraysWithKDistinct(self, A: List[int], k: int) -> int:
        n=len(A)
        log=[0 for i in range(n)]
        start=0
        end=0
        count=0
        out=0
        while end<n or count>=k:
            if count<k:
                tmp=A[end]
                end+=1
                if log[tmp]==0:
                    count+=1
                log[tmp]+=1
            elif count>k:
                tmp=A[start]
                start+=1
                log[tmp]-=1
                if log[tmp]==0:
                    count-=1
            if count==k:
                out+=1
                print(log)
                if end<n:
                    tmp=A[end]
                    end+=1
                    if log[tmp]==0:
                        count+=1
                    log[tmp]+=1
                else:
                    tmp=A[start]
                    start+=1
                    log[tmp]-=1
                    if log[tmp]==0:
                        count-=1
        return out
A = [1,2,1,2,3]
K = 2
sl=Solution()
print(sl.subarraysWithKDistinct(A,K))
