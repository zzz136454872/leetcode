from typing import *

# sometimes tle, sometimes ac

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n=len(envelopes)
        if n==0:
            return 0
        envelopes.sort()
        log=[1 for i in range(n)]
        logmax=[0 for i in range(n)]
        for i in range(n):
            before=0
            for j in range(i-1,-1,-1):
                if envelopes[i][0]>envelopes[j][0] and envelopes[i][1]>envelopes[j][1] and log[j]>before:
                    before=log[j]
            log[i]+=before
        return max(log)

sl=Solution()
print(sl.maxEnvelopes(envelopes))
                
        
