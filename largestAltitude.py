from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        tmp = 0
        res = 0

        for g in gain:
            tmp += g
            res = max(tmp, res)

        return res
