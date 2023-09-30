from typing import List


class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        for op in operations:
            t = gem[op[0]] // 2
            gem[op[0]] -= t
            gem[op[1]] += t

        return max(gem) - min(gem)


gem = [3, 1, 2]
operations = [[0, 2], [2, 1], [2, 0]]
gem = [100, 0, 50, 100]
operations = [[0, 2], [0, 1], [3, 0], [3, 0]]
gem = [0, 0, 0, 0]
operations = [[1, 2], [3, 1], [1, 2]]
print(Solution().giveGem(gem, operations))
