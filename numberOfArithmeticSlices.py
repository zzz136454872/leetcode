from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        diff = [nums[i] - nums[i - 1] for i in range(1, len(nums))]

        out = 0
        val = -1
        count = 0

        for v in diff:
            if v == val:
                count += 1
                out += count - 1
            else:
                count = 1
                val = v

        return out


sl = Solution()
nums = [1, 2, 3, 4]
nums = [1]
print(sl.numberOfArithmeticSlices(nums))
