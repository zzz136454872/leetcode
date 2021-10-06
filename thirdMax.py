from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)), reverse=True)

        if len(nums) < 3:
            return nums[0]

        return nums[2]


nums = [3, 2, 1]
nums = [1, 2]
nums = [2, 2, 3, 1]
print(Solution().thirdMax(nums))
