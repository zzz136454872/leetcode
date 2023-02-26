from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        a = set(nums)
        a.discard(0)
        return len(a)
