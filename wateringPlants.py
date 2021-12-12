from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        last = capacity
        out = 0

        for i in range(len(plants)):
            if last >= plants[i]:
                last -= plants[i]
                out += 1
            else:
                last = capacity - plants[i]
                out += 2 * i + 1

        return out


plants = [2, 2, 3, 3]
capacity = 5
plants = [1, 1, 1, 4, 2, 3]
capacity = 4
plants = [7, 7, 7, 7, 7, 7, 7]
capacity = 8
print(Solution().wateringPlants(plants, capacity))
