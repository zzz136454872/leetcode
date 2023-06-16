from typing import List


class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n = len(flips)
        mem = [False] * n
        res = 0
        c = 0

        for i in range(n):
            mem[flips[i] - 1] = True

            while c < len(flips) and mem[c]:
                c += 1

            if c == i + 1:
                res += 1

        return res


flips = [3, 2, 4, 1, 5]
flips = [4, 1, 2, 3]
print(Solution().numTimesAllBlue(flips))
