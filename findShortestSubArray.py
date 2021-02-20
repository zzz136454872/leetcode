from typing import *

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        log={}
        for i in range(len(nums)):
            if nums[i] not in log.keys():
                log[nums[i]]=[i]
            else:
                log[nums[i]].append(i)

        target=max([len(v) for v in log.values()])

        out=len(nums)
        for v in log.values():
            if len(v)==target:
                out=min(out,v[-1]-v[0]+1)
        return out

sl=Solution()
inp=[1, 2, 2, 3, 1]
print(sl.findShortestSubArray(inp))
