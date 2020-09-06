from typing import *

class Solution:
    def countDigitOne(self, n: int) -> int:
        base=1
        out=0
        while n>0:
            if n%10>0:
                out+=base
            n=n//10
            out+=n*base
            base=base*10
        return out

sl=Solution()
n=13
print(sl.countDigitOne(n))

            
                
