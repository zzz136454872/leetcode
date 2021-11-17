from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        out = 0

        def l2n(a):
            return ord(a) - ord('a')

        def genId(word):
            mask = 0

            for letter in word:
                mask |= (1 << l2n(letter))

            return (len(word), mask)

        wordId = [genId(word) for word in words]

        for i in range(len(wordId) - 1):
            id1 = wordId[i]

            for j in range(i + 1, len(wordId)):
                id2 = wordId[j]

                if id1[1] & id2[1] == 0 and id1[0] * id2[0] > out:
                    out = id1[0] * id2[0]

        return out


inp = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
inp = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
inp = ["a", "aa", "aaa", "aaaa"]
print(Solution().maxProduct(inp))
