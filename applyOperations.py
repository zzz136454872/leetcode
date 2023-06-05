from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        n1 = []
        n2 = 0

        for num in nums:
            if num != 0:
                n1.append(num)
            else:
                n2 += 1

        return n1 + [0] * n2


nums = [1, 2, 2, 1, 1, 0]
print(Solution().applyOperations(nums))

