from typing import *


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        s0=s.split('1')
        s1=s.split('0')
        l0=max([len(x) for x in s0])
        l1=max([len(x) for x in s1])
        if l1>l0:
            return True
        return False

sl=Solution()
s = "111000"
s = "110100010"
print(sl.checkZeroOnes(s))
