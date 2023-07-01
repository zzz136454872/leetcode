from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted([(nums[i], i) for i in range(len(nums))])
        i = 0
        j = len(nums) - 1

        while i < j:
            a = nums[i][0] + nums[j][0]

            if a == target:
                return [nums[i][1], nums[j][1]]
            elif a > target:
                j -= 1
            else:
                i += 1

        return [-1, -1]


nums = [2, 7, 11, 15]
target = 9
nums = [3, 2, 4]
target = 6
nums = [3, 2, 4]
target = 6
print(Solution().twoSum(nums, target))
