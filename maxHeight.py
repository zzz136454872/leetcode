from typing import List


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        cuboids = [sorted(c) for c in cuboids]
        cuboids.sort()
        height = [c[2] for c in cuboids]

        for i in range(len(cuboids)):
            for j in range(i - 1, -1, -1):
                if cuboids[i][0] >= cuboids[j][0] and\
                        cuboids[i][1] >= cuboids[j][1] and\
                        cuboids[i][2] >= cuboids[j][2]:
                    height[i] = max(height[i], cuboids[i][2] + height[j])

        return max(height)


sl = Solution()
cuboids = [[50, 45, 20], [95, 37, 53], [45, 23, 12]]
cuboids = [[38, 25, 45], [76, 35, 3]]
cuboids = [[7, 11, 17], [7, 17, 11], [11, 7, 17], [11, 17, 7], [17, 7, 11],
           [17, 11, 7]]
print(sl.maxHeight(cuboids))
