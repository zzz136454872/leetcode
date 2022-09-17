from typing import List


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        prev = {}
        res = -1

        for i in range(len(s)):
            if s[i] not in prev:
                prev[s[i]] = i
            else:
                res = max(res, i - prev[s[i]] - 1)

        return res
