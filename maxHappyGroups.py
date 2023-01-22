from functools import cache
from typing import List


class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        b = batchSize

        res = 0
        state = 0

        for g in groups:
            if g % b == 0:
                res += 1
            else:
                state += 1 << ((g % b) * 5)

        @cache
        def dfs(s, m):
            r = 0

            if m == 0:
                x = 1
            else:
                x = 0

            for i in range(1, b):
                if (s >> (i * 5)) & 31:
                    t = dfs(s - (1 << (i * 5)), (m + i) % b)
                    r = max(r, t + x)

            return r

        return res + dfs(state, 0)


batchSize = 3
groups = [1, 2, 3, 4, 5, 6]
batchSize = 4
groups = [1, 3, 2, 5, 2, 2, 1, 6]
batchSize = 7
groups = [
    839562595, 994462569, 405916966, 82304069, 612871994, 590853022, 240211157,
    607701921, 87771155, 286392333, 391799587, 956454997, 317347197, 606070171,
    73694014, 993283352, 122745984, 491525998, 962888093
]
print(Solution().maxHappyGroups(batchSize, groups))
