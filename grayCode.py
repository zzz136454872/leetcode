from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        tmp = self.grayCode(n - 1)

        return tmp + [2**(n - 1) + i for i in tmp[::-1]]


n = 2
n = 3
print(Solution().grayCode(n))
