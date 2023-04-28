from typing import List


def isFront(a, b):
    if len(a) != len(b) - 1:
        return False
    i = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            for j in range(i, len(a)):
                if a[j] != b[j + 1]:
                    return False

            break

    return True


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        b = [1]

        for i in range(1, len(words)):
            t = 1

            for j in range(i - 1, -1, -1):
                if isFront(words[j], words[i]):
                    t = max(t, b[j] + 1)
            b.append(t)

        return max(b)


words = ["a", "b", "ba", "bca", "bda", "bdca"]
words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
words = ["abcd", "dbqca"]
print(Solution().longestStrChain(words))
print(isFront('ab', 'bac'))
