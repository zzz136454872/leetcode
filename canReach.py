from typing import *


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        cr = [False] * len(s)
        cr[0] = True

        if s[-1] != '0':
            return False

        for i in range(len(s)):
            if not cr[i]:
                continue
            for j in range(minJump, maxJump + 1):
                if i + j < len(s):
                    if s[i + j] == '0' and not cr[i + j]:
                        cr[i + j] = True

        return cr[-1]


sl = Solution()
s = "011010"
minJump = 2
maxJump = 3
s = "01101110"
minJump = 2
maxJump = 3
print(sl.canReach(s, minJump, maxJump))
