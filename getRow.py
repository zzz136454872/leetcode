from typing import *

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tmp=1
        out=[]
        for i in range(rowIndex):
            out.append(tmp)
            tmp=tmp*(rowIndex-i)//(i+1)
        out.append(tmp)
        return out

sl=Solution()
row=10
print(sl.getRow(row))
