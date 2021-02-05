from typing import *

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        log=[abs(ord(s[i])-ord(t[i])) for i in range(len(s))]
        cost=0
        out=0
        r=0
        for i in range(len(s)):
            while cost<=maxCost:
                out=max(out,r-i)
                if r<len(s):
                    cost+=log[r]
                    r+=1
                else:
                    return out
            cost-=log[i]

        return out
sl=Solution()
s = "abcd"
t = "bcdf"
cost = 3
print(sl.equalSubstring(s,t,cost))
               
                
