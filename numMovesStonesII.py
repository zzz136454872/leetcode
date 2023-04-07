from typing import List


class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        v = stones[-1] - stones[0]
        v1 = min(stones[1] - stones[0], stones[-1] - stones[-2])
        v1 = v - len(stones) + 2 - v1

        res = 0
        j = 0
        n = len(stones)

        for i in range(n):
            while j < n and stones[j] <= stones[i] + n - 1:
                j += 1

            if j - i == n - 1 and stones[j - 1] == stones[i] + n - 2:
                res = max(res, n - 2)
            else:
                res = max(res, j - i)

        return [n - res, v1]


stones = [7, 4, 9]
stones = [6, 5, 4, 3, 10]
stones = [100, 101, 104, 102, 103]
stones = [1]
print(Solution().numMovesStonesII(stones))
