from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        tmp = [10**8 + 1, 10**8 + 1]

        def inside(inter, val):
            if inter[0] <= val and inter[1] >= val:
                return True

            return False

        for i in range(len(intervals) - 1, -1, -1):
            k = intervals[i][0]

            while not inside(intervals[i], tmp[1]):
                tmp.pop()

                if k == tmp[0]:
                    k += 1
                tmp.append(k)
                tmp.sort()
                res += 1
                k += 1
            print(tmp, res)

        return res


intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
print(Solution().intersectionSizeTwo(intervals))
