from typing import List


class Solution:
    def countAsterisks(self, s: str) -> int:
        state = 0
        res = 0

        for l in s:
            if l == '|':
                state ^= 1
            elif l == '*' and state == 0:
                res += 1

        return res


s = "l|*e*et|c**o|*de|"
s = "iamprogrammer"
s = "yo|uar|e**|b|e***au|tifu|l"
print(Solution().countAsterisks(s))
