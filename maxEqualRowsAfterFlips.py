from collections import defaultdict
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        mem = defaultdict(int)

        for line in matrix:
            if line[0] == 1:
                line = [(lambda x: 1 if x == 0 else 0)(x) for x in line]
            mem[tuple(line)] += 1

        return max(mem.values())


matrix = [[0, 1], [1, 1]]
matrix = [[0, 1], [1, 0]]
print(Solution().maxEqualRowsAfterFlips(matrix))
