from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def checkCol(col):
            if board[0][col] == board[1][col] and board[1][col] == board[2][
                    col]:
                return board[0][col]

            return ' '

        def checkRow(row):
            if board[row][0] == board[row][1] and board[row][1] == board[row][
                    2]:
                return board[row][0]

            return ' '

        def checkx(idx):
            if idx == 0:
                if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
                    return board[0][0]

                return ' '
            else:
                if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
                    return board[0][2]

                return ' '

        countO = 0
        countX = 0

        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    countX += 1
                elif board[i][j] == 'O':
                    countO += 1

        if countX < countO or countX > countO + 1:
            return False
        succeed = []
        target = set(['O', 'X'])

        for i in range(3):
            tmp = checkCol(i)

            if tmp in target:
                succeed.append(tmp)
            tmp = checkRow(i)

            if tmp in target:
                succeed.append(tmp)
        tmp = checkx(0)

        if tmp in target:
            succeed.append(tmp)
        tmp = checkx(1)

        if tmp in target:
            succeed.append(tmp)

        if 'O' in succeed and 'X' in succeed:
            return False

        if 'X' in succeed and countO == countX:
            return False

        if 'O' in succeed and countO < countX:
            return False

        return True


board = ["O  ", "   ", "   "]
board = ["XOX", " X ", "   "]
board = ["XXX", "   ", "OOO"]
print(Solution().validTicTacToe(board))
