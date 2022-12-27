from typing import List


class Solution:
    def minimumMoves(self, s: str) -> int:
        s = list(s)
        i = 0
        res = 0

        while i < len(s):
            if s[i] == 'X':
                s[i] = '0'
                res += 1
                i += 1

                if i < len(s):
                    s[i] = '0'
                i += 1

                if i < len(s):
                    s[i] = '0'
            i += 1

        return res


s = "XXX"
s = "XXOX"
s = "OOOO"
print(Solution().minimumMoves(s))
