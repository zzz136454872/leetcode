from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        out = 0
        n = len(nums)

        for i in range(n // 2):
            out = max(out, nums[i] + nums[n - 1 - i])

        return out


sl = Solution()
nums = [3, 5, 2, 3]
nums = [3, 5, 4, 2, 4, 6]
print(sl.minPairSum(nums))
