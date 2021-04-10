from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums

sl=Solution()
nums = [1,0,1,1,1]
target = 0
print(sl.search(nums,target))

