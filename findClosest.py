from collections import defaultdict
from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        mem = defaultdict(list)

        for i in range(len(words)):
            mem[words[i]].append(i)
        l1 = mem[word1]
        l2 = mem[word2]
        j = 0
        res = 1234567

        for i in range(len(l1)):
            res = min(res, abs(l1[i] - l2[j]))

            while l1[i] > l2[j]:
                if j == len(l2) - 1:
                    break
                j += 1
                res = min(res, abs(l1[i] - l2[j]))

        return res


words = [
    "I", "am", "a", "student", "from", "a", "university", "in", "a", "city"
]
word1 = "a"
word2 = "student"

print(Solution().findClosest(words, word1, word2))
