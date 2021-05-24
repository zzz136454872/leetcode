from typing import *

import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist)-1>=hour:
            return -1
        left=1
        right=10**7+1
        def getTime(speed):
            time=0
            for d in dist[:-1]:
                time+=math.ceil(d/speed)
            time+=dist[-1]/speed
            return time
        while left<=right:
            mid=(left+right)//2
            t=getTime(mid)
            if t<=hour:
                right=mid-1
            else:
                left=mid+1
        return left

dist = [1,3,2]
hour = 1.9
sl=Solution()
print(sl.minSpeedOnTime(dist,hour))
