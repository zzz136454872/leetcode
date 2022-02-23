from collections import Counter, defaultdict
from typing import List


class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        table = [0] * (2**len(primes))
        table[0] = 1
        mem = defaultdict(int)
        mod = 10**9 + 7

        for num in nums:
            mem[num] += 1

        for k, v in mem.items():
            if k == 1:
                continue
            flag = False
            subs = 0

            for i in range(len(primes)):
                if k % (primes[i]**2) == 0:
                    flag = True

                    break
                elif k % primes[i] == 0:
                    subs |= 1 << i

            if flag:
                continue

            for i in range(2**len(primes) - 1, 0, -1):
                if i & subs == subs:
                    table[i] = (table[i] + table[i ^ subs] * v) % mod

        return sum(table[1:]) * 2**mem[1] % mod


nums = [1, 2, 3, 4]
nums = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
]
print(Solution().numberOfGoodSubsets(nums))
