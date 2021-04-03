from typing import *
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mem=[[-1]*(len(text2)+1) for i in range(len(text1)+1)]
        
        def lcs(i,j):
            if i==0 or j==0:
                return 0
            if mem[i][j]!=-1:
                return mem[i][j]
            if text1[i-1]==text2[j-1]:
                out=lcs(i-1,j-1)+1
            else:
                out=max(lcs(i,j-1),lcs(i-1,j))
            mem[i][j]=out
            return out
        return lcs(len(text1),len(text2))

sl=Solution()
text1 = "abc"
text2 = "def" 
print(sl.longestCommonSubsequence(text1,text2))
        
