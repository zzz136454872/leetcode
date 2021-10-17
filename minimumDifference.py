from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        out = 123456
        k -= 1

        for i in range(len(nums) - k):
            out = min(out, nums[i + k] - nums[i])

        return out


nums = [90]
k = 1
nums = [9, 4, 1, 7]
k = 2
print(Solution().minimumDifference(nums, k))
