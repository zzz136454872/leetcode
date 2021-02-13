from typing import *

mod=10**9+7

def c(i,k):
    out=1
    for i in range(i):
        out=out*(k-i)//(i+1)
    return out%mod

class Solution:
    def numWays(self, s: str) -> int:
        cn=s.count('1')
        if cn%3!=0:
            return 0
        if cn==0:
            return c(2,len(s)-1)
        cn=cn//3
        i=0
        j=len(s)-1
        ci=0
        cj=0
        while ci<cn:
            if s[i]=='1':
                ci+=1
            i+=1
        while cj<cn:
            if s[j]=='1':
                cj+=1
            j-=1
        ii=i
        jj=j
        # print(ii,jj,i,j)
        while s[ii]!='1':
            ii+=1
        while s[jj]!='1':
            jj-=1
        return ((ii-i+1)*(j-jj+1))%mod

sl=Solution()
s = "100100010100110"
print(sl.numWays(s))

