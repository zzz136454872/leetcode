from typing import *


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        tmp = 0
        total = 0

        for price in satisfaction:
            tmp += price

            if tmp >= 0:
                total += tmp
            else:
                break

        return total


satisfaction = [4, 3, 2]
sl = Solution()
print(sl.maxSatisfaction(satisfaction))
