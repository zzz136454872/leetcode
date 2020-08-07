from typing import *

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        premax=-123456
        count=0
        for interval in intervals:
            if interval[1]>premax:
                premax=interval[1]
                count+=1
        return count

intervals = [[3,10],[4,10],[5,11]]
sl=Solution()
print(sl.removeCoveredIntervals(intervals))
                
                
            
