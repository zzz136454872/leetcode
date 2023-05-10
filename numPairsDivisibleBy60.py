from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        a = [0] * 60

        for t in time:
            a[t % 60] += 1

        res = 0

        for i in range(1, 30):
            res += a[i] * a[60 - i]
        res += a[0] * (a[0] - 1) // 2
        res += a[30] * (a[30] - 1) // 2

        return res


time = [30, 20, 150, 100, 40]
time = [60, 60, 60]
print(Solution().numPairsDivisibleBy60(time))
