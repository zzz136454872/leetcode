from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        out = 0

        for i in range(2**len(requests)):
            mem = [0 for i in range(n)]
            c = 0

            for j in range(len(requests)):
                if (i & (1 << j)):
                    c += 1
                    mem[requests[j][0]] -= 1
                    mem[requests[j][1]] += 1

            if not any(mem):
                out = max(out, c)

        return out


n = 5
requests = [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]
n = 3
requests = [[0, 0], [1, 2], [2, 1]]
print(Solution().maximumRequests(n, requests))
