class Solution:
    def greatestLetter(self, s: str) -> str:
        u = [0] * 26
        l = [0] * 26

        for letter in s:
            if letter.isupper():
                u[ord(letter) - ord('A')] = 1
            elif letter.islower():
                l[ord(letter) - ord('a')] = 1

        res = -1

        for i in range(26):
            if u[i] == 1 and l[i] == 1:
                res = i

        if res == -1:
            return ""

        return chr(res + ord('A'))


s = "lEeTcOdE"
s = "arRAzFif"
s = "AbCdEfGhIjK"
print(Solution().greatestLetter(s))
