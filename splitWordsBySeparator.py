from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str],
                              separator: str) -> List[str]:
        res = []

        for word in words:
            tmp = word.split(separator)

            for w in tmp:
                if len(w) > 0:
                    res.append(w)

        return res
