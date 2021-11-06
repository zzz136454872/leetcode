from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            # print(i,nums[i])

            if nums[i] != i and nums[i] < len(nums):
                c = nums[i]
                nums[i], nums[c] = nums[nums[i]], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)


nums = [3, 0, 1]
nums = [0, 1]
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
nums = [0]
print(Solution().missingNumber(nums))
