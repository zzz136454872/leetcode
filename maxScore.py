from typing import *

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        log1=[0 for i in range(n+1)]
        log2=[0 for i in range(n+1)]
        tmp=0
        for i in range(n):
            tmp+=cardPoints[i]
            log1[i+1]=tmp
        tmp=0
        for i in range(n-1,-1,-1):
            tmp+=cardPoints[i]
            log2[i]=tmp
        out=0
        # print(log1)
        # print(log2)
        for i in range(k+1):
            out=max(out,log1[i]+log2[n-k+i])
            # print(i,out)
        return out

sl=Solution()
cardPoints = [1,79,80,1,1,1,200,1]
k = 3
print(sl.maxScore(cardPoints,k))

