from typing import List


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int,
                    by1: int, bx2: int, by2: int) -> int:
        def coverLine(a1, a2, b1, b2):
            l1 = max(a1, b1)
            l2 = min(a2, b2)

            return max(l2 - l1, 0)

        def s(x1, x2, y1, y2):
            return (x2 - x1) * (y2 - y1)

        return s(ax1, ax2, ay1, ay2) + s(bx1, bx2, by1, by2) - coverLine(
            ax1, ax2, bx1, bx2) * coverLine(ay1, ay2, by1, by2)


ax1 = -3
ay1 = 0
ax2 = 3
ay2 = 4
bx1 = 0
by1 = -1
bx2 = 9
by2 = 2
ax1 = -2
ay1 = -2
ax2 = 2
ay2 = 2
bx1 = -2
by1 = -2
bx2 = 2
by2 = 2
print(Solution().computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))
