from typing import *

# 寻找旋转排序数组中的最小值
# 寻找旋转排序数组中的最小值II
class Solution:
    def findMin(self, nums: List[int]) -> int:
        out=123456781234
        for num in nums[::-1]:
            if out>=num:
                out=num
            else:
                return out
        return out

sl=Solution()
nums = [2,2,2,0,1]
print(sl.findMin(nums))

