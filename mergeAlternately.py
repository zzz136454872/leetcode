from typing import *


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = ''

        while word1 or word2:
            if word1:
                out += word1[0]
                word1 = word1[1:]

            if word2:
                out += word2[0]
                word2 = word2[1:]

        return out


sl = Solution()
word1 = "ab"
word2 = "pqrs"
print(sl.mergeAlternately(word1, word2))
# 输出："apbqcd"
