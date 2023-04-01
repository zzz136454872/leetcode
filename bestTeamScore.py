from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        ps = [(ages[i], scores[i]) for i in range(len(scores))]
        ps.sort()
        ss = [p[1] for p in ps]

        for i in range(len(scores)):
            t = 0

            for j in range(i - 1, -1, -1):
                if ps[j][1] > ps[i][1]:
                    continue
                t = max(ss[j], t)
            ss[i] += t

        return max(ss)


scores = [1, 3, 5, 10, 15]
ages = [1, 2, 3, 4, 5]
scores = [4, 5, 6, 5]
ages = [2, 1, 2, 1]
scores = [1, 2, 3, 5]
ages = [8, 9, 10, 1]
print(Solution().bestTeamScore(scores, ages))
