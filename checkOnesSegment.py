from typing import *


# 解法1
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        flag = True

        for l in s:
            if l == '0':
                flag = False

            if not flag and l == '1':
                return False

        return True


# 解法2
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return len(list(filter(lambda x: len(x) > 0, s.split('0')))) <= 1


sl = Solution()
s = '110'
s = '1001'

print(sl.checkOnesSegment(s))
