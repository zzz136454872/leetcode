from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        out = 0

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                for k in range(j + 1, len(nums) - 1):
                    for h in range(k + 1, len(nums)):
                        if nums[i] + nums[j] + nums[k] == nums[h]:
                            out += 1

        return out


nums = [1, 2, 3, 6]
nums = [3, 3, 6, 4, 5]
nums = [1, 1, 1, 3, 5]
nums = [28, 8, 49, 85, 37, 90, 20, 8]
print(Solution().countQuadruplets(nums))
