from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        miss = (len(rolls) + n) * mean - sum(rolls)

        if miss < n or miss > 6 * n:
            return []

        avg = miss // n
        change = miss - avg * n

        return [avg + 1] * change + [avg] * (n - change)


rolls = [3, 2, 4, 3]
mean = 4
n = 2
rolls = [1, 5, 6]
mean = 3
n = 4
rolls = [1, 2, 3, 4]
mean = 6
n = 4
print(Solution().missingRolls(rolls, mean, n))
