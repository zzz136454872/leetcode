class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)

        if idx == -1:
            return word

        return ''.join(list(word[:idx + 1])[::-1]) + word[idx + 1:]


word = "abcdefd"
ch = "d"
print(Solution().reversePrefix(word, ch))
