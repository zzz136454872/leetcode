from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum(1 if words[i] == s[:len(words[i])] else 0
                   for i in range(len(words)))
