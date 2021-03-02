from typing import *

class NumArray:
    def __init__(self, nums: List[int]):
        self.pre_sum=[0]
        tmp=0
        for num in nums:
            tmp+=num
            self.pre_sum.append(tmp)

    def sumRange(self, i: int, j: int) -> int:
        return self.pre_sum[j+1]-self.pre_sum[i]

nums=[-2, 0, 3, -5, 2, -1]
# Your NumArray object will be instantiated and called as such:
obj = NumArray(nums)
print(obj.sumRange(0,2))
print(obj.sumRange(2,5))
print(obj.sumRange(0,5))
