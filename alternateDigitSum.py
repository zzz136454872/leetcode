from typing import List


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = list(map(int, list(str(n))))
        s = 1
        res = 0

        for i in range(len(n)):
            res += s * n[i]
            s = -s

        return res


n = 521
n = 111
n = 886996
print(Solution().alternateDigitSum(n))
