from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int],
                             duration: int) -> int:
        if len(timeSeries) == 0:
            return 0
        else:
            out = duration

        for i in range(len(timeSeries) - 1):
            out += min(timeSeries[i + 1] - timeSeries[i], duration)

        return out


timeSeries = [1, 2]
duration = 2
print(Solution().findPoisonedDuration(timeSeries, duration))
