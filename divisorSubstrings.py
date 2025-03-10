from typing import List


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        l = len(s)
        res = 0

        for i in range(l - k + 1):
            t = int(s[i:i + k])

            if t == 0:
                continue

            if num % t == 0:
                res += 1

        return res


num = 240
k = 2
num = 430043
k = 2
print(Solution().divisorSubstrings(num, k))
