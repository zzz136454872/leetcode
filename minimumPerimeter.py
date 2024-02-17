from typing import List


class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        left = 0
        right = 12345

        while left <= right:
            mid = (left + right) // 2
            t = 2 * mid * (mid + 1) * (2 * mid + 1)

            if t >= neededApples:
                right = mid - 1
            else:
                left = mid + 1

        return 8 * left


neededApples = 1
neededApples = 13
neededApples = 1000000000
print(Solution().minimumPerimeter(neededApples))
