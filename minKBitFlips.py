from typing import *

class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        log=[0 for i in range(len(A)+1)]
        out=0
        revCount=0
        for i in range(len(A)):
            revCount+=log[i]
            # print(i,revCount,log[i],A[i])
            if (A[i]+revCount)%2==0:
                # print(i)
                out+=1
                if i+K>len(A):
                    return -1
                log[i+K]-=1
                revCount+=1
                # print(log)
        return out

sl=Solution()
A = [0,0,0,1,0,1,1,0]
K = 3
print(sl.minKBitFlips(A,K))
