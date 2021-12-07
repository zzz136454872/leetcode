from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int,
                    color: int) -> List[List[int]]:
        def die(r, c):
            if grid[r][c] == -1 or grid[r][c] == color:
                return
            pre = grid[r][c]
            grid[r][c] = -1
            is_border = False

            if r == 0 or c == 0 or r == len(grid) - 1 or c == len(
                    grid[0]) - 1 or (
                        (grid[r - 1][c] != pre and grid[r - 1][c] != -1) or
                        (grid[r + 1][c] != pre and grid[r + 1][c] != -1) or
                        (grid[r][c - 1] != pre and grid[r][c - 1] != -1) or
                        (grid[r][c + 1] != pre and grid[r][c + 1] != -1)):

                is_border = True

            if r > 0 and grid[r - 1][c] == pre:
                die(r - 1, c)

            if c > 0 and grid[r][c - 1] == pre:
                die(r, c - 1)

            if r < len(grid) - 1 and grid[r + 1][c] == pre:
                die(r + 1, c)

            if c < len(grid[0]) - 1 and grid[r][c + 1] == pre:
                die(r, c + 1)

            if not is_border:
                grid[r][c] = pre

        die(row, col)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    grid[i][j] = color

        return grid


grid = [[1, 1], [1, 2]]
row = 0
col = 0
color = 3
# grid = [[1,2,2],[2,3,2]]
# row = 0
# col = 1
# color = 3

# grid = [[1,1,1],[1,1,1],[1,1,1]]
# row = 1
# col = 1
# color = 2
grid = [[1, 2, 1, 2, 1, 2], [2, 2, 2, 2, 1, 2], [1, 2, 2, 2, 1, 2]]
row = 1
col = 3
color = 1
grid = [[2, 1, 2, 2, 1, 1], [1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 1, 1],
        [2, 2, 2, 1, 2, 1], [2, 2, 2, 1, 1, 2], [1, 2, 2, 1, 1, 1]]
row = 3
col = 2
color = 1
print(Solution().colorBorder(grid, row, col, color))
