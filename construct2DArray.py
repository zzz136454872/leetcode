from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int,
                         n: int) -> List[List[int]]:
        if len(original) != n * m:
            return []
        out = []
        idx = 0

        for i in range(m):
            tmp = []

            for j in range(n):
                tmp.append(original[idx])
                idx += 1
            out.append(tmp)

        return out


original = [1, 2, 3, 4]
m = 2
n = 2
original = [1, 2, 3]
m = 1
n = 3
original = [1, 2]
m = 1
n = 1
original = [3]
m = 1
n = 2
print(Solution().construct2DArray(original, m, n))
