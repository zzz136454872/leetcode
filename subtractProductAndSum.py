from functools import reduce
from typing import List


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = list(map(int, list(str(n))))
        return reduce(lambda x, y: x * y, a) - sum(a)


n = 234
print(Solution().subtractProductAndSum(n))
