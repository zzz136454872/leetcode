from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        out = 1
        MOD = 1337

        for num in b[::-1]:
            out = (out * a**num) % MOD
            a = (a**10) % MOD

        return out


a = 2
b = [3]
a = 2
b = [1, 0]
a = 1
b = [4, 3, 3, 8, 5, 2]
a = 2147483647
b = [2, 0, 0]
print(Solution().superPow(a, b))
