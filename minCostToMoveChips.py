from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        c0 = 0
        c1 = 0

        for p in position:
            if p % 2 == 0:
                c0 += 1
            else:
                c1 += 1

        return min(c0, c1)


position = [2, 2, 2, 3, 3]
position = [1, 1000000000]
print(Solution().minCostToMoveChips(position))
