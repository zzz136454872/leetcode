from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        digits = sorted([int(x) for x in digits])

        def sub1(d, nn):
            s = len(digits)

            ln = len(str(n))

            return s

        return sub1(digits, n)
