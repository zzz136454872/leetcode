from typing import *

class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        def c1(loc):
            i=loc
            j=loc
            while i>=0 and j<n and s[i]==s[j]:
                i-=1
                j+=1
            return (j-i)//2
        def c2(loc):
            i=loc
            j=loc+1
            while i>=0 and j<n and s[i]==s[j]:
                i-=1
                j+=1
            return (j-i-1)//2
        out=0
        for i in range(len(s)):
            out+=c1(i)+c2(i)
        return out

