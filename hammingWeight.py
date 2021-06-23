from typing import *


class Solution:
    def hammingWeight(self, n: int) -> int:
        out = 0

        while n != 0:
            n = n & (n - 1)
            # print(n)
            out += 1

        return out


sl = Solution()
inp = int('1111', 2)
print(sl.hammingWeight(inp))
