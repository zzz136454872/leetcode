from typing import *

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        m=0
        log=[0 for i in range(26)]
        def c2n(a):
            return ord(a)-ord('A')
        while r<len(s):
            log[c2n(s[r])]+=1
            m=max(m,log[c2n(s[r])])
            r+=1
            if r-l-m>k:
                log[c2n(s[l])]-=1
                l+=1
            # print(l,r,m,k)
        return r-l

sl=Solution()
s="AABABBA"
k=1
print(sl.characterReplacement(s,k))

