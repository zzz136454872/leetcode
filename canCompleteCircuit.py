from typing import *

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start=0
        while start<len(gas):
            i=start
            rest=0
            while rest>=0:
                rest=rest+gas[i]-cost[i]
                i=(i+1)%len(gas)
                if i==start and rest>=0:
                    return start
            if i>start:
                start=i
            else:
                return -1

gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

gas  = [2,3,4]
cost = [3,4,3]

sl=Solution()
print(sl.canCompleteCircuit(gas, cost))

