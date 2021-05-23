from typing import *

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        table=[0]
        for num in nums:
            table=table+[t^num for t in table]
        return sum(table)

sl=Solution()
nums = [5,1,6]
print(sl.subsetXORSum(nums))
