from typing import *

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        max_time=0
        log=[-1 for i in range(n)]
        for man in range(n):
            if log[man]>=0:
                continue
            time=0
            while manager[man]!=-1:
                man=manager[man]
                time+=informTime[man]
            max_time=max(time,max_time)
        return max_time
sl=Solution()
n = 7
headID = 6
manager = [1,2,3,4,5,6,-1]
informTime = [0,6,5,4,3,2,1]
n = 1
headID = 0
manager = [-1]
informTime = [0]
print(sl.numOfMinutes(n,headID,manager,informTime))




