from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        res = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            f = questions[i][1] + i + 1
            t = questions[i][0]

            if f < len(questions):
                t += res[f]
            res[i] = max(res[i + 1], t)

        return res[0]


questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
questions = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
print(Solution().mostPoints(questions))
