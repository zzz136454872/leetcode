from typing import List


class Solution:
    def securityCheck(self, capacities: List[int], k: int) -> int:
        cap = [x - 1 for x in capacities]
        mem = {0: 1}
        mod = 10**9 + 7

        for c in cap:
            nmem = mem.copy()

            for key in mem:
                if key + c <= k:
                    if key + c in nmem:
                        nmem[key + c] = (nmem[key + c] + mem[key]) % mod
                    else:
                        nmem[key + c] = mem[key]
            mem = nmem

        return mem.get(k, 0)


capacities = [2, 2, 3]
k = 2
capacities = [3, 3]
k = 3
capacities = [4, 3, 2, 2]
k = 6
print(Solution().securityCheck(capacities, k))
