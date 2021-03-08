from typing import *

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if len(s)<=1:
            return True
        flag=True
        for l in s:
            if l=='0':
                flag=False
            if not flag and l=='1':
                return False
        return True

sl=Solution()
s='100'
print(sl.checkOnesSegment(s))

