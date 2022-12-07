from typing import *


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word = list(word)

        for i in range(len(word)):
            if not word[i].isdigit():
                word[i] = ' '
        word = ''.join(word).split()
        tmp = set()

        for w in word:
            tmp.add(int(w))

        return len(tmp)


sl = Solution()
word = "a123bc34d8ef34"
word = "a1b01c001"
print(sl.numDifferentIntegers(word))
