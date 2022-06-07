from functools import cache
from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        verySmall = -123456789
        mem = [verySmall] * n

        def maxVal(i):
            if i >= n:
                return 0

            if mem[i] != verySmall:
                return mem[i]
            res = verySmall
            tmp = stoneValue[i]
            res = max(res, tmp - maxVal(i + 1))

            if i < n - 1:
                tmp += stoneValue[i + 1]
                res = max(res, tmp - maxVal(i + 2))

            if i < n - 2:
                tmp += stoneValue[i + 2]
                res = max(res, tmp - maxVal(i + 3))
            mem[i] = verySmall

            return res

        tmp = maxVal(0)

        if tmp > 0:
            return 'Alice'
        elif tmp == 0:
            return 'Tie'
        else:
            return 'Bob'


values = [1, 2, 3, 7]
values = [1, 2, 3, -9]
values = [1, 2, 3, 6]
values = [1, 2, 3, -1, -2, -3, 7]

values = [-1, -2, -3]
print(Solution().stoneGameIII(values))
