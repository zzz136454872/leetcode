from collections import Counter
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        w1 = Counter(words1)
        w2 = Counter(words2)
        res = 0

        for k in w1:
            if w1[k] == 1 and w2[k] == 1:
                res += 1

        return res
