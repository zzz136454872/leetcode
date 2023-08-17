from functools import cache
from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m = len(pizza)
        n = len(pizza[0])
        apple = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                apple[i][j] = apple[i + 1][j] +\
                        apple[i][j + 1] - apple[i + 1][j + 1]

                if pizza[i][j] == 'A':
                    apple[i][j] += 1

        # print(apple)
        mod = 10**9 + 7

        @cache
        def dfs(a, b, c):
            if apple[a][b] < c:
                return 0

            if c == 1:
                return 1
            res = 0

            for i in range(a + 1, m):
                if apple[i][b] < apple[a][b]:
                    res += dfs(i, b, c - 1)

            for j in range(b + 1, n):
                if apple[a][j] < apple[a][b]:
                    res += dfs(a, j, c - 1)

            return res % mod

        return dfs(0, 0, k)


pizza = ["A..", "AAA", "..."]
k = 3
pizza = ["A..", "AA.", "..."]
k = 3
pizza = ["A..", "A..", "..."]
k = 1
print(Solution().ways(pizza, k))
