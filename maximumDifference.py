from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        out = -1
        premin = 10**9 + 1

        for num in nums:
            out = max(out, num - premin)
            premin = min(num, premin)

        return out if out != 0 else -1


nums = [7, 1, 5, 4]
nums = [9, 4, 3, 2]
nums = [1, 5, 2, 10]

print(Solution().maximumDifference(nums))
