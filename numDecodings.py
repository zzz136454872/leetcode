from typing import *

class Solution:
    def numDecodings(self, s: str) -> int:
        log=[0]*(len(s)+1)
        log[0]=1
        if s[0]=='0':
            return 0
        else:
            log[1]=1
        table={str(i) for i in range(1,27)}
        for i in range(1,len(s)):
            if s[i] in table:
                log[i+1]=log[i]
            if s[i-1:i+1] in table:
                log[i+1]+=log[i-1]
        # print(log)
        return log[-1]

sl=Solution()
s = "12"
print(sl.numDecodings(s))
            
