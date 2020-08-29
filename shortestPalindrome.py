from typing import *

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r=s[::-1]
        test=s+'#'+r
        n=[0 for i in range(len(test))]
        i=0
        j=-1
        n[0]=-1
        while i<len(test)-1:
            if j==-1 or test[i]==test[j]:
                i+=1
                j+=1
                n[i]=j
            else:
                j=n[j]
        l=n[-1]+1
        return r[:-l]+s

inp="abcd"
sl=Solution()
print(sl.shortestPalindrome(inp))


