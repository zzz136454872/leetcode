class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i = 0
        j = len(s) - 1
        vo = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        while i < j:
            while i < j and s[i] not in vo:
                i += 1

            while i < j and s[j] not in vo:
                j -= 1

            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return ''.join(s)


s = "leetcode"
sl = Solution()
print(sl.reverseVowels(s))
