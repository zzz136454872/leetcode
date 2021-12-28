from typing import List


def l2n(a):
    return ord(a) - ord('a')


class Trie:
    def __init__(self):
        self.has = False
        self.sons = [None for i in range(26)]

    def add(self, word):
        p = self

        for letter in word:
            idx = l2n(letter)

            if p.sons[idx] is None:
                p.sons[idx] = Trie()
            p = p.sons[idx]
        p.has = True


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        root = Trie()
        words.sort(key=lambda x: len(x))
        out = []

        def inside(word, idx):
            p = root

            if idx == len(word):
                return True

            for i in range(idx, len(word)):
                if p.sons[l2n(word[i])] is None:
                    return False
                else:
                    p = p.sons[l2n(word[i])]

                if p.has and inside(word, i + 1):
                    return True

            return False

        for word in words:
            if len(word) == 0:
                continue

            if inside(word, 0):
                out.append(word)
            else:
                root.add(word)

        return out


words = [
    "cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat",
    "ratcatdogcat"
]
words = ["cat", "dog", "catdog"]

print(Solution().findAllConcatenatedWordsInADict(words))
