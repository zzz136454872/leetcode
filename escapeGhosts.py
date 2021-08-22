from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        min_dis = 123456

        for g in ghosts:
            min_dis = min(min_dis,
                          abs(target[0] - g[0]) + abs(target[1] - g[1]))

        return abs(target[0]) + abs(target[1]) < min_dis


ghosts = [[1, 0], [0, 3]]
target = [0, 1]
ghosts = [[1, 0]]
target = [2, 0]
sl = Solution()
print(sl.escapeGhosts(ghosts, target))
