from typing import *

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)==0:
            return 0
        intervals.sort(key=lambda x:(x[0],-x[1]))
        log=[]
        for i in range(len(intervals)):
            now=1
            for j in range(i-1,-1,-1):
                if intervals[j][1]<=intervals[i][0]:
                    now=max(now, log[j]+1)
                    break
            log.append(now)
        return len(intervals)-max(log)

sl=Solution()
inp=[ [1,2], [2,3], [3,4], [1,3] ]
print(sl.eraseOverlapIntervals(inp))
