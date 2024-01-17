from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        words1 = set(words)
        res = 0

        for word in words:
            tmp = word[::-1]

            if word != tmp and tmp in words1:
                res += 1

        return res // 2


words = ["cd", "ac", "dc", "ca", "zz"]
print(Solution().maximumNumberOfStringPairs(words))
