class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)

        def nice(st):
            mem = {}

            for letter in st:
                if letter.isupper():
                    letter = letter.lower()
                    mem[letter] = mem.get(letter, 0) | 2
                else:
                    mem[letter] = mem.get(letter, 0) | 1

            for v in mem.values():
                if v != 3:
                    return False

            return True

        out = ''

        for i in range(n - 1):
            for j in range(i + 1, n):
                if j - i + 1 <= len(out):
                    continue

                if nice(s[i:j + 1]):
                    out = s[i:j + 1]

        return out


s = "YazaAay"
print(Solution().longestNiceSubstring(s))
