from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        out = 0
        total = 0

        for num in nums:
            total |= num

        def brutal(idx, lst):
            if idx == len(nums):
                tmp = 0

                for num in lst:
                    tmp |= num

                if tmp == total:
                    nonlocal out
                    out += 1

                return
            brutal(idx + 1, lst)
            brutal(idx + 1, lst + [nums[idx]])

        brutal(0, [])

        return out


nums = [3, 2, 1, 5]
nums = [i + 1 for i in range(16)]
print(Solution().countMaxOrSubsets(nums))
