from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        def grey(a):
            if a == 0:
                return [0]
            t = grey(a - 1)
            res = t + [2**(a - 1) + x for x in t[::-1]]

            return res

        tmp = grey(n)

        for i in range(len(tmp)):
            if tmp[i] == start:
                break

        return tmp[i:] + tmp[:i]


n = 2
start = 3
n = 3
start = 2
print(Solution().circularPermutation(n, start))
