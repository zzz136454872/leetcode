class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mem = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        n = len(s)
        l0 = 0
        l1 = 0

        for letter in s[:n // 2]:
            if letter in mem:
                l0 += 1

        for letter in s[n // 2:]:
            if letter in mem:
                l1 += 1

        return l0 == l1


s = "book"
s = "textbook"
print(Solution().halvesAreAlike(s))
