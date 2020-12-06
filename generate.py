from typing import *

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        out=[[1 for j in range(i+1)] for i in range(numRows)]
        if numRows==1:
            return out
        for i in range(numRows):
            for j in range(1,i):
                out[i][j]=out[i-1][j-1]+out[i-1][j]
        return out

sl=Solution()
inp=5
print(sl.generate(5))

