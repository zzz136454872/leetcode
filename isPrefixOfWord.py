class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s = sentence.split()
        n = len(searchWord)

        for i in range(len(s)):
            if len(s[i]) >= n and s[i][:n] == searchWord:
                return i + 1

        return -1
