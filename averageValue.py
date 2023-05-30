from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        c = 0
        a = 0

        for num in nums:
            if num % 6 == 0:
                c += 1
                a += num

        return a // c if c != 0 else 0
