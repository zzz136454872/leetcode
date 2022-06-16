from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        j = 0

        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while j < len(nums) and nums[j] - nums[i] <= k:
                j += 1
            j -= 1

            if i != j and nums[j] - nums[i] == k:
                res += 1

        return res


nums = [3, 1, 4, 1, 5]
k = 2
nums = [1, 2, 3, 4, 5]
k = 1
nums = [1, 3, 1, 5, 4]
k = 0
print(Solution().findPairs(nums, k))
