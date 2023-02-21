from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        gap = []

        for i in range(n + 1):
            if ranges[i] == 0:
                continue
            gap.append([i - ranges[i], i + ranges[i]])
        gap.sort()
        now = 0
        idx = 0
        res = 0

        while idx < len(gap):
            if gap[idx][0] > now:
                return -1
            r = idx
            nxt = now

            while r < len(gap) and gap[r][0] <= now:
                nxt = max(nxt, gap[r][1])
                r += 1
            res += 1
            now = nxt
            idx = r

            if now >= n:
                break

        if now >= n:
            return res

        return -1


n = 5
ranges = [3, 4, 1, 1, 0, 0]
n = 3
ranges = [0, 0, 0, 0]
print(Solution().minTaps(n, ranges))
