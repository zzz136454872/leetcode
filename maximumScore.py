from typing import *

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        log=[a,b,c]
        log.sort()
        if log[2]>=log[0]+log[1]:
            return log[0]+log[1]
        return sum(log)//2

sl=Solution()
a = 4
b = 4
c = 6
print(sl.maximumScore(a,b,c))
