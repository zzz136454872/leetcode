class Solution:
    def maxPower(self, s: str) -> int:
        out = 1
        tmp = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                tmp += 1
                out = max(out, tmp)
            else:
                tmp = 1

        return out
