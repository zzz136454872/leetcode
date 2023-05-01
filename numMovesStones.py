from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        ma = c - a - 2

        if c - a == 2:
            mi = 0
        elif b - a == 1 or c - b == 1 or b - a == 2 or c - b == 2:
            mi = 1
        else:
            mi = 2

        return [mi, ma]


a = 1
b = 2
c = 5
a = 4
b = 3
c = 2
a = 3
b = 5
c = 1
print(Solution().numMovesStones(a, b, c))
