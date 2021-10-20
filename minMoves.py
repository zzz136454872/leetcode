from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        a = min(nums)

        return sum([num - a for num in nums])
