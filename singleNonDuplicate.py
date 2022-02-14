from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if mid % 2 != 0:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                elif nums[mid] == nums[mid + 1]:
                    right = mid - 1
                else:
                    return nums[mid]
            else:
                if mid == 0 or mid == len(nums) - 1:
                    return nums[mid]

                if nums[mid] == nums[mid + 1]:
                    left = mid + 1
                elif nums[mid] == nums[mid - 1]:
                    right = mid - 1
                else:
                    return nums[mid]

        return -1


nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
nums = [3, 3, 7, 7, 10, 11, 11]
nums = [1, 1, 2]
print(Solution().singleNonDuplicate(nums))
