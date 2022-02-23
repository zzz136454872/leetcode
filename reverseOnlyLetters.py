class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        s = list(s)

        while i < j:
            while i < j and not s[i].isalpha():
                i += 1

            while i < j and not s[j].isalpha():
                j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return ''.join(s)


s = "ab-cd"
s = "a-bC-dEf-ghIj"
s = "Test1ng-Leet=code-Q!"
print(Solution().reverseOnlyLetters(s))
