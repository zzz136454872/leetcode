from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        c = [0] * n

        if k >= 0:
            p = k
            s = 0

            for i in range(1, k + 1):
                s += code[i]

            for i in range(n):
                c[i] = s
                s -= code[(i + 1) % n]
                p = (p + 1) % n
                s += code[p]

            return c
        else:
            p = n + k
            s = 0

            for i in range(n + k, n):
                s += code[i]

            for i in range(n):
                c[i] = s
                s += code[i]
                s -= code[p]
                p = (p + 1) % n

            return c


code = [5, 7, 1, 4]
k = 3
code = [1, 2, 3, 4]
k = 0
code = [2, 4, 9, 3]
k = -2
print(Solution().decrypt(code, k))
