from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        i = 0
        mem = [False] * n
        i = 0
        c=k

        while True:
            if mem[i]:
                return [i + 1 for i in range(n) if not mem[i]]
            mem[i] = True
            i = (i + c) % n
            c = (c+k)%n


n = 5
k = 2
print(Solution().circularGameLosers(n, k))
