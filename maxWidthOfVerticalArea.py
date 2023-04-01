from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        a = sorted([x[0] for x in points])

        return max([a[i + 1] - a[i] for i in range(len(a) - 1)])
