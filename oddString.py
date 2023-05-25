from typing import List


class Solution:
    def oddString(self, words: List[str]) -> str:
        def l2n(a):
            return ord(a) - ord('a')

        def w2l(word):
            res = []

            for i in range(len(word) - 1):
                res.append(l2n(word[i + 1]) - l2n(word[i]))

            return tuple(res)

        if w2l(words[0]) != w2l(words[1]):
            if w2l(words[0]) != w2l(words[2]):
                return words[0]

            return words[1]
        flag = w2l(words[0])

        for word in words[2:]:
            if w2l(word) != flag:
                return word

        return ''


words = ["adc", "wzy", "abc"]
words = ["aaa", "bob", "ccc", "ddd"]
print(Solution().oddString(words))
