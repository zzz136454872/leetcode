from typing import List

# WA
class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int,
                        stampWidth: int) -> bool:

        for i in range(len(grid)):
            acc = 0

            for j in range(len(grid[0])):
                if grid[i][j] & 1 == 1:
                    acc = 0

                    continue
                acc += 1

                if acc == stampWidth:
                    for k in range(stampWidth):
                        grid[i][j - k] |= 2
                elif acc > stampWidth:
                    grid[i][j] |= 2

        for j in range(len(grid[0])):
            acc = 0

            for i in range(len(grid)):
                if grid[i][j] & 1 == 1:
                    acc = 0

                    continue
                acc += 1

                if acc == stampHeight:
                    for k in range(stampHeight):
                        grid[i - k][j] |= 4
                elif acc > stampHeight:
                    grid[i][j] |= 4

        for i in range(len(grid)):
            print(grid[i])

        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j] != 1 and grid[i][j] & 6 != 6:
                    return False

        return True


grid = [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
stampHeight = 4
stampWidth = 3
grid = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
stampHeight = 2
stampWidth = 2
grid = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
stampHeight = 2
stampWidth = 8
grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1]]
stampHeight = 2
stampWidth = 2
print(Solution().possibleToStamp(grid, stampHeight, stampWidth))
