from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = 10**9

        while left <= right:
            mid = (left + right) // 2
            print(left, right, mid)
            time = sum(ceil(i / mid) for i in piles)

            if time > h:
                left = mid + 1
            else:
                right = mid - 1

        return left


piles = [2, 2]
h = 2
print(Solution().minEatingSpeed(piles, h))
