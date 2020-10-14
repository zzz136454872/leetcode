from typing import *

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        def n2s(a):
            return chr(a+ord('a'))

        def s2n(a):
            return ord(a)-ord('a')

        def counter(a):
            out=[0 for i in range(26)]
            for c in a:
                out[s2n(c)]+=1
            return out
        count_total=[1234 for i in range(26)]
        for s in A:
            count_now=counter(s)
            count_total=[min(count_now[i],count_total[i]) for i in range(26)]
        out=[]
        for i in range(26):
            out+=count_total[i]*n2s(i)
        return out

A=["cool","lock","cook"]
sl=Solution()
print(sl.commonChars(A))
