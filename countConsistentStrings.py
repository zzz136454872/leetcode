from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = len(words)

        for word in words:
            for letter in word:
                if letter not in allowed:
                    res -= 1

                    break

        return res


allowed = "ab"
words = ["ad", "bd", "aaab", "baa", "badab"]
print(Solution().countConsistentStrings(allowed, words))
