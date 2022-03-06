from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        front = [0] * n
        end = [0] * n
        out = []

        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                end[i] = end[i + 1] + 1
            else:
                end[i] = 0

        for i in range(1, n):
            if security[i] <= security[i - 1]:
                front[i] = front[i - 1] + 1
            else:
                front[i] = 0

        for i in range(n):
            if front[i] >= time and end[i] >= time:
                out.append(i)

        return out


security = [5, 3, 3, 3, 5, 6, 2]
time = 2
security = [1, 1, 1, 1, 1]
time = 0
security = [1, 2, 3, 4, 5, 6]
time = 2
security = [1]
time = 5
print(Solution().goodDaysToRobBank(security, time))
