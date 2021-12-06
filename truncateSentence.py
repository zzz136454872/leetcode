class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        space = 0

        for i in range(len(s)):
            if s[i] == ' ':
                space += 1

                if space == k:
                    return s[:i]

        return s
