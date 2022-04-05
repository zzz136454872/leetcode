from typing import List


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        out = 0

        def isPrimeSet(a):
            return bin(a).count('1') in primes

        for i in range(left, right + 1):
            if isPrimeSet(i):
                out += 1

        return out


left = 6
right = 10
left = 10
right = 15
left = 990
right = 1048
print(Solution().countPrimeSetBits(left, right))
