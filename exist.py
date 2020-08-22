from typing import *

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])

        def test(x,y,loc,log):
            if loc==len(word):
                return True
            if x<0 or y<0 or x>=n or y>=m:
                return False
            if not log[x][y] or board[x][y]!=word[loc]:
                return False
            log[x][y]=False
            if test(x-1,y,loc+1,log) or test(x+1,y,loc+1,log) or test(x,y-1,loc+1,log) or test(x,y+1,loc+1,log):
                return True
            log[x][y]=True
            return False

        log=[[True for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0] and test(i,j,0,log):
                    return True
        return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
board = [["a","b"],["c","d"]]
word = "abcd"
sl=Solution()
from time import time
start=time()
print(sl.exist(board,word))
end=time()
print(end-start)


