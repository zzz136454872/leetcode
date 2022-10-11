from typing import List


class Solution:
    def sandyLandManagement(self, size: int) -> List[List[int]]:
        res = []

        for i in range(size):
            j = 1

            while j <= 2 * i + 1:
                res.append([i + 1, j])
                j += 4

            if j != 2 * i + 5:
                res.append([i + 1, 2 * i + 1])

        return res


size = 3
print(Solution().sandyLandManagement(size))
