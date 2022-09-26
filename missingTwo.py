from typing import List


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        n = len(nums) + 2
        nums.append(-1)
        nums.append(-1)
        nums.append(-1)

        for i in range(n + 1):
            while nums[i] != i and nums[i] != -1:
                tmp = nums[i]
                nums[i] = nums[tmp]
                nums[tmp] = tmp

        res = []

        for i in range(1, n + 1):
            if nums[i] != i:
                res.append(i)

        return res


nums = [1]
nums = [2, 3]

print(Solution().missingTwo(nums))
