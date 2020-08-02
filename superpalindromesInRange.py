from typing import *

from math import sqrt

def check(s):
    s=str(s)
    return s==s[::-1]

class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:
        count=0
        start=10**(len(L)//4)
        L=int(L)
        R=int(R)
        out=0
        while True:
            str_num=str(start)
            start+=1
            test1=int(str_num+str_num[::-1])**2
            test2=int(str_num[:-1]+str_num[::-1])**2
            if test1>=L and test1<R and check(test1):
                out+=1
            if test2>=L and check(test2):
                if test2<=R:
                    out+=1
                else:
                    break
        return out

sl=Solution()
L = "4"
R = "1000"
print(sl.superpalindromesInRange(L,R))


                
        








