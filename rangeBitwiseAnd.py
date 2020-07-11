from typing import *

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m==0:
            return 0
        m=bin(m)[2:]
        n=bin(n)[2:]
        if len(m)!=len(n):
            return 0
        i=0
        out=''
        while i<len(m) and m[i]==n[i]:
            out+=m[i]
            i+=1
        out+='0'*(len(m)-i)
        return int(out,2)


def test(m,n):
    out=n
    for i in range(m,n):
        out=out&i
    return out
print('test',test(0,2))
    
sl=Solution()
m=3
n=3
print(sl.rangeBitwiseAnd(m,n))

