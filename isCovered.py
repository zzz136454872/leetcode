from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int,
                  right: int) -> bool:
        ranges.sort()
        rangeNew = [ranges[0]]

        for r in ranges[1:]:
            if r[0] > rangeNew[-1][1]:
                rangeNew.append(r)
            else:
                rangeNew[-1][1] = max(rangeNew[-1][1], r[1])
        color = [False for i in range(51)]

        for r in rangeNew:
            for i in range(r[0], r[1] + 1):
                color[i] = True

        for i in range(left, right + 1):
            if not color[i]:
                return False

        return True


sl = Solution()
ranges = [[1, 2], [3, 4], [5, 6]]
left = 2
right = 5
ranges = [[1, 10], [10, 20]]
left = 21
right = 21
print(sl.isCovered(ranges, left, right))
