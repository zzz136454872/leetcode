from typing import List


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        heights = []

        for i in range(len(positions)):
            bottom = 0

            for j in range(i):
                if not (positions[i][0] >= positions[j][0] + positions[j][1] or
                        positions[j][0] >= positions[i][0] + positions[i][1]):
                    bottom = max(bottom, heights[j])
            heights.append(bottom + positions[i][1])

        for i in range(1, len(positions)):
            heights[i] = max(heights[i], heights[i - 1])

        return heights


positions = [[1, 2], [2, 3], [6, 1]]
positions = [[100, 100], [200, 100]]
positions = [[1, 5], [2, 2]]
positions = [[3, 2], [9, 8]]
positions = [[1, 10], [1, 10]]
print(Solution().fallingSquares(positions))
