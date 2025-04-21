from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int,
                       upper: int) -> int:
        m1 = 0
        m2 = 0
        s = 0

        for d in differences:
            s += d
            m1 = max(m1, s)
            m2 = min(m2, s)

        return max(0, upper - lower - m1 + m2 + 1)


differences = [1, -3, 4]
lower = 1
upper = 6

print(Solution().numberOfArrays(differences, lower, upper))
