from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        mem = []
        left = -1
        right = -1

        for i in range(len(seats)):
            if seats[i] == 1:
                left = i

                break

        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 1:
                right = i

                break

        j = left + 1

        for i in range(left + 1, right + 1):
            if seats[i] == 1:
                mem.append(i - j)
                j = i + 1

        if len(mem) > 0:
            return max(left, len(seats) - right - 1, (max(mem) + 1) // 2)

        return max(left, len(seats) - right - 1)


seats = [1, 0, 0, 0, 1, 0, 1]
seats = [1, 0, 0, 0]
seats = [0, 1]
print(Solution().maxDistToClosest(seats))
