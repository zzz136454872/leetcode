from functools import cache
from typing import List


# tle
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        @cache
        def ms(pizza):
            if len(pizza) == 3:
                return max(pizza)
            res = max(
                ms(pizza[1:len(pizza) - 2]) + pizza[-1],
                ms(pizza[2:len(pizza) - 1]) + pizza[0])

            for i in range(1, len(pizza) - 1):
                res = max(res, ms(pizza[:i - 1] + pizza[i + 2:]) + pizza[i])

            return res

        return ms(tuple(slices))


slices = [1, 2, 3, 4, 5, 6]
slices = [8, 9, 8, 6, 1, 1]

print(Solution().maxSizeSlices(slices))
