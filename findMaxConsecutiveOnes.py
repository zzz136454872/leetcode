from typing import *

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        out=0
        now=0
        for num in nums:
            if num==0:
                now=0
            else:
                now+=1
                out=max(out,now)
        return out
