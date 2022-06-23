from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        c = Counter(words)
        wc = len(words)
        wl = len(words[0])
        res = []

        for i in range(len(s) - wc * wl + 1):
            if Counter([s[i + j * wl:i + (j + 1) * wl]
                        for j in range(wc)]) == c:
                res.append(i)

        return res


s = "barfoothefoobarman"
words = ["foo", "bar"]
print(Solution().findSubstring(s, words))
