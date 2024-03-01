from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        mem = [False] * len(nums)

        for i in range(n):
            if i > 0 and not mem[i - 1]:
                continue

            if i < n - 1 and nums[i] == nums[i + 1]:
                mem[i + 1] = True

            if i < n - 2:
                if nums[i] == nums[i + 1] and nums[i + 1] == nums[
                        i + 2] or nums[i] + 1 == nums[
                            i + 1] and nums[i + 1] + 1 == nums[i + 2]:
                    mem[i + 2] = True

        return mem[-1]


nums = [4, 4, 4, 5, 6]
nums = [1, 1, 1, 2]
print(Solution().validPartition(nums))
