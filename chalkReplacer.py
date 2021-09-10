from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        k %= total

        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]

        return -1


chalk = [5, 1, 5]
k = 22
chalk = [3, 4, 1, 2]
k = 25
print(Solution().chalkReplacer(chalk, k))
