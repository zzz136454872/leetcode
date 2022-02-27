from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        nums = [str(a) for a in nums]

        if len(nums) <= 2:
            return '/'.join(nums[:2])

        return nums[0] + '/(' + '/'.join(nums[1:]) + ')'


inp = [1000, 100, 10, 2]
inp = [2]
print(Solution().optimalDivision(inp))
