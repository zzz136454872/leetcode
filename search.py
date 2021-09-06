from typing import List


class Solution1:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums


# I. 在排序数组中查找数字 I
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.count(target)


# 二分查找
class Solution1:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid

        return -1


sl = Solution()
nums = [1, 0, 1, 1, 1]
target = 0
print(sl.search(nums, target))
