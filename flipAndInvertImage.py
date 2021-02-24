from typing import *

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[0 if num==1 else k for num in row[::-1]] for row in A]

sl=Solution()
inp=[[1,1,0],[1,0,1],[0,0,0]]
print(sl.flipAndInvertImage(inp))
