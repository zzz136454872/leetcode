
from typing import *

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens.sort()
        self.queens=queens
        self.king=king
        out=[]
        self.log=[[False for j in range(8)] for i in range(8)]
        for queen in queens:
            self.log[queen[0]][queen[1]]=True
        for queen in queens:
            if queen==[4,0]:
                print('now')
            if self.check(queen):
               out.append(queen)
        return out
    
    def check(self,queen):
        if self.king[0]==queen[0]: # same row
            if self.king[1]>queen[1]:
                for i in range(queen[1]+1,self.king[1]):
                    if self.log[queen[0]][i]:
                        return False
                return True
            else:
                for i in range(self.king[1]+1,queen[1]):
                    if self.log[queen[0]][i]:
                        return False
                return True
        elif self.king[1]==queen[1]: #same column
            if self.king[0]>queen[0]:
                for i in range(queen[0]+1,self.king[0]):
                    if self.log[i][queen[1]]:
                        return False
                return True
            else:
                for i in range(self.king[0]+1,queen[0]):
                    if self.log[i][queen[1]]:
                        return False
                return True
        elif sum(self.king)==sum(queen):
            s=sum(queen)
            if self.king[0]>queen[0]:
                for i in range(queen[0]+1,self.king[0]):
                    if self.log[i][s-i]:
                        return False
                return True
            else:
                for i in range(self.king[0]+1,queen[0]):
                    if self.log[i][s-i]:
                        return False
                return True
        elif self.king[0]-self.king[1]==queen[0]-queen[1]:
            sub=queen[1]-queen[0]
            if self.king[0]>queen[0]:
                for i in range(queen[0]+1,self.king[0]):
                    if self.log[i][i+sub]:
                        return False
                return True
            else:
                for i in range(self.king[0]+1,queen[0]):
                    if self.log[i][i+sub]:
                        return False
                return True
        return False
            
sl=Solution()
queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]
king = [0,0]
print(sl.queensAttacktheKing(queens,king))
