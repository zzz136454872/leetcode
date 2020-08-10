from typing import *

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s)==0:
            return 0
        out=0
        count_now=1
        count_last=0
        i=1
        now=s[0]
        for i in range(1,len(s)):
            if s[i]==now:
                count_now+=1
            else:
                now=s[i]
                out+=min(count_last,count_now)
                count_last=count_now
                count_now=1
        out+=min(count_last,count_now)
        return out

inp="100111001"
sl=Solution()
print(sl.countBinarySubstrings(inp))
