from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        out = []

        for num in nums:
            s += num
            out.append(s)

        return out
