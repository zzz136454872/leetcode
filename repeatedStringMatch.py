from typing import List


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if len(b) == 0:
            return 0
        k = len(b) // len(a)

        if len(a) * k == len(b) and b in a * k:
            return k

        if b in a * (k + 1):
            return k + 1

        if b in a * (k + 2):
            return k + 2

        return -1


a = "abcd"
b = "cdabcdab"
a = "a"
b = "aa"
a = "a"
b = "a"
a = "abc"
b = "wxyz"
print(Solution().repeatedStringMatch(a, b))
