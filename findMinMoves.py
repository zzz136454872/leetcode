from typing import *

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        if len(machines)==0:
            return -1
        total=sum(machines)
        avg=total//len(machines)
        if avg*len(machines)!=total:
            return -1
        machines=[i-avg for i in machines]
        #print(machines)
        tmp=0
        out=0
        for m in machines:
            tmp+=m
            out=max(abs(tmp),out)
        out=max(max(machines),out)
        return out

sl=Solution()
m=[0,0,11,5]
print(sl.findMinMoves(m))
