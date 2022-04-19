from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        table = [-10**4 - 100]

        for i in range(len(s)):
            if s[i] == c:
                table.append(i)
        table.append(2 * 10**4 + 100)
        j = 0
        res = []

        for i in range(len(s)):
            while i >= table[j]:
                j += 1
            res.append(min(i - table[j - 1], table[j] - i))

        return res
