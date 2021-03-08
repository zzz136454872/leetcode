from typing import *

class Solution:
    def minCut(self, s: str) -> int:
        log=[[True for j in s] for i in s]

        for i in range(len(s)-2,-1,-1):
            for j in range(i+1,len(s)):
                if s[i]!=s[j] or not log[i+1][j-1]:
                    log[i][j]=False

        #print(log)
        cuts=[12345678 for i in s]
        cuts[0]=0
        for i in range(1,len(s)):
            if log[0][i]:
                cuts[i]=0
                continue
            for j in range(i,0,-1):
                if log[j][i]:
                    cuts[i]=min(cuts[i],cuts[j-1]+1)
        return cuts[-1]

sl=Solution()
s = "aababb"
print(sl.minCut(s))
        
