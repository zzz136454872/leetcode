from typing import List


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        nums.sort()

        out = []

        for i in range(len(nums)):
            if (i == 0 or nums[i - 1] < nums[i] - 1) and (
                    i == len(nums) - 1 or nums[i + 1] > nums[i] + 1):
                out.append(nums[i])

        return out


nums = [10, 6, 5, 8]
nums = [1, 3, 5, 3]
print(Solution().findLonely(nums))
