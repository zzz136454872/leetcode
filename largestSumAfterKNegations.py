from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0

        while k >= 1 and i < len(nums):
            if nums[i] < 0:
                nums[i] = -nums[i]
            else:
                break
            i += 1
            k -= 1
        nums.sort()

        if k % 2 != 0:
            nums[0] = -nums[0]

        return sum(nums)


nums = [4, 2, 3]
k = 1
nums = [3, -1, 0, 2]
k = 3
nums = [2, -3, -1, 5, -4]
k = 2
print(Solution().largestSumAfterKNegations(nums, k))
