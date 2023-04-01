from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        mem = set()

        for i in range(len(nums) - 1):
            t = nums[i] + nums[i + 1]

            if t in mem:
                return True
            mem.add(t)

        return False


nums = [4, 2, 4]
nums = [1, 2, 3, 4, 5]
nums = [0, 0, 0]
print(Solution().findSubarrays(nums))
