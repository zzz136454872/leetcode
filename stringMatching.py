from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))
        res = []

        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if words[j].find(words[i]) != -1:
                    res.append(words[i])

                    break

        return res
