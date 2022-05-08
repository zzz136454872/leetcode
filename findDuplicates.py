from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[nums[i] - 1] == nums[i]:
                    break
                else:
                    tmp = nums[i]
                    nums[i], nums[tmp - 1] = nums[tmp - 1], nums[i]

        return [nums[i] for i in range(len(nums)) if nums[i] != i + 1]


nums = [4, 3, 2, 7, 8, 2, 3, 1]
nums = [1, 1, 2]
print(Solution().findDuplicates(nums))
