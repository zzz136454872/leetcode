from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        r = n - 1

        while l <= r:
            mid = (l + r) // 2

            if (mid == 0 or nums[mid] > nums[mid - 1]) and (
                    mid == n - 1 or nums[mid] > nums[mid + 1]):
                return mid

            if mid == 0 or nums[mid] > nums[mid - 1]:
                l = mid + 1
            else:
                r = mid - 1

        return l


nums = [4, 1]
print(Solution().findPeakElement(nums))
