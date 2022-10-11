from collections import defaultdict
from typing import List


class Solution:
    def beautifulBouquet(self, flowers: List[int], cnt: int) -> int:
        mem = defaultdict(int)
        j = 0
        res = 0
        mod = 10**9 + 7
        cnt += 1

        for i in range(len(flowers)):
            mem[flowers[i]] += 1

            while mem[flowers[i]] == cnt:
                mem[flowers[j]] -= 1
                j += 1
            res = (res + i - j + 1) % mod

        return res


flowers = [1, 2, 3, 2]
cnt = 1
flowers = [5, 3, 3, 3]
cnt = 2
print(Solution().beautifulBouquet(flowers, cnt))
