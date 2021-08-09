from heapq import heappop, heappush
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]
        mem = set()

        for i in range(n - 1):
            now = heappop(heap)

            for prime in primes:
                tmp = prime * now

                if tmp not in mem:
                    heappush(heap, tmp)
                    mem.add(tmp)

        return heappop(heap)


sl = Solution()
n = 12
primes = [2, 7, 13, 19]
print(sl.nthSuperUglyNumber(n, primes))
