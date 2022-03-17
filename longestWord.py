from typing import List


class Trie:
    def __init__(self):
        self.has = False
        self.sons = [None for i in range(26)]


def l2n(a):
    return ord(a) - ord('a')


# 词典中最长的单词
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        out = ""
        root = Trie()

        for word in words:
            p = root
            flag = True

            for letter in word[:-1]:
                if p.sons[l2n(letter)] is None:
                    flag = False
                else:
                    p = p.sons[l2n(letter)]
            letter = word[-1]

            if flag and p.sons[l2n(letter)] is None:
                p.sons[l2n(letter)] = Trie()

                if len(out) < len(word):
                    out = word

        return out


words = ["w", "wo", "wor", "worl", "world"]
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
print(Solution().longestWord(words))


# 不知道是哪个
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: (-len(x), x))
        root = Trie()

        for word in words:
            p = root

            for letter in word:
                n = l2n(letter)

                if p.sons[n] is None:
                    p.sons[n] = Trie()
                p = p.sons[n]
            p.has = True

        def search(w, sp):
            i = sp
            p = root

            while i < len(w):
                p = p.sons[l2n(w[i])]

                if p is None:
                    return 0

                if p.has:
                    if search(w, i + 1) > 0:
                        return 2
                i += 1

            if p.has:
                return 1

            return 0

        for word in words:
            if search(word, 0) > 1:
                return word

        return ''


# sl = Solution()
# inp = ["cat", "banana", "dog", "nana", "walk", "walker", "dogwalker"]
# inp=['c','ccc']
# print(sl.longestWord(inp))
