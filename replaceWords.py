from typing import List


class TrieNode:
    def __init__(self):
        self.has = False
        self.sons = [None] * 26

    def __str__(self):
        return str(self.has) + ' ' + str(self.sons)


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        def l2n(a):
            return ord(a) - ord('a')

        root = TrieNode()

        for word in dictionary:
            p = root

            for letter in word:
                print(letter)
                loc = l2n(letter)

                if p.sons[loc] is None:
                    p.sons[loc] = TrieNode()
                p = p.sons[loc]

                if p.has:
                    break
            p.has = True

        words = sentence.split()
        res = []

        for word in words:
            p = root
            flag = False

            for i in range(len(word)):
                loc = l2n(word[i])

                if p.sons[loc] is None:
                    break
                p = p.sons[loc]

                if p.has:
                    res.append(word[:i + 1])
                    flag = True

                    break

            if not flag:
                res.append(word)

        return ' '.join(res)


dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
dictionary = ["a", "b", "c"]
sentence = "aadsfasf absbs bbab cadsfafs"
print(Solution().replaceWords(dictionary, sentence))
