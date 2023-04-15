class Solution:
    def longestDecomposition(self, text: str) -> int:
        if len(text) == 0:
            return 0

        for i in range(1, len(text) // 2 + 1):
            if text[:i] == text[-i:]:
                return 2 + self.longestDecomposition(text[i:len(text) - i])

        return 1


text = 'ghiabcdefhelloadamhelloabcdefghi'
text = "merchant"
print(Solution().longestDecomposition(text))
