from collections import defaultdict
from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]],
                                  k: int) -> List[int]:
        mem = defaultdict(set)

        for log in logs:
            mem[log[0]].add(log[1])
        res = [0] * k

        for u in mem:
            res[len(mem[u]) - 1] += 1

        return res


logs = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
k = 5
logs = [[1, 1], [2, 2], [2, 3]]
k = 4
print(Solution().findingUsersActiveMinutes(logs, k))
