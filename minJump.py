from typing import *

class Solution:
    def minJump(self, jump: List[int]) -> int:
        n=len(jump)
        dp=[123456 for i in range(n)]
        for i in range(n-1,-1,-1):
            if i+jump[i]>=n:
                dp[i]=1
            else:
                dp[i]=dp[jump[i]+i]+1
            for j in range(i+1,n):
                if dp[j]>=dp[i]+1:
                    dp[j]=dp[i]+1
                else:
                    break
        return dp[0]

jump = [2, 5, 1, 1, 1, 1]
sl=Solution()
print(sl.minJump(jump))
