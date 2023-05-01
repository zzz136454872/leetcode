from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int],
                     informTime: List[int]) -> int:
        max_time = 0
        log = [-1 for i in range(n)]

        def get_time(man):
            if log[man] >= 0:
                return log[man]

            if manager[man] == -1:
                return 0
            high = manager[man]
            time = informTime[high] + get_time(high)
            log[man] = time

            return time

        for man in range(n):
            max_time = max(max_time, get_time(man))

        return max_time


sl = Solution()
n = 7
headID = 6
manager = [1, 2, 3, 4, 5, 6, -1]
informTime = [0, 6, 5, 4, 3, 2, 1]
print(sl.numOfMinutes(n, headID, manager, informTime))
