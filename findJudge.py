from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        from_t = [0 for i in range(n)]
        to_t = [0 for i in range(n)]

        for t in trust:
            from_t[t[0] - 1] += 1
            to_t[t[1] - 1] += 1

        for i in range(n):
            if from_t[i] == 0 and to_t[i] == n - 1:
                return i + 1

        return -1


n = 2
trust = [[1, 2]]

n = 3
trust = [[1, 3], [2, 3]]
n = 3
trust = [[1, 3], [2, 3], [3, 1]]
n = 3
n = 4
trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
print(Solution().findJudge(n, trust))
