from typing import List


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        af = [123456] * (len(nums) + 1)

        for i in range(len(nums) - 2, -1, -1):
            af[i] = min(af[i + 1], nums[i + 1])
        pre = nums[0]
        res = 0

        for i in range(1, len(nums) - 1):
            if nums[i] > pre and nums[i] < af[i]:
                res += 2
            elif nums[i] > nums[i - 1] and nums[i + 1] > nums[i]:
                res += 1
            pre = max(pre, nums[i])

        return res


nums = [1, 2, 3]
nums = [2, 4, 6, 4]
nums = [3, 2, 1]

print(Solution().sumOfBeauties(nums))
