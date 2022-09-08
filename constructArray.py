from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        l = n - (k + 1)
        r = k + 1
        res = [i + 1 for i in range(l)]

        for j in range(r):
            if j % 2 == 0:
                res.append(n - k + j // 2)
            else:
                res.append(n - j // 2)

        return res


n = 3
k = 1
n = 3
k = 2
n = 5
print(Solution().constructArray(n, k))
