from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        res = set()

        while i < j:
            tmp = nums[i] + nums[j]
            i += 1
            j -= 1
            res.add(tmp)

        return len(res)


nums = [4, 1, 4, 0, 3, 5]
nums = [1, 100]
print(Solution().distinctAverages(nums))
