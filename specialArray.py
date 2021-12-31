from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(nums[-1] + 1):
            l = 0
            r = len(nums) - 1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] >= i:
                    r = mid - 1
                else:
                    l = mid + 1

            if len(nums) - l == i:
                return i

        return -1


nums = [3, 5]
nums = [0, 0]
nums = [0, 4, 3, 0, 4]
nums = [3, 6, 7, 7, 0]
print(Solution().specialArray(nums))
