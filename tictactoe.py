from typing import *

class Solution:
    def tictactoe(self, board: List[str]) -> str:
        n=len(board)
        def check(letter,startx,starty,dx,dy):
            x=startx
            y=starty
            for i in range(n):
                if board[x][y]!=letter:
                    return False
                x+=dx
                y+=dy
            return True
        def checkall(letter):
            for x in range(n):
                if check(letter,x,0,0,1):
                    return True
            for y in range(n):
                if check(letter,0,y,1,0):
                    return True
            if check(letter,0,0,1,1):
                return True
            if check(letter,0,n-1,1,-1):
                return True
            return False
        if checkall('X'):
            return 'X'
        if checkall('O'):
            return 'O'
        for i in range(n):
            if ' ' in board[i]:
                return 'Pending'
        return 'Draw'

board = ["O X"," XO","X O"]
board = ["OOX","XXO","OXO"]
board = ["OOX","XXO","OX "]
sl=Solution()
print(sl.tictactoe(board))

