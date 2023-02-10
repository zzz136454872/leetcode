from functools import cache
from typing import List


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = 10**9 + 7
        rollMax.append(1)

        @cache
        def dp(pos, last, num):
            if last > pos:
                return 0

            if last > rollMax[num]:
                return 0

            if pos == 1:
                return 1

            if last > 1:
                return dp(pos - 1, last - 1, num)
            r = 0

            for i in range(6):
                if i == num:
                    continue

                for j in range(1, rollMax[i] + 1):
                    r = (r + dp(pos - 1, j, i)) % mod

            # print(pos,last,num,r)

            return r

        return dp(n + 1, 1, 6)


n = 2
rollMax = [1, 1, 2, 2, 2, 3]
n = 2
rollMax = [1, 1, 1, 1, 1, 1]
n = 3
rollMax = [1, 1, 1, 2, 2, 3]
print(Solution().dieSimulator(n, rollMax))
