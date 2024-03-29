from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for op in ops:
            m = min(m, op[0])
            n = min(n, op[1])

        return m * n


m = 3
n = 3
operations = [[2, 2], [3, 3]]
print(Solution().maxCount(m, n, operations))
