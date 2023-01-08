from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        n = len(pref)

        for word in words:
            if word[:n] == pref:
                res += 1

        return res


words = ["pay", "attention", "practice", "attend"]
pref = "at"
words = ["leetcode", "win", "loops", "success"]
pref = "code"
print(Solution().prefixCount(words, pref))
