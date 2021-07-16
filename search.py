from typing import List


class Solution1:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums


# I. 在排序数组中查找数字 I
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.count(target)


sl = Solution()
nums = [1, 0, 1, 1, 1]
target = 0
print(sl.search(nums, target))
