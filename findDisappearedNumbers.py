from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(len(nums)):
            nums[nums[i] % n - 1] += 1000000
        out = []
        print(nums)

        for i in range(len(nums)):
            if nums[i] <= n:
                out.append(i + 1)

        return out


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(Solution().findDisappearedNumbers(nums))
exp = [5, 6]
