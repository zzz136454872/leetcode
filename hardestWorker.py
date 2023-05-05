from collections import defaultdict
from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        prev = 0
        t = 0
        idx = 12345678

        for log in logs:
            tmp = log[1] - prev

            if tmp > t or tmp == t and idx > log[0]:
                idx = log[0]
                t = tmp
            prev = log[1]

        return idx


n = 10
logs = [[0, 3], [2, 5], [0, 9], [1, 15]]
n = 26
logs = [[1, 1], [3, 7], [2, 12], [7, 17]]
print(Solution().hardestWorker(n, logs))
