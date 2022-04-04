from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 1
        n = len(candies)
        right = sum(candies) // k

        while left <= right:
            mid = (left + right) // 2
            count = sum([candies[i] // mid for i in range(n)])

            if count >= k:
                left = mid + 1
            else:
                right = mid - 1

        return left - 1


candies = [5, 8, 6]
k = 3
candies = [2, 5]
k = 11
print(Solution().maximumCandies(candies, k))
