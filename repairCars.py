from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        right = 10**14
        left = 0
        eps = 10**(-9)

        while left <= right:
            mid = (left + right) // 2
            t = 0

            for r in ranks:
                t += int((mid / r)**0.5 + eps)

            if t >= cars:
                right = mid - 1
            else:
                left = mid + 1

        return left


ranks = [4, 2, 3, 1]
cars = 10
ranks = [5, 1, 8]
cars = 6
ranks = [100]
cars = 1000000
print(Solution().repairCars(ranks, cars))
