from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        c1 = 0
        c2 = 1
        out = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                c2 += 1
            elif nums[i] == nums[i - 1] + 1:
                if c1 > 0:
                    out = max(out, c1 + c2)
                c1, c2 = c2, 1
            else:
                if c1 > 0:
                    out = max(out, c1 + c2)
                c1, c2 = 0, 1

        if c1 > 0:
            out = max(out, c1 + c2)

        return out


nums = [1, 3, 2, 2, 5, 2, 3, 7]
nums = [1, 2, 3, 4]
nums = [1, 1, 1, 1]
print(Solution().findLHS(nums))
