from typing import List


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        sons = [[-1, -1] for _ in range(n)]
        count = [[0, 0, 0] for _ in range(n)]

        for s, p in enumerate(parents):
            if p == -1:
                continue

            if sons[p][0] == -1:
                sons[p][0] = s
            else:
                sons[p][1] = s
        out = 0

        # print(sons)

        def dfs(idx):
            if idx == -1:
                return 0
            count[idx][0] = dfs(sons[idx][0])
            count[idx][1] = dfs(sons[idx][1])
            total = count[idx][0] + count[idx][1] + 1
            count[idx][2] = n - total

            return total

        dfs(0)
        maxV = 0
        maxCount = 0

        for i in range(n):
            now = 1
            flag = False

            if count[i][0] > 0:
                now *= count[i][0]
                flag = True

            if count[i][1] > 0:
                now *= count[i][1]
                flag = True

            if count[i][2] > 0:
                now *= count[i][2]
                flag = True

            if not flag:
                now = 0

            if now < maxV:
                continue

            if now == maxV:
                maxCount += 1
            else:
                maxCount = 1
                maxV = now

        return maxCount


parents = [-1, 2, 0, 2, 0]
parents = [-1, 2, 0]
print(Solution().countHighestScoreNodes(parents))
