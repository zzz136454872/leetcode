class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mem = [0] * 26
        mod = 10**9 + 7

        for letter in s:
            i = ord(letter) - ord('a')
            mem[i] = (1 + sum(mem)) % mod

        return sum(mem) % mod


s = "abc"
s = "aba"
print(Solution().distinctSubseqII(s))
