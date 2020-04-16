from typing import *


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        i=0
        while i<len(intervals)-1:
            if intervals[i][1]>=intervals[i+1][0]:
                tmp=[intervals[i][0],max(intervals[i+1][1],intervals[i][1])]
                del intervals[i]
                del intervals[i]
                intervals.insert(i,tmp)
            else:
                i+=1
        return intervals
                
inp=[[1,3],[2,6],[8,10],[15,18]]
sl=Solution()
print(sl.merge(inp))
            
            
        

