from typing import List


class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)

        for i in range(len(s)):
            if s[i] == '?':
                test = set(['a', 'b', 'c'])

                if i > 0:
                    test.discard(s[i - 1])

                if i < len(s) - 1:
                    test.discard(s[i + 1])
                s[i] = test.pop()

        return ''.join(s)


s = "?zs"
s = "ubv?w"
s = "j?qg??b"
print(Solution().modifyString(s))
