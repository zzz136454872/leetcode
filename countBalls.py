from typing import *


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        log = [0 for i in range(100)]

        def cnt(a):
            return sum((int(i) for i in str(a)))

        for i in range(lowLimit, highLimit + 1):
            log[cnt(i)] += 1

        return max(log)


sl = Solution()
lowLimit = 5
highLimit = 15
print(sl.countBalls(lowLimit, highLimit))
