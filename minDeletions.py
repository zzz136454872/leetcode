from typing import *

class Solution:
    def minDeletions(self, s: str) -> int:
        log={}
        for l in s:
            if l in log.keys():
                log[l]+=1
            else:
                log[l]=1
        log=list(log.values())
        log.sort()
        log2={}
        out=0
        for n in log:
            if n not in log2.keys():
                log2[n]=1
            else:
                new_n=n-1
                while new_n>0 and new_n in log2.keys():
                    new_n-=1
                out+=n-new_n
                log2[new_n]=0
        return out

s = "ceabaacb"
sl=Solution()
print(sl.minDeletions(s))


