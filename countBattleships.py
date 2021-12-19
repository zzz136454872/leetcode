from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def check(i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return

            if board[i][j] != 'X':
                return
            board[i][j] = 'a'
            check(i, j + 1)
            check(i, j - 1)
            check(i + 1, j)
            check(i - 1, j)

        out = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    out += 1
                    check(i, j)

        return out


board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
board = [["."]]
print(Solution().countBattleships(board))
