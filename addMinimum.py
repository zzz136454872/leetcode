class Solution:
    def addMinimum(self, word: str) -> int:
        i = 0
        j = 0
        s = 'abc'
        r = 0

        while i < len(word):
            while s[j] != word[i]:
                j = (j + 1) % 3
                r += 1
            j = (j + 1) % 3
            i += 1

        if j > 0:
            r += 3 - j

        return r


word = "b"
word = "aaa"
word = "abc"
print(Solution().addMinimum(word))
