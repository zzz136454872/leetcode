from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = 123456789000
        second = 123456789000

        for num in nums:

            if num > second:
                return True

            if num <= first:
                first = num

                continue

            if num < second:
                second = num

        return False


nums = [1, 2, 3, 4, 5]
nums = [5, 4, 3, 2, 1]
nums = [2, 1, 5, 0, 4, 6]
nums = [1, 1, -2, 6]

print(Solution().increasingTriplet(nums))
