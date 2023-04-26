class Solution:
    def lastSubstring(self, s: str) -> str:
        i = 0
        j = 1
        k = 0

        while j + k < len(s):
            if s[i + k] == s[j + k]:
                k += 1
            elif s[i + k] > s[j + k]:
                j += k + 1
                k = 0
            else:
                i += k + 1

                if i >= j:
                    j = i + 1
                k = 0

        return s[i:]


s = "abab"
# s = "leetcode"
print(Solution().lastSubstring(s))
