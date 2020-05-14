from typing import *

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        out=0
        for num in nums:
            out=out^num
        return out

