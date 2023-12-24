from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-p for p in piles]
        heapify(piles)

        for i in range(k):
            t = heappop(piles) // 2
            heappush(piles, t)

        return -sum(piles)


piles = [5, 4, 9]
k = 2
piles = [4, 3, 6, 7]
k = 3
print(Solution().minStoneSum(piles, k))
