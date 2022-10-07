from copy import deepcopy
from typing import List


class Solution:
    def flipChess(self, chessboard: List[str]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1),
                (-1, -1)]

        def bfs(a, b):
            res = 0
            mem = []

            for d in dirs:
                x = a + d[0]
                y = b + d[1]
                has = False

                if a == 2 and b == 4 and d == (0, -1):
                    print('flag')

                while x >= 0 and x < len(c) and y >= 0 and y < len(c[0]):

                    if c[x][y] == 'X':
                        has = True

                        break
                    elif c[x][y] == '.':
                        break
                    x += d[0]
                    y += d[1]

                if has:
                    x = a + d[0]
                    y = b + d[1]

                    while x >= 0 and x < len(c) and y >= 0 and y < len(
                            c[0]) and c[x][y] == 'O':
                        c[x][y] = 'X'
                        res += 1
                        mem.append((x, y))
                        x += d[0]
                        y += d[1]

            for point in mem:
                res += bfs(point[0], point[1])

            return res

        res = 0

        for i in range(len(chessboard)):
            for j in range(len(chessboard[0])):
                if chessboard[i][j] == '.':
                    c = [list(s) for s in chessboard]
                    res = max(res, bfs(i, j))

        return res


chessboard = ["....X.", "....X.", "XOOO..", "......", "......"]
chessboard = [".X.", ".O.", "XO."]
chessboard = [
    ".......", ".......", ".......", "X......", ".O.....", "..O....", "....OOX"
]

print(Solution().flipChess(chessboard))
