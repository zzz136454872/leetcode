from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        out = 0
        j = 0

        for h in houses:
            while j < len(heaters) and heaters[j] < h:
                j += 1
            this = 10**9

            if j > 0:
                this = min(this, h - heaters[j - 1])

            if j < len(heaters):
                this = min(this, heaters[j] - h)
            out = max(this, out)

        return out


houses = [1, 2, 3]
heaters = [2]
houses = [1, 2, 3, 4]
heaters = [1, 4]
houses = [1, 5]
heaters = [2]
print(Solution().findRadius(houses, heaters))
