from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: (x[1], x[0]))
        mem = [1] * len(pairs)

        for i in range(len(pairs)):
            for j in range(i - 1, -1, -1):
                if pairs[j][1] < pairs[i][0]:
                    mem[i] = max(mem[i], mem[j] + 1)

        return max(mem)


inp = [[1, 2], [2, 3], [3, 4]]
print(Solution().findLongestChain(inp))
