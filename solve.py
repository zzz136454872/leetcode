from typing import *

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.board=board
        self.x=len(board)
        if self.x==0:
            return 
        self.y=len(board[0])
        if self.y==0:
            return
        for i in range(self.x):
            if board[i][0]=='O':
                self.fill(i,0)
            if board[i][-1]=='O':
                self.fill(i,self.y-1)
        for j in range(self.y):
            if board[0][j]=='O':
                self.fill(0,j)
            if board[-1][j]=='O':
                self.fill(self.x-1,j)
        def convert(a):
            if a=='X' or a=='O':
                return 'X'
            return 'O'
        for i in range(self.x):
            for j in range(self.y):
                board[i][j]=convert(board[i][j])
                
    def fill(self,i,j):
        if i<0 or j<0 or i>=self.x or j>=self.y:
            return 
        if self.board[i][j]!='O':
            return 
        self.board[i][j]='1'
        self.fill(i-1,j)
        self.fill(i+1,j)
        self.fill(i,j-1)
        self.fill(i,j+1)
sl=Solution()
board=[['X','X','X','X'], ['X','O','O','X'], ['X','X','O','X'], ['X','O','X','X']] 
sl.solve(board)
print(board)

