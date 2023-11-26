from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        return len(set(nums + [int(str(a)[::-1]) for a in nums]))


nums = [1, 13, 10, 12, 31]
nums = [2, 2, 2]
print(Solution().countDistinctIntegers(nums))
