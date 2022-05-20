from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        i3 = [intervals[i] + [i, -1] for i in range(n)]
        i3.sort(key=lambda x: x[0])

        for i in range(n):
            left = i
            right = n - 1

            while left <= right:
                mid = (left + right) // 2

                if i3[mid][0] >= i3[i][1]:
                    right = mid - 1
                else:
                    left = mid + 1

            if left != n:
                i3[i][3] = i3[left][2]
        i3.sort(key=lambda x: x[2])

        return [x[3] for x in i3]


intervals = [[1, 2]]
intervals = [[3, 4], [2, 3], [1, 2]]
intervals = [[1, 4], [2, 3], [3, 4]]
print(Solution().findRightInterval(intervals))
