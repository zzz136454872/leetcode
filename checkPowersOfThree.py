from typing import List


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        c = 1

        while c < n:
            c *= 3

        while c > 0:
            if n >= c:
                n -= c
            c //= 3

        return n == 0


n = 12
n = 91
n = 21
print(Solution().checkPowersOfThree(n))
