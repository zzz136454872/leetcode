from typing import *


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diffs = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffs.append(i)

        if len(diffs) == 0:
            return True

        if len(diffs) != 2:
            return False

        return s1[diffs[0]] == s2[diffs[1]] and s1[diffs[1]] == s2[diffs[0]]


sl = Solution()
s1 = "abcd"
s2 = "dcba"
print(sl.areAlmostEqual(s1, s2))
