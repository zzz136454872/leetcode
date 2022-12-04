from functools import lru_cache
from itertools import combinations
from typing import List


class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]],
                             k: int) -> int:
        pre = [0] * n

        for i, j in relations:
            pre[j - 1] |= 2**(i - 1)

        @lru_cache
        def dfs(state):
            if state == 2**n - 1:
                return 0
            nxt = [
                i for i in range(n)
                if state & (2**i) == 0 and pre[i] == state & pre[i]
            ]
            res = n + 1
            floor = (len(nxt) + k - 1) // k

            for tmp in combinations(nxt, min(k, len(nxt))):
                res = min(res, 1 + dfs(state | sum(2**i for i in tmp)))

                if res == floor:
                    break

            return res

        return dfs(0)


n = 4
relations = [[2, 1], [3, 1], [1, 4]]
k = 2
n = 5
relations = [[2, 1], [3, 1], [4, 1], [1, 5]]
k = 2

n = 14
relations = [[11, 7]]
k = 2
print(Solution().minNumberOfSemesters(n, relations, k))
