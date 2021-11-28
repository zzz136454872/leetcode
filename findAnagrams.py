from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pid = [0] * 26

        def l2n(a):
            return ord(a) - ord('a')

        for letter in p:
            pid[l2n(letter)] += 1
        lp = len(p)

        for letter in s[:lp]:
            pid[l2n(letter)] -= 1
        out = []

        if not any(pid):
            out.append(0)

        for i in range(lp, len(s)):
            pid[l2n(s[i - lp])] += 1
            pid[l2n(s[i])] -= 1

            if not any(pid):
                out.append(i - lp + 1)

        return out


s = "cbaebabacd"
p = "abc"
s = "abab"
p = "ab"
print(Solution().findAnagrams(s, p))
